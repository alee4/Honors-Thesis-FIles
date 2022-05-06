import pandas as pd
#https://github.com/mattpodolak/pmaw, Pushshift Multithread API Wrapper
from pmaw import PushshiftAPI
from datetime import datetime, timedelta

#collect data from JoeRogan Subreddit every 2 hours, can be expanded to multiple subreddits
def gather_data():
    api = PushshiftAPI()
    #https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/14-Reddit-Data.html

    curr_date = int(datetime.now().timestamp())
    last_day = int((datetime.now() - timedelta(hours = 1)).timestamp())

    limit = None

    #JoeRogan, walkaway, WorkReform, ukraine, ivermectin, conspiracy, Russia, Coronavirus, China_Flu, HermanCainAward
    #antiwork, politics, Conservative

    subreddit_list = ["JoeRogan", "walkaway", "WorkReform", "ukraine", "ivermectin", "conspiracy", 
                      "Russia", "Coronavirus", "China_Flu", 
                      "HermanCainAward", "antiwork", "politics", "Conservative", "progressive", "Libertarian"]

    for subreddit in subreddit_list:
        print("start: " + subreddit)
    #   comments = api.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
        comments = api.search_comments(subreddit=subreddit, limit=limit, before=curr_date, after=last_day)

        print(f'Retrieved {len(comments)} comments from Pushshift')

        comments_df = pd.DataFrame(comments)

        curr_date_raw = datetime.now()
        string_time = curr_date_raw.strftime('%m-%d-%Y %H:%M')

        file_name = '/users/a/l/alee4/ThesisFiles/' + str(subreddit) + '/' + str(string_time) + "_" + str(subreddit)

        #print(file_name)
        comments_df.to_csv(file_name, header=True, index=False, columns=list(comments_df.axes[1]))

gather_data()

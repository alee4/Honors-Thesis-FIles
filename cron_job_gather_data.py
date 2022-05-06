import pandas as pd
#https://github.com/mattpodolak/pmaw, Pushshift Multithread API Wrapper
from pmaw import PushshiftAPI
import datetime as dt



def gather_data():
    api = PushshiftAPI()
    #https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/14-Reddit-Data.html

    curr_date = dt.datetime.now()
    last_hour = curr_date - timedelta(hours = 1)



    subreddit="JoeRogan"

    comments = api.search_comments(subreddit=subreddit, after=last_hour)

    print(f'Retrieved {len(comments)} comments from Pushshift')

    comments_df = pd.DataFrame(comments)
    comments_df.to_csv('./JoeRogan.csv', header=True, index=False, columns=list(comments_df.axes[1]))

gather_data()

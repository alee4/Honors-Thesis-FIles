#https://www.jcchouinard.com/how-to-use-reddit-api-with-python/
#
#gets most recent comments with the query word
import requests
import json
# query="covid" #Define Your Query
# url = f"https://api.pushshift.io/reddit/search/comment/?q={query}"
# request = requests.get(url)
# json_response = request.json()
# json_response
#
# with open('demo.txt', 'w') as demo_file:
#      demo_file.write(json.dumps(json_response) + "\n")
# demo_file.close()
#
# # print(json_response)
# print("Data successfully written to file.")


def get_pushshift_data(data_type, **kwargs):
    """
    Gets data from the pushshift api.

    data_type can be 'comment' or 'submission'
    The rest of the args are interpreted as payload.

    Read more: https://github.com/pushshift/api
    """

    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

data_type="comment"     # give me comments, use "submission" to publish something
query="python"          # Add your query
duration="30d"          # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
size=1000               # maximum 1000 comments
sort_type="score"       # Sort by score (Accepted: "score", "num_comments", "created_utc")
sort="desc"             # sort descending
aggs="subreddit"        #"author", "link_id", "created_utc", "subreddit"


json_response = get_pushshift_data(data_type=data_type,
                   q=query,
                    after=duration,
                    size=size,
                    sort_type=sort_type,
                    sort=sort)


with open('keywords.txt', 'w') as f:
    f.write(json.dumps(json_response, indent=4, sort_keys=True))
f.close()



#data = get_pushshift_data(data_type=data_type,
 #                         q=query,
  #                        after=duration,
  #                        size=size,
  #                        aggs=aggs)


#data = data.get("aggs").get(aggs)


#with open('agggs.txt', 'w') as f:
#     f.write(json.dumps(json_response))
#f.close()


#TFIDF, check frequencies of words (the isnt important but prob very frequent)
#Natural language processor techniques ^^^^
#explore differnet threads/subreddits
#machine learning? support vector machine
#explore different dashboards

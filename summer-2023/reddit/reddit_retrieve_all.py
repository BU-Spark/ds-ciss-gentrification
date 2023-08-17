import praw
import json
import re
import csv
import spacy
import datetime

ner = spacy.load('en_core_web_sm')

credentials = 'client_secrets.json'
search_term = "(Gentrification of|gentrification of|Gentrification Of)"
regex = re.compile('([\s \S]*)'+search_term+'([\s \S]*)')
filename = "all_top.csv"

with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

# with open("reddit_gentrification_unique.csv", "a") as f:
#     csv_writer = csv.writer(f)

######## GET USERNAME, TIME OF COMMENT (IF POSSIBLE, LOCATION) ###########
with open(filename, "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["URL", "TITLE", "TEXT", "LEFT CONTEXT", "RIGHT CONTEXT", "AUTHOR USERNAME", "TIME CREATED"])

def search_posts(search_keywords, limit=1000):
    posts = []
    last_post_id = None
    subreddit = reddit.subreddit("all")

    #while True:
        # Search for posts containing the specified keywords with pagination
    results = subreddit.search(search_keywords, sort="top", limit = limit)#, params={'after': posts[-1].id} if posts else "")

        # if posts:
        #     print(posts[-1].id)

        #     results = subreddit.search(search_keywords, sort="relevance", limit = limit, params={'before': last_post_id, 'start_year': 2012, 'end_year':2013})
        # else:
        #     results = subreddit.search(search_keywords, sort="relevance", limit = limit, params={'start_year': 2012, 'end_year':2013})

        # if posts:
        #     results = subreddit.new(limit=limit, params={'before': last_post_id})
        # else:
        #     results = subreddit.new(limit=limit)

        # new_posts = [post for post in results if search_keywords.lower() in post.title.lower()]

        #new_posts = [submission for submission in results]

        # if not new_posts:
        #     break

        # print(new_posts)
        # posts.extend(new_posts)

        # # Update the last_post_id to the ID of the last post in the current results
        # last_post_id = new_posts[-1].id
        # print(last_post_id)
    with open(filename, "a") as f:
        csv_writer = csv.writer(f)
        for submission in results:
            posts.append(submission)
            print(submission.url)
            print(submission.title)
            print(submission.author.name)
            time_created = datetime.datetime.fromtimestamp(submission.created)
            print(time_created)
            try:
                groups = regex.match(submission.title).groups()
            except Exception:
                print("#####EXCEPTION############")
                print(Exception.__class__)
                print(submission.title)
                print(submission.url)
                
                print()
                continue
            left = groups[0].strip().replace("'", "").replace('"', '').replace(",", "").split(" ")[-4:]
            right = groups[2].strip().replace("'", "").replace('"', '').replace(",", "").split(" ")[:4]
            #store all in csv
            csv_writer.writerow([submission.url, submission.title, submission.selftext, left, right, submission.author.name, time_created])
            print()
                # posts.append(submission)
        print(len(posts))
    return posts
    
posts = search_posts("gentrification of")


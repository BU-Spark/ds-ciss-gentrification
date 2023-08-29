import praw
import json
import re
import csv
import spacy

ner = spacy.load('en_core_web_sm')

credentials = 'client_secrets.json'
search_term = "(Gentrification of|gentrification of|Gentrification Of)"
regex = re.compile('([\s \S]*)'+search_term+'([\s \S]*)')

# with open("reddit_gentrification_all.csv", "w") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(["URL", "TITLE", "TEXT", "LEFT CONTEXT", "RIGHT CONTEXT"])

with open("reddit_gentrification_unique.csv", "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["URL", "TITLE", "TEXT", "LEFT CONTEXT", "RIGHT CONTEXT"])

with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

with open("reddit_gentrification_unique.csv", "a") as f:
    csv_writer = csv.writer(f)
    for submission in reddit.subreddit("all").search("gentrification of", sort="relevance"):
        print(submission.url)
        print(submission.title)
        #print(submission.selftext)
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
        #csv_writer.writerow([submission.url, submission.title, submission.selftext, left, right])
        #create a separate file for the ones which are not identified as entities
        
        print()
        # print(left)
        # print(right)


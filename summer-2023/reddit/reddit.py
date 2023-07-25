import json 
import pandas as pd
import requests
  
subreddit = 'gentrification+of'
limit = 100
timeframe = 'year' #hour, day, week, month, year, all
listing = 'best' # controversial, best, hot, new, random, rising, top
  
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        #base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        base_url = f'https://www.reddit.com/r/gentrification+of/best.json?limit=1000&start_year=2010&end_year=2024'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 
def get_post_titles(r):
    '''
    Get a List of post titles
    '''
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts
 
def get_results(r):
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments'], 'selftext':post['data']['selftext']}
        print(post['data']['url'])
        print(post['data']['title'])
    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df
 
if __name__ == '__main__':
    r = get_reddit(subreddit,listing,limit,timeframe)
    df = get_results(r)
    print(df.shape)
    #print(df)
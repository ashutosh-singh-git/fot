from pprint import pprint

import feedparser
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('spotfin-app-firebase-adminsdk-y3hu0-94a797fc1d.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL':'https://spotfin-app-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# parsing blog feed
print(feedparser.__version__)
blog_feed = feedparser.parse('http://feeds.feedburner.com/nseindia/ann')

# getting lists of blog entries via .entries
posts = blog_feed.entries

# dictionary for holding posts details
posts_details = {"Blog title" : blog_feed.feed.title,
                 "Blog link" : blog_feed.feed.link}

post_list = []

# iterating over individual posts
for post in posts:
    temp = dict()

    # if any post doesn't have information then throw error.
    try:
        temp["title"] = post.title
        temp["link"] = post.link
        temp["description"] = post.description
        temp["time_published"] = post.published
        temp["tags"] = [tag.term for tag in post.tags]
        temp["authors"] = [author.name for author in post.authors]
        temp["summary"] = post.summary
    except:
        pass

    post_list.append(temp)

# storing lists of posts in the dictionary
posts_details["posts"] = post_list
ref = db.reference("/")
ref.set(posts_details)
pprint(posts_details)

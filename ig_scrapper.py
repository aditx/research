import pprint as pp
import json
import requests

tag = "foodporn"
url = "https://www.instagram.com/explore/tags/" + tag + "/?__a=1"

keys = [
    'id', 'owner', 'display_url', 'edge_media_to_caption'
]

def jprint(data_dict):
    print(json.dumps(data_dict, indent=4))

# Grab the data

def get_ig_page(url, session=None):
    print(url)
    session = session or requests.Session()

    r = session.get(url)
    r_code = r.status_code
    print(r_code)

    if r_code == requests.codes.ok:
        return r
    else:
        return None

ig_data_dict = get_ig_page(url)

if ig_data_dict is not None:
    ig_data_dict = ig_data_dict.json()
    #print(ig_data_dict)
    data = ig_data_dict.get('graphql', None)

    top_posts = data.get('hashtag', None)
    #print(top_posts)
    if top_posts is not None:
        edge_posts = top_posts.get('edge_hashtag_to_top_posts')
        if edge_posts is not None:
            edges = edge_posts.get('edges')
            #print(edges)

            for post in edges:
                data = post.get('node')
                #print(data.get('id'))
                for key in keys:
                    print(key.upper(), ":", data.get(key))
else:
    print ('Opps Error :)')
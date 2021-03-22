#!/bin/usr/env/python3

'''
uses json data from: https://www.instagram.com/<username>/?__a=1
'''

import requests
import re

class Bot:
    def __init__(self, username):
        self.user = username
        self.base_url = "https://www.instagram.com/"

    def getStats(self):
        url = "{}{}/".format(self.base_url, self.user)
        print(self.user)

        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/78.0.3904.108 Chrome/78.0.3904.108 Safari/537.36"}
        r = requests.get(url, headers=headers).text

        #name = str(re.search('"fullname":"[]"',r).group(1))
        #print(name)
        print(url)

        following = int(re.search('"edge_follow":{"count":([0-9]+)}',r).group(1))
        followers = int(re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1))
        print("Following: {}\nFollowers: {}\n".format(str(following), str(followers)))

        uploads = int(re.search('"edge_owner_to_timeline_media":{"count":([0-9]+)',r).group(1))
        print("Uploads: {}".format(str(uploads)))

        comments = re.findall('"edge_media_to_comment":{"count":([0-9]+)}',r)
        comm_count = 0
        for i in range(len(comments)):
            comm_count += int(comments[i])
        print("Comments: {}".format(str(comm_count)))

        likes = re.findall('"edge_liked_by":{"count":([0-9]+)}',r)
        like_count = 0
        for i in range(len(likes)):
            like_count += int(likes[i])
        print("Likes: {}".format(str(like_count)))

        '''comm_count = 0
        ids = re.findall('"shortcode":"([.]+)",',r)
        print(str(ids))
        for i in range(len(ids)):
            p = requests.get("{}p/{}/".format(self.base_url, ids[i]), headers=headers).text
            c = int(re.search('"edge_media_to_parent_comment":{"count":([0-9]+)',r).group(1))
            comm_count += c
            print(str(c))
        print("Comments: {}".format(str(comm_count)))'''


if __name__ == "__main__":
    username = input("Username: ")
    print("\n\n")
    bot = Bot(username)
    bot.getStats()

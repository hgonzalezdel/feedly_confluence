from datetime import date
import calendar
from feedly_client import FeedlyClient
import config

#Start feedly client
user_id = config.feedly_user_id
user_token = config.feedly_token

feedly_client = FeedlyClient(client_id=user_id, sandbox=False)

#Specify the stream you would like to get information from
stream = config.feedly_stream
today = calendar.timegm(date.today().timetuple())

feed_content = feedly_client.get_feed_content(access_token=user_token, streamId=stream, unreadOnly=True, newerThan=today)

print feed_content

feed_result = ""
for item in feed_content["items"]:
    feed_result += "Title: " + item["title"] + "\n"
    feed_result += "Summary: " + item["summary"]["content"] + "\n"
    feed_result += "Author: " + item["author"] + "\n"
    feed_result += "Link: " + item["originId"] + "\n"
    feed_result += "\n"

feed_result = feed_result.encode("utf-8")

#At the moment we only print the information. It will be pused to confluence in later iteration
print feed_result


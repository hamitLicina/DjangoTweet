import urllib.request
import os

if not os.path.exists('media/profile_pics'):
    os.makedirs('media/profile_pics')

url = "https://www.gravatar.com/avatar/default?s=200"
urllib.request.urlretrieve(url, "media/profile_pics/default.png")

print("Default profile picture has been downloaded successfully!") 
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)

html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"

result = re.search(pattern , html , re.IGNORECASE)

if result :
    title = result.group()
    title = re.sub("<.*?>", "", title)

    print(title)

else:
    print("Match not found")



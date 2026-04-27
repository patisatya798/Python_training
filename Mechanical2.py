import mechanicalsoup

browser = mechanicalsoup.Browser()
url ="http://olympus.realpython.org/login"

login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = browser.submit(form, login_page.url)

links = profiles_page.soup.select("a")

for link in links :
    adress = link["href"]
    text = link.text
    print(f"{text}: {adress}")

input = login_html.select("input")

for names in input:
    print(names.get("name") , names.get("value"))
    
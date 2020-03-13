import urllib.request as req
url="https://www.everydayhealth.com.tw/category/3/index/1"
request=req.Request(url, headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("li", class_="sub-menu-title")
with open("JOINT.txt", mode="w", encoding="utf-8") as file:
    file.write(root.title.string+"\n")
    file.write("---------------------------------------------------------"+"\n")
    for title in titles:
        if title.li !=None:
            file.write(title.a.string+"\n")
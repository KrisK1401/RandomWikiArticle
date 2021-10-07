import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title} \nWould you like to read it? (Y/N)")
    ans = input("").lower()

    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Let's try something else then.")
        continue
    else:
        print("The option are y or n, nice try tho")
        break

if __name__ == '__main__':
    print()
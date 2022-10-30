import requests
from bs4 import BeautifulSoup

pages = []


def get_links(directory, url):
    global pages
    html = requests.get(f"{url}{directory}").text
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                new_page = link.attrs["href"]
                pages.append(new_page)
                get_links(new_page, url)


def main():
    get_links("", "http://localhost:5500/")
    print("\n".join(pages))


if __name__ == "__main__":
    main()

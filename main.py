import requests
from bs4 import BeautifulSoup
from utils import control_target, manage_target, is_404

pages = []
TARGET_URL = "http://localhost:5500"

def get_links(url):
    global pages

    html = requests.get(f'{url}').text

    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a"):
        if "href" in link.attrs:
            potential_page = manage_target(TARGET_URL, link.attrs["href"])
            if (potential_page not in pages) and (control_target(TARGET_URL, potential_page)) and (not is_404(potential_page)):
                print(url, " ~~> ", potential_page)
                pages.append(potential_page)
                get_links(potential_page)


def main():
    get_links(TARGET_URL)
    #print("\n".join(pages))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('bye!!')

from utils import cmd, control_target, manage_target, control_status_code
from bs4 import BeautifulSoup

pages = []


def get_links(TARGET_URL, url):
    global pages

    potential_pages = []

    html = cmd(f'curl -Ls {url}')
    soup = BeautifulSoup(html, "html.parser")

    # Get all potential links
    for link in soup.find_all(['a', 'link']):
        if "href" in link.attrs:
            # variable name is potential_pages because of
            # there is a potential page and potential page may a redirect page
            potential_page = manage_target(TARGET_URL, link.attrs['href'])
            if control_target(TARGET_URL, potential_page):
                potential_pages.append(potential_page)

    # Control potential pages
    for potential_page in potential_pages:
        if potential_page not in pages:
            page = control_status_code(potential_page)
            if page:
                for p in page:
                    pages.append(p)

                print(f'[PAGE FOUND] {page[0]}')
                get_links(TARGET_URL, page[0])

    return pages

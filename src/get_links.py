from src.utils import cmd, control_target, manage_target, control_status_code
from bs4 import BeautifulSoup
import warnings

pages = []


def get_links(TARGET_URL, url):

    global pages

    html = cmd(f'curl -Ls {url}')
    soup = BeautifulSoup(html, "html.parser")
    warnings.filterwarnings('ignore')

    # Get all potential links
    html_tags = {
        "link": ["href"],
        "a": ["href", "data-jshref", "data-url"],
        "img": ["src", "data-lazy-src"],
        "div": ["data-url"],
        #"meta": ["content"],
        "input":["value"]
    }


    """
    for link in soup.find_all("a"):
        if "href" in link.attrs:
    """
    """
                    for html_potential_tag in html_potential_tags:
                #print(html_potential_tag)
                for attr in attr_list:
                    if attr in html_potential_tag.attrs:
                        
    """
    for html_tag in html_tags:
        #html_tag = link
        html_potential_tags = soup.find_all(html_tag)
        # link listesini cıkardık
        attr_list = html_tags[html_tag]
        #print(attr_list)
        for html_potential_tag in html_potential_tags:
            for attr in attr_list:
                if attr in html_potential_tag.attrs:
                    # variable name is potential_pages because of
                    # there is a potential page and potential page may a redirect page
                    potential_pages = manage_target(TARGET_URL, url, html_potential_tag.attrs[attr])
                    if potential_pages and potential_pages not in pages:
                        potential_pages = control_target(TARGET_URL, potential_pages)
                        if potential_pages:
                            print(f'[FOUND] {url} ~~> {potential_pages}')
                            for potential_page in potential_pages:
                                pages.append(potential_page)

                            get_links(TARGET_URL, potential_pages[0])  # just get that finish with / one ~> get blog/, not blog

    return pages

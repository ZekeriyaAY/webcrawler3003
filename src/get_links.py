from src.utils import cmd, control_target, manage_target, url_encode
from bs4 import BeautifulSoup
import warnings
from colorama import Fore
import sys
import os


pages = []
crawlingStatus = True   # crawling is active


def mkdir_pages(TARGET_URL):
    global pages

    for page in pages:
        if '//' in TARGET_URL:
            page = page.split('//', 1)[1]
        os.makedirs(f'output/{page}', exist_ok=True)
    
    return pages


def getPages():
    global pages
    return pages


def setCrawlingStatus(status):
    if status:  # If crawling starts
        pages.clear()

    global crawlingStatus
    crawlingStatus = status
    print(Fore.BLACK + '[CRAWLING STATUS]' + Fore.WHITE + f' {crawlingStatus}')


def get_links(TARGET_URL, url):
    global pages
    global crawlingStatus

    # print("[GET_LINKS] ", end="")
    url = url_encode(TARGET_URL, url)
    html = cmd("curl -Ls \"" + url + "\"")
    try:
        soup = BeautifulSoup(html, "html.parser")
    except:
        return
    warnings.filterwarnings('ignore')

    # Get all potential links
    html_tags = {
        "link": ["href"],
        "a": ["href", "data-jshref", "data-url"],
        "img": ["src", "data-lazy-src"],
        "div": ["data-url"],
        # "meta": ["content"],
        "input": ["value"]
    }

    for html_tag in html_tags:
        html_potential_tags = soup.find_all(html_tag)
        attr_list = html_tags[html_tag]
        for html_potential_tag in html_potential_tags:
            for attr in attr_list:
                if crawlingStatus == False:
                    print(Fore.BLACK + '[STOPPED]' + Fore.WHITE + f' {url}')
                    sys.exit()
                if attr in html_potential_tag.attrs:
                    # variable name is potential_pages because of
                    # there is a potential page and potential page may a redirect page

                    potential_pages = manage_target(
                        TARGET_URL, url, html_potential_tag.attrs[attr])
                    if potential_pages and potential_pages not in pages:
                        potential_pages = control_target(
                            TARGET_URL, potential_pages)
                        if potential_pages:
                            print(Fore.RED + '[FOUND]' + Fore.WHITE +
                                  f' {url} ~~> {potential_pages[0]}')
                            #print(f'[FOUND] {url_decode(TARGET_URL,url)} ~~> {url_decode(TARGET_URL,potential_pages[0])}')
                            for potential_page in potential_pages:
                                pages.append(potential_page)

                            # just get that finish with / one ~> get blog/, not blog
                            get_links(TARGET_URL, potential_pages[0])

    return pages

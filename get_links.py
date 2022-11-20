from utils import control_target, manage_target, cmd
from bs4 import BeautifulSoup

pages = []


def get_links(TARGET_URL, url):
    global pages

    html = cmd(f'curl -Ls {url}')
    soup = BeautifulSoup(html, "html.parser")

    for link in soup.find_all("a"):
        if "href" in link.attrs:
            # variable name is potential_pages because of
            # there is a potential page and potential page may a redirect page
            potential_pages = manage_target(TARGET_URL, link.attrs["href"])

            # YUKARIDAKİ FOR İLE SAYFADAKİ TÜM LİNKLERİ CRAW EDİLECEK, STATUS_CODE KONTROLÜ VEYA RECURSIVE OLMAYACAK
            # AŞAĞIDA DA PAGES İÇERİSİNDEKİLERİ KONTROL EDİP RECURSİVE OLARAK TEKRAR TARANACAK
            # BUNUN İÇİN 2. BİR PAGES LİSTESİ YAPILABİLİR GİBİ

            if potential_pages not in pages:
                potential_pages = control_target(TARGET_URL, potential_pages)
                if potential_pages:
                    print(url, " ~~> ", potential_pages)
                    for potential_page in potential_pages:
                        pages.append(potential_page)

                    get_links(TARGET_URL, potential_pages[0])  # just get that finish with / one ~> get blog/, not blog

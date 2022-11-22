from get_links import get_links
from get_imgs import get_imgs

TARGET_URL = "http://localhost:5500"


def main():
    print(f'\n\t[PAGE SCAN STARTED]')
    pages = get_links(TARGET_URL, TARGET_URL)
    print(f'\t[PAGE SCAN FINISHED]\n')

    print(f'\n\t[IMAGE SCAN STARTED]')
    images = get_imgs(pages)
    print(f'\t[IMAGE SCAN FINISHED]\n')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('bye!!')

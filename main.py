from src.get_links import get_links,pages
import colorama

def main():
    colorama.init()
    TARGET_URL = input("Target url: ")
    if TARGET_URL.endswith("/"):
        TARGET_URL = TARGET_URL[:-1]

    print(f'\n\t[PAGE SCAN STARTED]')
    pages = get_links(TARGET_URL, TARGET_URL)
    print(f'\t[PAGE SCAN FINISHED]\n')


if __name__ == "__main__":
    try:

        main()
    except KeyboardInterrupt:
        print(pages)
        print('bye!!')

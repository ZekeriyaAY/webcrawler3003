from get_links import get_links

TARGET_URL = "http://localhost:5500"


def main():
    get_links(TARGET_URL, TARGET_URL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('bye!!')

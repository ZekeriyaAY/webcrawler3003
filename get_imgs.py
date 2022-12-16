from utils import cmd, manage_image, control_status_code
from bs4 import BeautifulSoup


images = []


def get_imgs(pages):
    global images

    for page in pages:
        html = cmd(f'curl -Ls {page}')
        soup = BeautifulSoup(html, "html.parser")

        for img in soup.find_all('img'):
            if "src" in img.attrs:
                image = manage_image(page, img.attrs['src'])
                image = control_status_code(image)
                if image:
                    images.append(image[0])

                print(f'[IMAGE FOUND] {image[0]}')

    return images

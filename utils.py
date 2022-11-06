import requests


def control_target(TARGET_URL, test_url):
    return True if test_url.startswith(TARGET_URL) else False

def manage_target(TARGET_URL, target):
    if target.startswith("/"):
        target = TARGET_URL + target
    return target

def is_404(url):
    r = requests.get(f'{url}')
    return True if r.status_code == 404 else False

def robotsChecker():
    pass
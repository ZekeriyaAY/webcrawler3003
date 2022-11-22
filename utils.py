import subprocess


def cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()


def control_target(TARGET_URL, target):
    if target.startswith(TARGET_URL):
        return True
    return False


def manage_target(TARGET_URL, target):
    if target.startswith("/"):
        target = TARGET_URL + target
    return target


def manage_image(page, image):
    if not image.startswith("http"):
        image = page + image
    return image


def control_status_code(url):
    status_cmd = cmd("curl -LI " + url + " -w %{http_code} -s")
    status_code = int(status_cmd.split("\n")[0].split(" ")[1])

    if is_404(status_code):
        return None
    elif is_3xx(status_code):
        return [get_redirect(url), url]
    else:
        return [url]


def is_404(status_code):
    return True if (status_code == 404) else False


def is_3xx(status_code):
    return True if (status_code < 400 and status_code >= 300) else False


def get_redirect(url):
    redirect_url_draft = cmd("curl -Ls -w %{url_effective} " + url)
    return redirect_url_draft.split("\n")[-1]


def robotsChecker():
    pass

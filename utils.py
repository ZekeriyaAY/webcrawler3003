import subprocess


def cmd(cmd):
    print(cmd)
    try:
        return subprocess.check_output(cmd, shell=True).decode('utf-8', 'ignore')
    except:
        return subprocess.check_output(cmd, shell=True)

def is_404(status_code):
    return True if (status_code == 404) else False

def is_3xx(status_code):
    return True if (status_code < 400 and status_code >= 300) else False

def get_redirect(TARGET_URL, url):
    redirect_url_draft = cmd("curl -Ls -w %{url_effective} " + url)
    redirect_url_draft = redirect_url_draft.split("</html>")[-1].replace("\r","").replace("\n","")
    if not redirect_url_draft.startswith(TARGET_URL):
        return None
    return redirect_url_draft

def control_status_code(TARGET_URL, url):
    status_cmd = cmd("curl -LI " + url + " -w %{http_code} -s")
    status_code = int(status_cmd.split("\n")[0].split(" ")[1])

    if is_404(status_code):
        return [url], False
    elif is_3xx(status_code):
        return [get_redirect(TARGET_URL, url), url], True
    else:
        return [url], True

def control_target(TARGET_URL, test_url):
    if not test_url.startswith(TARGET_URL):
        return None
    target_url, status_code = control_status_code(TARGET_URL, test_url)
    if status_code and target_url[0]:
        return target_url
    else:   # 404 Controller
        return None

def manage_target(TARGET_URL, url, target):
    if target and target[0].isalpha():
        if '#' in target:
            target = target[:target.find("#")]

        blacklist = ['tel:', 'mailto:','javascript:']
        if target.startswith(tuple(blacklist)):
            return None
        elif target.startswith(TARGET_URL):
            return target
        elif not target.startswith("http"):
            target = TARGET_URL + '/' + target
            return target
        else:
            return None

    elif target.startswith("."):
        if url.endswith("/"):
            url = url[:-1]
        target = url + "/" + target
        return target

    elif target.startswith("/"):
        if not target.startswith("//"):
            target = TARGET_URL + target
        return target

    elif target.startswith("#"):
        return None

    return None


def manage_image(page, image):
    if not image.startswith("http"):
        image = page + image
    return image


def robotsChecker():
    pass

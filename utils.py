import subprocess

def cmd(cmd):
    return subprocess.check_output(cmd, shell=True).decode()

def control_target(TARGET_URL, test_url):
    if not test_url.startswith(TARGET_URL):
        return None

    target_url, status_code = control_status_code(test_url)
    if status_code :
        return target_url
    else:   # 404 Controller
        return None

def manage_target(TARGET_URL, target):
    if target.startswith("/"):
        target = TARGET_URL + target
    return target

def control_status_code(url):
    status_cmd = cmd("curl -LI " + url + " -w %{http_code} -s")
    status_code = int(status_cmd.split("\n")[0].split(" ")[1])

    if is_404(status_code):
        return [url], False
    elif is_3xx(status_code):
        return [get_redirect(url),url], True
    else:
        return [url], True

def is_404(status_code):
    return True if (status_code == 404 ) else False

def is_3xx(status_code):
    return True if (status_code < 400 and status_code >= 300) else False

def get_redirect(url):
    redirect_url_draft = cmd('curl -Ls -w "%{url_effective}" ' + url)
    return redirect_url_draft.split("\n")[-1]

def robotsChecker():
    pass


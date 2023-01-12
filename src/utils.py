import subprocess
import urllib.parse
from colorama import Fore

DEBUG_MODE = 0

def rreplace(string, string_to_be_changed, string_to_replace):
    # myStr = "mississippi"
    # myStr = rreplace(myStr,"iss","XXX")
    # result: missXXXippi
    return string_to_replace.join(string.rsplit(string_to_be_changed, 1))


def url_encode(TARGET_URL, url):
    path = url[len(TARGET_URL):].replace(" ","%20")
    return TARGET_URL + path
    #return TARGET_URL + urllib.parse.quote(path,safe='/=?%#')

def url_decode(TARGET_URL, url):
    path = url[len(TARGET_URL):].replace("%20", " ")
    return TARGET_URL + path
    #return TARGET_URL + urllib.parse.unquote(path)

def cmd(cmd):
    global DEBUG_MODE
    if(DEBUG_MODE):
        print(Fore.GREEN,"[CMD] ",Fore.WHITE,cmd)

    try:
        # noinspection PyInterpreter
        return subprocess.check_output(cmd, shell=True).decode('utf-8', 'ignore')
    except subprocess.CalledProcessError:
        return None
    except:
        return subprocess.check_output(cmd, shell=True)


def is_404(status_code):
    return True if (status_code == 404) else False


def is_3xx(status_code):
    return True if (status_code < 400 and status_code >= 300) else False


def get_redirect(TARGET_URL, url):
    url = url_encode(TARGET_URL, url)
    #print("[GET_REDIRECT] ",end="")
    redirect_url_draft = cmd("curl -Ls -w %{url_effective} \"" + url + "\"")

    if not redirect_url_draft:
        return None
    redirect_url_draft = redirect_url_draft.split("</html>")[-1].replace("\r", "").replace("\n", "")
    if not redirect_url_draft.startswith(TARGET_URL):
        return None
    return redirect_url_draft


def control_status_code(TARGET_URL, url):
    global DEBUG_MODE
    if (DEBUG_MODE):
        print(Fore.BLUE,"[CONTROL_STATUS_CODE]",Fore.WHITE,TARGET_URL, url, url_encode(TARGET_URL,url),"curl -LI \"" + url + "\" -w %{http_code} -s")

    url = url_encode(TARGET_URL,url)
    #print("[control_status_code]".upper(), end="")
    status_cmd = cmd("curl -LI \"" + url + "\" -w %{http_code} -s")


    if not status_cmd:
        return None
    status_code = int(status_cmd.split("\n")[0].split(" ")[1])


    if is_404(status_code):
        return [url], False
    elif is_3xx(status_code):
        return [get_redirect(TARGET_URL, url), url], True
    else:
        return [url], True


def control_target(TARGET_URL, test_url):
    global DEBUG_MODE
    if (DEBUG_MODE):
        print(Fore.YELLOW, "[CONTROL_TARGET]", Fore.WHITE, TARGET_URL, test_url)

    if not test_url.startswith(TARGET_URL):
        return None
    target_url, status_code = control_status_code(TARGET_URL, test_url)
    if status_code and target_url[0]:
        return target_url
    else:   # 404 Controller
        return None


def manage_target(TARGET_URL, url, target):
    global DEBUG_MODE
    if (DEBUG_MODE):
        print(Fore.CYAN, "[MANAGE_TARGET]", Fore.WHITE, TARGET_URL, url, target)

    rightmost_path = url.split("/")[-1]
    if target and target[0].isalpha():
        if '#' in target:
            target = target[:target.find("#")]

        blacklist = ['tel:', 'mailto:', 'javascript:','data:']
        if target.startswith(tuple(blacklist)):
            return None
        elif "." in rightmost_path and rightmost_path.count(".") == 1 and \
                (rightmost_path != TARGET_URL.replace("https://","") and rightmost_path != TARGET_URL.replace("http://","")):
            #print(Fore.CYAN, "[MANAGE_TARGET_DEBUG2]", Fore.WHITE, url, target, rightmost_path)
            target = rreplace(url, rightmost_path, target)
            #print(Fore.CYAN, "[MANAGE_TARGET_DEBUG3]", Fore.WHITE, target)
            return target
        elif target.startswith(TARGET_URL):
            return target
        elif not target.startswith("http"):
            target = url + '/' + target
            return target
        else:
            return None

    elif target.startswith("."):
        if "./" == target:
            target = ""
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


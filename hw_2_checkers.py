import subprocess

folder_in = "/home/danielfalcony/tst"
folder_out = "/home/danielfalcony/out"
folder_ext = "/home/danielfalcony/folder1"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


def take_data(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    return result.stdout

import stow
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='Datasets'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path=extract_to)


if not stow.exists(stow.join('Datasets', 'captcha_images_v2')):
    download_and_unzip('https://github.com/AakashKumarNain/CaptchaCracker/raw/master/captcha_images_v2.zip', extract_to='Datasets')

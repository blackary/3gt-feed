import json
from urllib.request import urlopen

from xmltodict import parse, unparse


def get_url(url):
    with urlopen(url) as response:
        response_content = response.read()

    return response_content


def handler():
    content = get_url("https://3gt.xyz/feed/")
    return content

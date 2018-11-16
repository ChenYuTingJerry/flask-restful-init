import requests

from utils.entity import Entity

default_timeout = 10


def post(url, data=None, headers=None, params=None, timeout=default_timeout):
    response = requests.post(url, data=data, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok or \
            code == requests.codes.created:
        body = response.json()
        if body:
            return Entity.from_object(body)


def get(url, headers=None, params=None, timeout=default_timeout):
    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        body = response.json()
        if body:
            return Entity.from_object(body)


def update(url, data=None, headers=None, params=None, timeout=default_timeout):
    response = requests.put(url, data=data, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        return {}


def head():
    raise NotImplementedError


def patch():
    raise NotImplementedError


def delete(url, headers=None, params=None, timeout=default_timeout):
    response = requests.delete(url, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        return {}

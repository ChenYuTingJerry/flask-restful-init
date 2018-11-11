import requests
from lib import entity

default_timeout = 10


def post(url, data=None, headers=None, params=None, timeout=default_timeout):
    response = requests.post(url, data=data, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok or \
            code == requests.codes.created:
        body = response.json()
        if body:
            return entity.mapper(body)
    else:
        response.raise_for_status()


def get(url, headers=None, params=None, timeout=default_timeout):
    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        body = response.json()
        if body:
            return entity.mapper(body)
    else:
        response.raise_for_status()


def update(url, data=None, headers=None, params=None, timeout=default_timeout):
    response = requests.put(url, data=data, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        return {}
    else:
        response.raise_for_status()


def head():
    raise NotImplementedError


def patch():
    raise NotImplementedError


def delete(url, headers=None, params=None, timeout=default_timeout):
    response = requests.delete(url, headers=headers, params=params, timeout=timeout)
    code = response.status_code
    if code == requests.codes.ok:
        return {}
    else:
        response.raise_for_status()


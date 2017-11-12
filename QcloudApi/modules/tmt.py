#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import Base

class Tmt(Base):
    requestHost = 'tmt.api.qcloud.com'

def main():
    action = 'TextTranslate'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {}
    service = Tmt(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()

# -*- coding: utf-8 -*-

import os

import leancloud
from wsgiref import simple_server

from app import app
from cloud import engine

APP_ID = 'lVuhkVzMAnyuCuBa5MS30lY7-gzGzoHsz'        #os.environ['LC_APP_ID']
MASTER_KEY = 'UWBunXpUqMTgXTkjiNCTxAQO'    #os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])


#leancloud.init(APP_ID, master_key=MASTER_KEY)
leancloud.init('lVuhkVzMAnyuCuBa5MS30lY7-gzGzoHsz', master_key='UWBunXpUqMTgXTkjiNCTxAQO')

application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    server = simple_server.make_server('192.168.0.12', PORT, application)
    server.serve_forever()

# -*- coding: utf-8 -*-
"""
用于测试环境的全局配置
"""
import os

from conf.default import PROJECT_PATH
from settings import APP_ID


# ===============================================================================
# 数据库设置, 测试环境数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认用mysql
        'NAME': APP_ID,                        # 数据库名 (默认与APP_ID相同)
        'USER': 'examer',                        # 你的数据库user
        'PASSWORD': 'mypwd',                        # 你的数据库password
        'HOST': '192.168.165.187',                   # 开发的时候，使用localhost
        'PORT': '3306',                        # 默认3306
    },
}

# 使用sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # 默认用mysql
#         'NAME': os.path.join(os.path.dirname(PROJECT_PATH), 'db.sqlite3'),
#     },
# }

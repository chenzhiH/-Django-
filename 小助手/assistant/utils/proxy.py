#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2018/11/2
# @Filename       : proxy.py
# @Desc           :

import assistant.settings


def proxy():
    if assistant.settings.USE_PROXY:
        # add your proxy here
        return {}
    else:
        return {}

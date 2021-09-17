# 人生苦短，我用python
# @Time : 2021/9/17 8:47
# @Author : shiChao
# @File : loadIni.py
# @Desc : 读取ini配置文件

import os
import sys
import configparser


class LoadIni:

    def __init__(self, confName):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        sys.path.append(BASE_DIR)
        TEST_CONFIG = os.path.join(BASE_DIR, "config", confName)
        self.conf = configparser.RawConfigParser()
        self.conf.read(TEST_CONFIG, encoding='utf-8')

    # 获取配置
    def getConfig(self, section, option):
        return self.conf.get(section, option)

# 人生苦短，我用python
# @Time : 2021/9/15 9:20
# @Author : shiChao
# @File : log.py
# @Desc : 日志操作
import logging
import os
from apiunittest.lib.loadIni import LoadIni


class LoggerHandler(logging.Logger):
    # 继承Logger类
    def __init__(self, name='root', level='DEBUG', format=None):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        # 生成日志文件
        try:
            if not os.path.exists(log_path):
                os.makedirs(log_path)
        except Exception as e:
            raise e

        file = log_path + 'log.txt'

        # 如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        # # 输出日志到控制台
        # stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(level)
        # stream_handler.setFormatter(fmt)
        # self.addHandler(stream_handler)


name = LoadIni('config.ini').getConfig('log', 'name')
level = LoadIni('config.ini').getConfig('log', 'level')
formats = LoadIni('config.ini').getConfig('log', 'formats')

logger = LoggerHandler(name=name, level=level, format=formats)

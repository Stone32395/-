"""
    读取yaml数据
"""
import yaml


def loadYaml(filename):
    files = open(filename, 'r', encoding='utf-8')

    data = yaml.load(files, Loader=yaml.FullLoader)

    return data

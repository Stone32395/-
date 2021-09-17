"""
    实现关键字驱动的封装
"""
import json
import jsonpath
import requests


class Keyword:

    # post请求
    def keyPost(self, url,  params=None, **kwargs):
        return requests.post(url=url, params=params, **kwargs)

    # get请求
    def keyGet(self, url, params=None, **kwargs):
        return requests.post(url=url, params=params, **kwargs)

    # 获取JSON内容
    def getText(self, res, key):
        try:
            text = json.loads(res)
            value = jsonpath.jsonpath(text, '$..{0}'.format(key))
            if len(value) == 1:
                return value[0]
            else:
                return value
        except Exception as e:
            return False

    # 判断
    def handle(self, res):

        # 接口请求错误
        if res.status_code != 200:
            return False

        # 返回状态码不等于0
        if res.json()['code']:
            return False

        return True

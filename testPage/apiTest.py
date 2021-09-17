"""
    测试用例
"""
import unittest
import jsonpath
import requests
from apiunittest.lib.loadIni import LoadIni
from apiunittest.keyword.keyword import Keyword
from apiunittest.lib.log import logger
from ddt import ddt, file_data


@ddt
class ApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.keyword = Keyword()
        cls.cookie = None
        cls.confData = LoadIni('config.ini')
        logger.info('----------用例开始执行----------')

    # 登录
    @file_data('../data/data.yaml')
    def test_1_login(self, username, password):
        s = requests.Session()
        loginUrl = self.confData.getConfig('urlConfig', 'login')

        data = {
            'uname': username,
            'upass': password,
            'encode': 1
        }
        res = s.post(url=loginUrl, data=data)
        logger.info(res.text)
        cookie = dict(res.cookies)
        sess = jsonpath.jsonpath(cookie, '$..{0}'.format('PHPSESSION'))
        phpSession = 'PHP_SESSION=' + sess[0]
        ApiTest.cookie = phpSession
        logger.info('用例执行成功')


if __name__ == '__main__':
    unittest.main()

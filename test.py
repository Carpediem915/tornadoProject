#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/1/3 15:16 
# @Author : hcm 
# @File : test.py
# @desc : tornado框架练习

import tornado.web
import tornado.ioloop


# 自定义接口处理类
class IndexHandler(tornado.web.RequestHandler):
    """这是IndexHandler"""

    # 添加一个处理get请求的方法
    def get(self):
        username = self.get_argument('username', '小明')
        print('get方式获取参数username：' + username)
        # 向响应中，添加数据
        self.write('哈哈哈哈哈哈哈')

if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
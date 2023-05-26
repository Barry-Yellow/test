import json
from flask import Flask
from TeamProject.main import app
from TeamProject.initial import initial
import pytest
import coverage


"""
几大功能：
    1.账号密码登录、邮件验证码登录、修改账户信息
    2.根据对应课程表发评论、收评论
    3.根据对应的课程返回课表
    4.根据最新一封邮件总结关键词
    5.日程安排便签功能
    6.根据关键词搜索全校课表

"""

initial(app) # 将student 与 comments清空
"""
几大功能：
    1.账号密码登录、邮件验证码登录、修改账户信息
    2.根据对应课程表发评论、收评论
    3.根据对应的课程返回课表
    4.根据最新一封邮件总结关键词
    5.日程安排便签功能
    6.根据关键词搜索全校课表

"""
with app.test_client() as client:
    response = client.post('/register', data={'id': '12011129', 'username': 'barry', 'name': 'hyh', 'password': '1234567', 'gender': 'Male', 'major': 'Computer Science', 'email': '2292683883@qq.com', 'email_password': 'hyhHYH20020713'})


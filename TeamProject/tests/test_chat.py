import json
from flask import Flask
from TeamProject.main import app
from TeamProject.initial import initial
from TeamProject.module.verifyUser import verify_code
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



@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client





def test_hello_world(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


def test_get_data(client):
    response = client.get('/get_data')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'data' in json_data
    # Add more assertions to validate the structure and content of the JSON response


def test_select_class(client):
    response = client.get('/select_class?courses[]=软件工程&courses[]=计算机操作系统')
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'data' in json_data
    # Add more assertions to validate the structure and content of the JSON response


def test_post_data(client):
    response = client.post('/post_data', data={'name': 'John', 'age': '30'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'name' in json_data
    assert json_data['name'] == 'John'
    assert 'age' in json_data
    assert json_data['age'] == '30'


def test_get_course_list(client):
    response = client.get('/getCourseList?id=12011129&college=&course=计算机&teacher=')
    assert response.status_code == 200
    # Add assertions for the response data



def test_register(client):
    response = client.post('/register', data={'id': '123', 'username': 'testuser', 'name': 'Test User', 'password': 'pass123', 'gender': 'Male', 'major': 'Computer Science', 'email': 'test@example.com', 'email_password': 'pass123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'succeed'


def test_register_id_exist(client):
    response = client.post('/register', data={'id': '123', 'username': 'testuser', 'name': 'Test User', 'password': 'pass123', 'gender': 'Male', 'major': 'Computer Science', 'email': 'test@example.com', 'email_password': 'pass123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'id exists or name exist'


def test_register_invalid_info(client):
    response = client.post('/register', data={'id': '123', 'name': 'Test User', 'password': 'pass123', 'gender': 'Male', 'major': 'Computer Science', 'email': 'test@example.com', 'email_password': 'pass123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'invalid information'




def test_login(client):
    response = client.post('/login', data={'id': '123', 'password': 'pass123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'succeed'
    assert 'id' in json_data
    assert 'password' in json_data
    assert 'username' in json_data
    assert 'name' in json_data
    assert 'major' in json_data
    assert 'gender' in json_data
    assert 'email' in json_data
    assert 'email_password' in json_data


def test_login_no_user(client):
    response = client.post('/login', data={'id': '1234', 'password': 'pass123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'no such user'


def test_login_wrong_password(client):
    response = client.post('/login', data={'id': '123', 'password': 'pass125'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'wrong password'



def test_login_by_email(client):
    response = client.post('/register_by_email', data={'email_address': '2292683883@qq.com'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'send succeed'


def test_login_by_email_wrong_address(client):
    response = client.post('/register_by_email', data={'email_address': '22926838'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'email address don\'t exist'


def test_verify_by_email(client):
    response = client.post('/login_by_verify_code', data={'email_address': '2292683883@qq.com', 'verify_code': '123456'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'wrong code'



def test_verify_by_email_succeed(client):

    response = client.post('/login_by_verify_code', data={'email_address': '2292683883@qq.com', 'verify_code': verify_code['2292683883@qq.com']})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'succeed'





def test_verify_by_email_wrong_address(client):
    response = client.post('/login_by_verify_code', data={'email_address': '2292683883@cq.com', 'verify_code': '123456'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'wrong email address'






def test_modify_st(client):
    response = client.post('/modify', data={
    'id': '123',
    'username': 'johnny',
    'name': 'John Doe',
    'password': 'pass123',
    'gender': 'male',
    'major': 'Computer Science',
    'email': 'john.doe@example.com',
    'email_password': 'emailpassword123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'succeed'
    assert 'id' in json_data
    assert 'name' in json_data
    assert json_data['name'] == 'John Doe'



def test_modify_st_wrong(client):
    response = client.post('/modify', data={
    'id': '123',
    'username': 'johnny',
    'name': 'John Doe',
    'password': 'pass12',
    'gender': 'male',
    'major': 'Computer Science',
    'email': 'john.doe@example.com',
    'email_password': 'emailpassword123'})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'state' in json_data
    assert json_data['state'] == 'wrong password'








import json
from flask import Flask
from TeamProject.main import app
from TeamProject.initial import initial
import pytest
import coverage

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

"""
    1.正常post和get            P
    2.post course id不合法
    3.post参数不全


"""

def test_get_comments():
    with app.test_client() as client:
        response = client.get('/getCourseComments?course_id=ECA1539E4EB011FDE053CB0412AC12F6')
        data = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert isinstance(data, list)

        # Add more assertions based on the expected response


def test_post_comment():
    with app.test_client() as client:
        response = client.post('/postComment', data={
            'student_id': '12011129',
            'course_id': 'ECA1539E4EB011FDE053CB0412AC12F6',
            'content': 'Test comment',
            'reply_to': '789'
        })
        data = json.loads(response.data.decode('utf-8'))

        assert response.status_code == 200
        assert isinstance(data, list)

        # Add more assertions based on the expected response



def test_post_comment_courseid(client):
    response = client.post('/postComment', data={'student_id': '123', 'course_id': '456',})
    data = json.loads(response.data).get('response')
    assert data == 'invalid course_id'
    assert response.status_code == 200
    # Add assertions for the response data


def test_post_comment_studentid(client):
    response = client.post('/postComment', data={
            'course_id': 'ECA1539E4EB011FDE053CB0412AC12F6',
            'content': 'Test comment',
            'reply_to': '789'
        })
    data = json.loads(response.data).get('response')
    assert data == 'invalid args'
    assert response.status_code == 200
    # Add assertions for the response data


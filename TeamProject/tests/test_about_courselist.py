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


def test_get_course_list(client):
    response = client.get('/getCourseList?id=123&college=计算机&course=计算机&teacher=郑锋')
    assert response.status_code == 200
    # Add assertions for the response data




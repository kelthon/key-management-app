from flask import app
import pytest

aplicacao = app.test_client()


def login(client, username):
    return client.post('/index/login', data=dict(
        usuario=username,
        senha='123456789'
    ), follow_redirects=True)

def logout(client):
    return client.get('/usuario/logout', follow_redirects=True)

@pytest.fixture
def client():
    return(aplicacao)

@pytest.fixture
def preparacao():
    app.config['WTF_CSRF_ENABLED'] = False
    yield
    app.config['WTF_CSRF_ENABLED'] = True

def test01(client):
    rv = client.get('/',follow_redirects=True)
    assert 200 == rv.status_code

def test02(client):
    rv = client.get('/index/view/',follow_redirects=True)
    assert rv.status_code==200



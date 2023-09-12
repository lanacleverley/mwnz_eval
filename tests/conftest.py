import pytest

import flaskr 

@pytest.fixture
def app():
    app = flaskr.app
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

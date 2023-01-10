import typing as t
import pytest

from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture()
def app() -> t.Generator[Flask, None, None]:
    from app import create_app

    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app: Flask) -> t.Generator[FlaskClient, None, None]:
    with app.test_client() as client:
        yield client

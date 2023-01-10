from http import HTTPStatus
from flask import url_for
from flask.testing import FlaskClient


def test_get_index_success(client: FlaskClient) -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.mimetype == "text/html"

    body = response.data.decode("utf-8")
    assert "Predictimmo" in body
    assert '<form method="post"' in body
    assert url_for("home.index") in body
    assert "Estimate" in body
    assert "Estimated value" not in body


def test_post_index_success(client: FlaskClient) -> None:
    params = dict(
        housing_type="appartment",
        surface="50",
        rooms="3",
    )

    response = client.post("/", data=params)
    assert response.status_code == HTTPStatus.OK
    assert response.mimetype == "text/html"

    body = response.data.decode("utf-8")
    assert "Predictimmo" in body
    assert '<form method="post"' in body
    assert url_for("home.index") in body
    assert "Estimate" in body
    assert "Estimated value" in body

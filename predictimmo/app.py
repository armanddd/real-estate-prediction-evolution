import typing as t
import joblib
import pandas as pd

from pathlib import Path
from flask import Blueprint, Flask, current_app, render_template, request


def load_model() -> t.Any:
    filepath = Path(".") / "model.joblib"
    return joblib.load(filepath)


def predict_model(model: t.Any, housing_type: str, surface: int, rooms: int) -> int:
    housing_type_map = {
        "house": "Maison",
        "appartment": "Appartement",
    }
    params = pd.DataFrame({
        "type_local": [housing_type_map[housing_type]],
        "surface_reelle_bati": [surface],
        "nombre_pieces_principales": [rooms],
    })
    predictions =  model.predict(params)
    print(predictions)
    return int(predictions[0][0])


home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def index() -> str:
    context = {}

    if request.method == "POST":
        print(request.form.to_dict())
        housing_type = request.form.get("housing_type")
        surface = request.form.get("surface")
        rooms = request.form.get("rooms")
        context["estimated_value"] = predict_model(
            current_app.config["model"],
            housing_type,
            surface,
            rooms,
        )
        context.update(**request.form.to_dict())

    return render_template("index.html", **context)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["model"] = load_model()
    app.register_blueprint(home, url_prefix="")
    return app

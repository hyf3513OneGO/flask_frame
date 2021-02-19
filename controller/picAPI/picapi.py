from flask import Blueprint
from flask import redirect
import random
picapi=Blueprint("picapi",__name__)


@picapi.route("/random")
def radompic():

    return redirect()

from flask import redirect, render_template, session, url_for, request, abort, g as flask_g
from .import controller
from .import app


@app.route("/")
def index():
  inventory = controller.get_from_inventory()
  return render_template("index.html", store=inventory)


@app.route("/item")
@app.route("/item/<item_id>")
def view_item(item_id=None):
  flask_g.item = controller.get_from_inventory(item=item_id)
  return render_template('item.html')


@app.route("/cart")
def cart():
  return abort(501)

@app.errorhandler(400)
def bad_request(static):
  return "Bad Request."

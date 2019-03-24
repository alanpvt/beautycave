# pylint: disable=no-member, unresolved-import
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(80), unique=False, nullable=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  quantity = db.Column(db.Integer(), nullable=False)
  specs = db.Column(db.Text(), nullable=True)
  images = db.Column(db.String(80), unique=True, nullable=False)
  is_on_sale = db.Column(db.Boolean())

  def __repr__(self):
    return '<Item %r>' % self.name
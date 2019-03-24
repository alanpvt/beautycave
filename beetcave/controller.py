from dictalchemy import make_class_dictable
import operator
from .models import Inventory


def get_from_inventory(item: int = 0):
  make_class_dictable(Inventory)

  if int(item) > 0:
    return Inventory.query.get(item).asdict()

  return list(map(operator.methodcaller('asdict'), Inventory.query.all()))


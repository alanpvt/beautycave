from wtforms_alchemy import ModelForm
from .models import Inventory


class InventoryForm(ModelForm):
  class Meta:
    model = Inventory


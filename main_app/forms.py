from django.forms import ModelForm
from .models import Building

class BuildingForm(ModelForm):
  class Meta:
    model = Building
    fields = '__all__'

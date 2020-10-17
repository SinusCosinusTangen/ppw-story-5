from django.forms import ModelForm
from .models import Schedule

class tambahForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
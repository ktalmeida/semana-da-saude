from django.forms import ModelForm
from .models import Patient

class PatientForm(ModelForm):

    class Meta:
        model = Patient
        exclude = ('created_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for key in self.fields:
            # print(self.fields[key].widget.help_text)



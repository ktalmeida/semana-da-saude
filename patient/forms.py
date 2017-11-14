from django.forms import ModelForm
from .models import Patient
from django.core.validators import EMPTY_VALUES


class PatientForm(ModelForm):

    class Meta:
        model = Patient
        exclude = ('created_at',)

    def clean(self):
        has_referral = self.cleaned_data.get('has_referral', False)
        print(has_referral)
        if has_referral:
            print(self.cleaned_data)
            referral_character = self.cleaned_data.get(
                'referral_character', None)
            other_referral_place = self.cleaned_data.get(
                'other_referral_place', None)

            if referral_character in EMPTY_VALUES:
                self._errors['referral_character'] = self.error_class([
                    'Caráter do encaminhamento obrigatório'])

            if other_referral_place in EMPTY_VALUES:
                self._errors['other_referral_place'] = self.error_class([
                    'Local do encaminhamento obrigatório'])
        print(self._errors)
        return self.cleaned_data




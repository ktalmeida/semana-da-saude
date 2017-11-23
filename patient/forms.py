from django.forms import ModelForm, DateField
from .models import Patient
from django.core.validators import EMPTY_VALUES


class PatientForm(ModelForm):
    birthdate = DateField(input_formats=('%d/%m/%Y',))
    class Meta:
        model = Patient
        exclude = ('created_at',)

    def clean(self):
        has_referral = self.cleaned_data.get('has_referral', False)
        if has_referral:
            referral_character = self.cleaned_data.get(
                'referral_character', None)
            if referral_character in EMPTY_VALUES:
                self._errors['referral_character'] = self.error_class([
                    'Caráter do encaminhamento obrigatório'])
            referral_place = self.cleaned_data.get('referral_place', None)
            other_referral_place = self.cleaned_data.get(
                'other_referral_place', None)
            if referral_place in EMPTY_VALUES:
                self._errors['referral_place'] = self.error_class([
                        'Local do encaminhamento obrigatório'])
            elif int(referral_place) == 2 and \
                    other_referral_place in EMPTY_VALUES:
                self._errors['other_referral_place'] = self.error_class([
                    'Local do encaminhamento obrigatório'])
        print(self.cleaned_data.get('birthdate'))
        return self.cleaned_data




from faker import Faker
from .models import Patient
import random


def gen_fake_patients(count=500):
    factory = Faker('pt_BR')
    for i in range(500):
        patient = Patient()
        patient.name = factory.name()
        patient.mother_name = factory.name()
        patient.address = factory.address()
        patient.phone = factory.phone_number()
        patient.birthdate = factory.date_time()
        patient.exame_number = factory.word()
        patient.notes = factory.text()
        patient.prostate_history = bool(random.getrandbits(1))
        patient.trouble_urinating = bool(random.getrandbits(1))
        patient.suspicious_nodule = bool(random.getrandbits(1))
        patient.has_referral = bool(random.getrandbits(1))
        if patient.has_referral:
            patient.referral_character = random.randint(1,2)
            patient.referral_place = random.randint(0,2)
            if patient.referral_place == 2:
                patient.other_referral_place = factory.address()
        patient.save()

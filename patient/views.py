from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Patient, CHARACTER_CHOICES, REFERAL_PLACES
from .forms import PatientForm
from datetime import datetime


def get_registry_number():
    return Patient.objects.count() + 1


def index(request):
    patient_list = Patient.objects.all()
    paginator = Paginator(patient_list, 25)
    page = int(request.GET.get('page', 1))
    print(paginator.num_pages)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    page_range = range(1, patients.paginator.num_pages)
    return render(request, 'patient/list.html', {
        'patients': patients, 'page_range': page_range})


def create(request):
    title = 'Novo paciente'
    if request.method == 'GET':
        return render(
            request, 'patient/view.html',
            {
                'title': title,
                'form': PatientForm(), 'number': get_registry_number(),
            })
    else:
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('patient:print', patient_id=patient.id)
        else:
            return render(
            request, 'patient/view.html',
            { 'title': title, 'form': form })


def edit(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    form = PatientForm(instance=patient)
    if request.method == 'GET':
        return render(
            request, 'patient/view.html',
            {
                'title': 'Paciente',
                'patient': patient, 'form': form, 'number': patient.id
            })
    else:
        form = PatientForm(request.POST, instance=patient, )
        if form.is_valid():
            patient.save()
            return redirect('patient:print', patient_id=patient.id)
        else:
            return render(
            request, 'patient/view.html',
            { 'title': 'Paciente', 'patient': patient, 'form': form})


def print_patient(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(
            request, 'patient/print.html',
            {
                'title': 'Paciente',
                'patient': patient,
                'time': datetime.now().strftime('%d/%m/%Y'),
                'CHARACTER_CHOICES': CHARACTER_CHOICES,
                'REFERAL_PLACES': REFERAL_PLACES,
                'patient_age': patient.get_age()
            })

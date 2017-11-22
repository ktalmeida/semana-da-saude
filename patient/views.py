from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Patient, CHARACTER_CHOICES, REFERAL_PLACES
from .forms import PatientForm
from datetime import datetime


def get_registry_number():
    return Patient.objects.count() + 1

def create_flash(color, message):
    return {
        'color': color,
        'message': message
    }

def get_error_msg(form):
    return 'Formulário inválido'


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
    response_args = {
        'title': title,
        'form': PatientForm(),
        'number': get_registry_number(),
    }
    if request.method == 'POST':
        form = PatientForm(request.POST)
        response_args['form'] = form
        if form.is_valid():
            patient = form.save()
            response_args.update({
                'flash': create_flash('green', 'Paciente criado com sucesso!')
            })
        else:
            response_args.update({
                'flash': create_flash('red', get_error_msg(form))
            })

    return render(
        request, 'patient/view.html', response_args)


def edit(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    form = PatientForm(instance=patient)
    response_args = {
        'title': 'Editar Paciente',
        'number': patient.id,
        'patient': patient,
        'form': form
    }
    if request.method == 'GET':
        return render(
            request, 'patient/view.html', response_args)
    else:
        form = PatientForm(request.POST, instance=patient)
        response_args['form'] = form
        if form.is_valid():
            patient.save()
            response_args.update({
                'flash': create_flash('green', 'Paciente editado com sucesso!')
            })
        else:
            response_args.update({
                'flash': create_flash('red', get_error_msg(form))
            })
        return render(
            request, 'patient/view.html', response_args)


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

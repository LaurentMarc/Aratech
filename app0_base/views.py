from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'app0_base/index.html')


def team(request):
    return render(request, 'app0_base/team.html')


def expertise(request):
    return render(request, 'app0_base/expertise.html')


def ai(request):
    return render(request, 'app0_base/ai.html')


def contact(request):
    return render(request, 'app0_base/contact.html')


def legalnotice(request):
    return render(request, 'app0_base/legalnotice.html')




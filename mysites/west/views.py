#coding=utf-8

from django.shortcuts import render
#from django.http import HttpResponse
from django.core.context_processors import csrf

from west.models import Character
from django import forms
# Create your views here.
#def staff(request):
#    staff_list = Character.objects.all()
#    staff_str = map(str, staff_list)
#    context = {'label': ' '.join(staff_str)}
#    return render(request, 'templay.html', context)
class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)


def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs': staff_list})


def templay(request):
    context          = {}
    context['label'] = 'FUCK GFW!'
    return render(request, 'templay.html', context)

def form(request):
    return render(request, 'form.html')


def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted = request.POST['name']
            new_record = Character(name = submitted)
            new_record.save()
    form = CharacterForm()
    ctx = {}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form'] = form
    return render(request, "investigate.html", ctx)

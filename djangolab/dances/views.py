from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from .models import Dance, Action, Dancer,Place
from .forms import DanceForm, DancerForm
from django.template.context_processors import csrf
# Create your views here.
def dance_home(request):
    return HttpResponse ('<h1> Main page </h1>')

def dancer_detail(request, id):
    instance=get_object_or_404(Dancer,id=id)
    context={
        'title':'Detail',
        'instance':instance,
    }
    return render(request,'dances/dancer_detail.html',context)
def dancer_list(request):
    queryset=Dancer.objects.all()
    context={
        'queryset':queryset,
        'title':'Dancers list'
    }
    return render(request,'dances/index.html',context)


def dancer_create(request):
    form=DancerForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        'form':form,
    }
    return render(request,'dances/dancer_create.html',context)

def dancer_update(request, id=None):
    instance=get_object_or_404(Dancer,id=id)
    form=DancerForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        'title':'Update',
        'instance':instance,
        'form':form,
    }
    return render (request,'dances/dancer_create.html',context)

def dancer_delete(request):
    return HttpResponse('<h1>Delete</h1')

def dance_create(request):
    form=DanceForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/dances')
    context={
        'form':form,
    }
    return render(request,'dances/dance_create.html',context)
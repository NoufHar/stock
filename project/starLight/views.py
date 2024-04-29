from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from .models import Event
from django.forms import ModelForm
# Create your views here.

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_delete.html', {'event': event})

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location']

def event_update(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_detail', event_id=event.id)
    return render(request, 'event_update.html', {'form': form, 'event': event})
from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import ApplicantForm

# Create your views here.
def index(request):
    events_obj=Event.objects.all()
    print(events_obj)
    return render(request,'index.html',{'events':events_obj})

def details(request,pk):
    event_obj=Event.objects.get(pk=pk)
    form=ApplicantForm()
    if request.method=='POST':
        form=ApplicantForm(request.POST)
        if form.is_valid():
            applicant=form.save(commit=False)
            applicant.event=event_obj
            applicant.save()
    return render(request,'details.html',{'event':event_obj,'form':form})

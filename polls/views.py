from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import NameForm
import urllib.request

def index(request):
    # return HttpResponse("Hello")
    return render(request, 'polls/index.html')


def results(request,pageNumber):
    if request.method=='POST':
        form = NameForm(request.POST)
        # print(form.phone_number)
        if form.is_valid():
            token =  "514757767373664e566552486956746a686a554b696c736158666e6e56656f4f526d6c4b536d71756c704256"
            phone = form.cleaned_data['phone_number']
            message = form.cleaned_data['paragraph_text']
            res = urllib.request.urlopen("https://api.tropo.com/1.0/sessions?action=create&"
            "token="+token+"&numberToDial="+phone+"&customerName=temp&msg="+message).read()
            return render(request,'polls/Thanks.html',{'phonenumber':phone})
        else:
            form = NameForm()
            return render(request,'polls/Try Again.html')
    # return render(request, 'index.html', {'form': form})



# response = "You're looking at page number %s."
     # return HttpResponse(response % pageNumber)
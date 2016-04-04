from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import NameForm

def index(request):
    # return HttpResponse("Hello")
    return render(request, 'polls/index.html')


def results(request,pageNumber):
    if request.method=='POST':
        form = NameForm(request.POST)
        # print(form.phone_number)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            message = form.cleaned_data['paragraph_text']
            return HttpResponse(phone+message)
        else:
            form = NameForm()
            return HttpResponse("try again")
    # return render(request, 'index.html', {'form': form})



# response = "You're looking at page number %s."
     # return HttpResponse(response % pageNumber)
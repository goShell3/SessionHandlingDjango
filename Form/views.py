from django.shortcuts import render, redirect
from .forms import PersonForm 
from django.contrib import messages

def PersonView(request):
    if request.method == 'POST':
        forms = PersonForm(request.POST) 
        if forms.is_valid():
            forms.save()

            messages.success(request, 'Your message has been successfully submitted!')

            return redirect('form_view')
    else:
        forms = PersonForm() 

    return render(request, 'base.html', {'forms': forms})

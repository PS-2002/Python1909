from django.shortcuts import render
from datetime import datetime
from .forms import UserForm
from .models import UserModel
# Create your views here.
def index(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'myapp/index.html', {'current_time': current_time})

def contact(request):
    if request.method == 'POST':
        form = UserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/thank_you.html', {'name': form.cleaned_data['name']})
    else:
        form = UserForm()
    return render(request, 'myapp/contact.html', {'form': form})

def display_contacts(request):
    contacts = UserModel.objects.all()
    return render(request, 'myapp/display_contacts.html', {"contacts": contacts})
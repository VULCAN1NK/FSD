from django.shortcuts import render, redirect
from .models import UserEntry
from .forms import UserEntryForm

def submit_form(request):
    if request.method == 'POST':
        form = UserEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank-you page after submission
    else:
        form = UserEntryForm()
    return render(request, 'myapp/form.html', {'form': form})

def thank_you(request):
    return render(request, 'myapp/thank_you.html')

def view_entries(request):
    entries = UserEntry.objects.all()
    return render(request, 'myapp/entries.html', {'entries': entries})
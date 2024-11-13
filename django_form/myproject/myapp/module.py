from .forms.py import UserEntryForm

def process_form_data(data):
    form = MyForm(data)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        return cleaned_data
    return None

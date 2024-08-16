import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import UserInputForm

def fetch_data(request):
    data = None
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            url = f'https://ordspub.epa.gov/ords/pesticides/cswu/ProductSearch/searchWithIngName/v1/{query}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
    else:
        form = UserInputForm()

    return render(request, 'myapp/fetch_data.html', {'form': form, 'data': data})
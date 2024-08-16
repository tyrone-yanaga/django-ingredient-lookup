import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from . import UserInputForm

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

    #filtering/sorting of data
    sort_by = request.GET.get('sort', 'id')
    order = request.GET.get('order', 'asc')
    data = sorted(data, key=lambda x: x.get(sort_by), reverse=order == 'desc')

    paginated_data = Paginator(data, 20)
    page_number = request.GET.get('page')
    page_obj = paginated_data.get_page(page_number)

    context = {
        'form': form,
        'data': data,
        'sort': sort_by,
        'order': order,
    }

    if request.htmx:
        return render(request, 'myapp/partials/data_table.html', context)
    return render(request, 'myapp/fetch_data.html', context)
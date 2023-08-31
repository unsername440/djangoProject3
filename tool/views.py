from django.shortcuts import render
from .forms import MyForm

from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})



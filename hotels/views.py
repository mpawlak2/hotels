from django.shortcuts import render
from .forms import SearchForm

# Create your views here.

def show_form(request):
	form = SearchForm()
	return render(request, 'hotels/test_form.html', {'form': form})
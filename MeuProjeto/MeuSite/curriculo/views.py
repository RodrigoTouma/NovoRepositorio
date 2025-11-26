from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def curriculo_spiff(request):
    return render(request, 'curriculo/index.html')

@login_required
def curriculo_mariobros(request):
    return render(request, 'curriculo/meu-curriculo.html')
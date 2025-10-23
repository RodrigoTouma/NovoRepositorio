from django.urls import path
from . import views

app_name = 'curriculo'

urlpatterns = [
    # rota para a página do Spiff
    # pode ser acessada em /curriculo/spiff/
    path('spiff/', views.curriculo_spiff, name='curriculo_spiff'),

    # rota para a página do MarioBros
    # pode ser acessada em /curriculo/mariobros/
    path('mariobros/', views.curriculo_mariobros, name='curriculo_mariobros'),
]
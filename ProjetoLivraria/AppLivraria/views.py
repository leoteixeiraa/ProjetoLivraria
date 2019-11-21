from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppLivraria.models import Livro
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView

class Index(TemplateView):
    template_name = "index.html"
    
class CriaLivro(CreateView):
    template_name = "cadastra.html"
    model = Livro()
    fields = '__all__'
    success_url = reverse_lazy("lista_livros")
    
class ListaLivro(ListView):
    template_name = "lista.html"
    model = Livro
    context_object_name = 'livros'

class AtualizaLivro(UpdateView):
    template_name = "atualiza.html"
    model = Livro()
    fields = '__all__'
    context_object_name = 'livro'   
    success_url = reverse_lazy("lista_livros")
    
class DeletaLivro(DeleteView):
    template_name = "exclui.html"
    model = Livro()
    context_object_name = 'livro'
    success_url = reverse_lazy("lista_livros")
    
    
    
    
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Articoli,Giornalisti
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request): 
    return render(request, "home.html")

class ArticoliView(ListView):
    model = Articoli #modello dei dati da utilizzare 
    template_name = "news/articoli.html"  #pagina per mostrare i dati
    
    #recupera di dati da passare alla pagina per il render
    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context["posts"] = BlogPostModel.objects.all()
       # return context

#class PostDetailView(DetailView):
#    model = BlogPostModel #modello dei dati da utilizzare 
#    template_name = "blog/post_detail.html" #pagina per mostrare i dati

class GiornalistiView(ListView):
    model = Giornalisti #modello dei dati da utilizzare 
    template_name = "news/giornalisti.html"

def ArticoliGiornalistiView(request, pk):
    obj = get_object_or_404(Articoli, id=pk)
    
    context = {'post': post,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form
                }
    return render(request, 'blog/post_detail.html', context)





from django.db import models
from django.views.generic import DeleteView, ListView
from django.views.generic.detail import DetailView

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
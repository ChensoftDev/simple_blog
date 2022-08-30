from django.shortcuts import render

# Create your views here.
from blog.models import Category


def index(request):
    categories = Category.objects.all()
    context = {"title": "my_homepage", "content": "my home page content",
               "categories": categories}
    return render(request, 'index.html', context)

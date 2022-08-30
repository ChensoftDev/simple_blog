from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from blog.models import Category


def index(request):
    categories = Category.objects.all()
    context = {"title": "my_homepage", "content": "my home page content",
               "categories": categories}
    return render(request, 'index.html', context)


def categoryDetail(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {"category": category}
    return render(request, 'category.html', context)


def createCategory(request):
    category_name = request.POST.get("category_name")
    category = Category(name=category_name)
    category.save()
    return HttpResponseRedirect(reverse('home'))


def updateCategory(request):
    category_id = request.POST.get("category_id")
    category_name = request.POST.get("category_name")
    category = Category.objects.get(id=category_id)
    category.name = category_name
    category.save()
    return HttpResponseRedirect(reverse('category', args={str(category_id)}))

def deleteCategory(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('home'))

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import SearchForm

from django import forms
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q, Search
from elasticsearch_dsl.query import MultiMatch, MatchAll

from item.documents import ItemDocument
from item.serializers import ItemSerializer
from category.documents import CategoryDocument


def login_view(request):
    return render(request, 'login.html', {})

@login_required
def home_view(request):
    return render(request, 'home.html', {})

def index_view(request):
    return render(request, 'index.html', {})


def item_search(query: str):
    result = []
    q = Q("multi_match", query=query, fields=['title_item', 'description_item', 'categories'])
    qs = ItemDocument.search().query(q)
    return qs

def search_item_form(request):
    items=[]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            items = item_search(query)
    else:
        form = SearchForm()
    return render(request, 'searchItemForm.html', {'form': form, 'items': items})

def cat_search(query: str):
    q = Q("multi_match", query=query, fields=['name_category', 'description_category'])
    s = CategoryDocument.search().query(q).execute()
    return s

def search_cat_form(request):
    hits=[]
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            hits = cat_search(query)       
    else:
        form = SearchForm()
    return render(request, 'searchCatForm.html', {'form': form, 'hits': hits})
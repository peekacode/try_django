
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostModelForm

# Create your views here.

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)

#CREATE RETREIVE UPDATE DELETE

def blog_post_create_view(request):

    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BlogPostModelForm()

    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'update.html'
    context = {"object": obj, "form": None}
    return render(request, template_name, context)

def blog_post_delete_view(request,slug):    
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'delete.html'
    context = {"object": obj, "form": None}
    return render(request, template_name, context)

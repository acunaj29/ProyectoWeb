from django.shortcuts import render
from blog.models import Post,categoria


def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria=categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categoria=categoria)
    #40

    return render(request, "blog/categoria.html", {'categoria':categoria,"posts":posts})
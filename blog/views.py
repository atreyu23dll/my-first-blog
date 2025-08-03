from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def detalles_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalles_post.html', {'post': post})

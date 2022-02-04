from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # QuerySet name
    return render(request, 'blog/post_list.html', {'posts': posts}) # takes user requests as 1st parameter, template as 2nd, template propertires as 3rd

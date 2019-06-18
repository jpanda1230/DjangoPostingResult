from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .models import Comment
from .forms import CommentForm


# Create your views here.
'''
def post_list(request):
	return render(request, 'blog/post_list.html')

'''


post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)
comment_new = CreateView.as_view(model=Comment, form_class =CommentForm)
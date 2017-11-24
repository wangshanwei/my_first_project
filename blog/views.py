from django.shortcuts import render,get_object_or_404 
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			post = form.save()
			post.save()

	else:
		form = EmailPostForm()
	return render(request, 'blog/index.html', {'form':form,})

def detail(request):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/detail.html', context={'post': post})

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id)
	sent = False
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_url(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'wangwei6978@126.com', [cd['wangwei6978@126.com']])
			sent = True

	else:
		form = EmailPostForm()
	return render(request, 'blog/index.html', {'post':post, 'form':form, 'sent': sent})
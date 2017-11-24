
from django.forms import ModelForm
from blog.models import Post

class EmailPostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'     #field = ('title','content')

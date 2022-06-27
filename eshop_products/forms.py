from django.forms import ModelForm
from .models import ProductComment


class AddCommentForm(ModelForm):
	class Meta:
		model = ProductComment
		fields = ('title', 'text')
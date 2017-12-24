from django import  forms
from .models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name','email','text']
		widgets = {
			# 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
			# 例如 user_name 渲染后的html组件如下：
			# <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

			'name': forms.TextInput(attrs={
				'class': '',
				'placeholder': "请输入昵称",
				'type': "text",

			}),
			'email': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': "请输入邮箱",
				'maxlength': "58",
				'autocomplete': "off",
				'type': "email",

			}),
			'text': forms.Textarea(attrs={
				'placeholder': '我来评两句',
				'rows':"5",

			}),
		}
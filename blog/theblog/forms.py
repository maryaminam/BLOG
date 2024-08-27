from django import forms
from .models import Post,Category, Comment

#choices =[('coding','coding'),('health','health'),('fun','fun'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title','title_tag','author','category','body', 'snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'maryam','type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title','title_tag','body','snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Body'}),
        }
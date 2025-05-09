from django import forms
from .models import BlogPost
from .models import Contact

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'image']



# # forms.py
# from django import forms
# from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'organisation', 'email', 'phone', 'subject', 'message']
        labels = {
            'full_name': 'Full Name',
            'organisation': 'Organisation',
            'email': 'Email',
            'phone': 'Phone',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Full Name','class':'form-control'}),
            'organisation': forms.TextInput(attrs={'placeholder': 'Your Organisation','class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email','class':'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number','class':'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject','class':'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message','class':'form-control'}),
        }

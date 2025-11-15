# from django.contrib import admin

# from .models import BlogPost,Contact

# admin.site.register(BlogPost)
# admin.site.register(Contact)


from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import BlogPost, Contact


class BlogPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = BlogPost
        fields = '__all__'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostAdminForm
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'organisation')

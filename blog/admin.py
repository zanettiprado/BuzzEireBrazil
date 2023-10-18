from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    """
    Admin settings for our Post model.
    
    We're using Summernote for a fancy text editor.
    This sets how the Posts look and can be searched in the admin area.
    """
    
    list_display = ('title', 'slug', 'status', 'created_on')
    
    search_fields = ('title', 'content')
    
    list_filter = ('status', 'created_on')
    
    prepopulated_fields = {'slug': ('title',)}
    
    summernote_fields = ('content',)
    

class CommentAdmin(admin.ModelAdmin):
    """
    Admin settings for our Comment model.
    
    This sets how Comments are displayed, searched, and managed in the admin area.
    """
    
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    
    search_fields = ('name', 'email', 'body')
    
    list_filter = ('approved', 'created_on')
    
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        A handy button to approve a bunch of comments all at once.
        
        When you select comments and use this action, 
        it'll mark them as approved!
        """
        queryset.update(approved=True)

# Let's tell Django to use our fancy admin settings for Post and Comment.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

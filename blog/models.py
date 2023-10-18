from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choices for the status of a blog post

STATUS = (
    (0, "Draft"),
    (1, "Published") # set to default
)


class Post(models.Model):
    """
    Represents a blog post in the system.

    The 'title' attribute defines the post's title.
    The 'slug' provides an SEO-friendly URL for the post.
    The 'author' links the post to a user in the system.
    The 'content' contains the main content of the blog post.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """Returns the total number of likes for this post."""
        return self.likes.count()


class Comment(models.Model):
    """
    Represents a comment made on a blog post.

    The 'post' attribute links the comment to a specific blog post.
    The 'name' and 'email' capture the commenter's details.
    The 'body' contains the main content of the comment.
    nspired in the Code institute I think Therefore I blog
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class UserSuggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    likes = models.ManyToManyField(User, related_name='suggestion_likes')
    dislikes = models.ManyToManyField(User, related_name='suggestion_dislikes')
    created_on = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    @classmethod
    def total_suggestions(cls):
        return cls.objects.count()


class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

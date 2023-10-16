from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, UserSuggestion
from .forms import CommentForm, UserSuggestionForm, SuggestionForm, PostForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.forms.utils import ErrorList  
from django.contrib.auth.models import User

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new post
            new_post = form.save(commit=False)
            new_post.author = request.user  # Set the author to the currently logged-in user
            new_post.save()
            return redirect(reverse('post_detail', kwargs={"slug": new_post.slug}))  # Redirect to the new post's detail page
    else:
        # Initialize the form with initial values as empty strings ('') and status as "Draft" (0) now the default is set to 1
        form = PostForm(initial={'title': '', 'slug': '', 'excerpt': '', 'content': '', 'status': 0})

    return render(request, 'create_post.html', {'form': form})

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suggestion_form'] = UserSuggestionForm()
        context['suggestions'] = UserSuggestion.objects.all()
        return context

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # queryset = Post.objects.filter(status=1) see if is necessary
        # post = get_object_or_404(queryset, slug=slug)
        post = Post.objects.get(slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
            },
        )

class CommentLike(View):
    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        liked = request.POST.get("liked")

        if liked == "liked" and request.user not in comment.likes.all():
            comment.likes.add(request.user)
        elif liked == "unliked" and request.user in comment.likes.all():
            comment.likes.remove(request.user)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class CommentDislike(View):
    def post(self, request, comment_id, *args, **kwargs):
        comment = get_object_or_404(Comment, id=comment_id)
        disliked = request.POST.get("disliked")

        if disliked == "disliked" and request.user not in comment.dislikes.all():
            comment.dislikes.add(request.user)
        elif disliked == "undisliked" and request.user in comment.dislikes.all():
            comment.dislikes.remove(request.user)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class UserSuggestionView(View):
    def post(self, request, *args, **kwargs):
        suggestion_form = UserSuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            return redirect('home')
        return redirect('home')

    def get(self, request, *args, **kwargs):
        suggestions = UserSuggestion.objects.all()
        suggestion_form = UserSuggestionForm()
        return render(request, 'suggestions.html', {'suggestions': suggestions, 'suggestion_form': suggestion_form})
    
class SuggestionLike(View):
    def post(self, request, suggestion_id, *args, **kwargs):
        suggestion = get_object_or_404(UserSuggestion, id=suggestion_id)
        
        if suggestion.likes.filter(id=request.user.id).exists():
            suggestion.likes.remove(request.user)
        else:
            suggestion.likes.add(request.user)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

class SuggestionDislike(View):
    def post(self, request, suggestion_id, *args, **kwargs):
        suggestion = get_object_or_404(UserSuggestion, id=suggestion_id)
        
        if suggestion.dislikes.filter(id=request.user.id).exists():
            suggestion.dislikes.remove(request.user)
        else:
            suggestion.dislikes.add(request.user)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    
@login_required
@staff_member_required
def edit_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(UserSuggestion, pk=suggestion_id)

    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SuggestionForm(instance=suggestion)

    return render(request, 'edit_suggestion.html', {'form': form, 'suggestion': suggestion})

@login_required
@staff_member_required
def delete_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(UserSuggestion, id=suggestion_id)
    if request.method == 'POST':
        suggestion.delete()
        return redirect('home')
    return render(request, 'delete_suggestion.html', {'suggestion': suggestion})

@login_required
def edit_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(UserSuggestion, pk=suggestion_id)

    if request.user == suggestion.user:
        if request.method == 'POST':
            form = SuggestionForm(request.POST, instance=suggestion)
            if form.is_valid():
                form.save()
                return redirect('home')  
        else:
            form = SuggestionForm(instance=suggestion)

        return render(request, 'edit_suggestion.html', {'form': form, 'suggestion': suggestion})
    else:
        return redirect('home')

@login_required
def edit_comment(request, slug, comment_id):
    # Get the comment and perform authorization checks so the user can edit their own text POSTS in this case
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Ensure that the user editing the comment is the comment owner
    if request.user == comment.name:
        if request.method == "POST":
            # Process the form for editing the comment
            comment_form = CommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
                return redirect('post_detail', slug=slug)
        else:
            # Display the form for editing the comment
            comment_form = CommentForm(instance=comment)
            
        return render(
            request,
            "edit_comment.html",
            {
                "comment_form": comment_form,
                "comment": comment,
            },
        )
    else:
        # Handle the case where the user is not allowed to edit the comment  ok working and redirectiong correctly 
        return redirect('home', slug=slug)

@login_required
def delete_comment(request, slug, comment_id):
    # Get the comment and perform authorization checks - working as expected 
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Ensure that the user deleting the comment is the comment owner - ok now redirecting to home
    if request.user == comment.name:
        if request.method == "POST":
            # Process the deletion of the comment
            comment.delete()
            return redirect('home', slug=slug)
        else:
            # Display the confirmation page for deleting the comment
            return render(
                request,
                "delete_comment.html",
                {
                    "comment": comment,
                },
            )
    else:
        # Handle the case where the user is not allowed to delete the comment
        return redirect('post_detail', slug=slug)
    
@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect('home') # ok now working and again redirecting to home

    return render(request, 'delete_post.html', {'post': post})

@login_required
def index_view(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
        'user': request.user,
    }

    if request.user.is_authenticated:
        for post in post_list:
            post.is_editable = request.user == post.author or request.user.is_staff
    
    return render(request,'index.html', context)
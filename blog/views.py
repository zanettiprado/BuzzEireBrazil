from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment, UserSuggestion
from .forms import CommentForm, UserSuggestionForm, SuggestionForm
from django.contrib.auth.decorators import login_required


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
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
                "comment_form": CommentForm()
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
                "comment_form": comment_form
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
def delete_suggestion(request, suggestion_id):
    suggestion = get_object_or_404(UserSuggestion, id=suggestion_id, user=request.user)
    if request.method == 'POST':
        suggestion.delete()
        return redirect('home')
    return render(request, 'delete_suggestion.html', {'suggestion': suggestion}) 
  

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('your_comment_list_view')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and request.user == comment.user:
        comment.delete()
    return redirect('your_comment_list_view')
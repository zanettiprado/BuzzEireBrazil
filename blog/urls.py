from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('create_post/', views.create_post, name='create_post'), # Creates a new post
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'), # Edit posts
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'), # Delete Posts 
    path('submit-suggestion/', views.UserSuggestionView.as_view(), name='submit_suggestion'), # Send a new suggestion in the bottom of the page
    path('suggestion-like/<int:suggestion_id>/', views.SuggestionLike.as_view(), name='suggestion_like'), # Reaction to the suggestion 
    path('suggestion-dislike/<int:suggestion_id>/', views.SuggestionDislike.as_view(), name='suggestion_dislike'),
    path('suggestion/edit/<int:suggestion_id>/', views.edit_suggestion, name='edit_suggestion'), # Edit Suggestion
    path('suggestion/delete/<int:suggestion_id>/', views.delete_suggestion, name='delete_suggestion'), # Delete Suggestion
    path('<slug:slug>/edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'), # Edit Comment 
    path('<slug:slug>/delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), # Delete Comment
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), # Post main page with details
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('comment-like/<int:comment_id>/', views.CommentLike.as_view(), name='comment_like'), 
    path('comment_dislike/<int:comment_id>/', views.CommentDislike.as_view(), name='comment_dislike'),
    path('sponsorship/contact/', views.sponsorship_contact, name='sponsorship_contact'),
    path('sponsorship/thank-you/', views.sponsorship_thank_you, name='sponsorship_thank_you'),
]
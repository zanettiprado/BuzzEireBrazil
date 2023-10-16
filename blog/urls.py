from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('submit-suggestion/', views.UserSuggestionView.as_view(), name='submit_suggestion'),
    path('create_post/', views.create_post, name='create_post'), #create new post
    path('suggestion-like/<int:suggestion_id>/', views.SuggestionLike.as_view(), name='suggestion_like'),
    path('suggestion-dislike/<int:suggestion_id>/', views.SuggestionDislike.as_view(), name='suggestion_dislike'),
    path('suggestions/<int:suggestion_id/edit/', views.edit_suggestion, name='edit_suggestion'),
    path('suggestions/<int:suggestion_id>/delete/', views.delete_suggestion, name='delete_suggestion'), 
    path('edit_suggestion/<int:suggestion_id>/', views.edit_suggestion, name='edit_suggestion'), # to edit suggestions on index
    path('delete_suggestion/<int:suggestion_id>/', views.delete_suggestion, name='delete_suggestion'),
    path('<slug:slug>/edit-comment/<int:comment_id>/', views.edit_comment, name='edit_comment'), # for edit and delete in post
    path('<slug:slug>/delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'), # for edit and delete in post
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('comment-like/<int:comment_id>/', views.CommentLike.as_view(), name='comment_like'),
    path('comment_dislike/<int:comment_id>/', views.CommentDislike.as_view(), name='comment_dislike'),
]
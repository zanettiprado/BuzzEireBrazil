from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('submit-suggestion/', views.UserSuggestionView.as_view(), name='submit_suggestion'),
    path('suggestion-like/<int:suggestion_id>/', views.SuggestionLike.as_view(), name='suggestion_like'),
    path('suggestion-dislike/<int:suggestion_id>/', views.SuggestionDislike.as_view(), name='suggestion_dislike'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('comment-like/<int:comment_id>/', views.CommentLike.as_view(), name='comment_like'),
    path('comment_dislike/<int:comment_id>/', views.CommentDislike.as_view(), name='comment_dislike'),
]

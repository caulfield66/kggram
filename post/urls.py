from post.views import index, NewPost, PostDetails, tags, like, favorite, delete, edit, SearchResultsView

from django.urls import path

urlpatterns = [
    # path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetails, name='postdetails'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('<uuid:post_id>/like/', like, name='postlike'),
    path('<uuid:post_id>/favorite/', favorite, name='postfavorite'),
    path('<uuid:post_id>/delete/', delete, name='postdelete'),
    path('<uuid:post_id>/edit/', edit, name='postedit'),
    path('post/search/', SearchResultsView.as_view(), name='search-results'),
]
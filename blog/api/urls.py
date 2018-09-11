from django.urls import path
from .views import PostsView, CategoriesView, get_post, TagsView

app_name = "blog"

urlpatterns = [
	# url(r'^messages/(?P<pk>[0-9]+)/$', MessageListAPIView.as_view({'get': 'retrieve'}), name="messages"),
	path('tags', TagsView.as_view()),
	path('categories', CategoriesView.as_view()),
	path('posts', PostsView.as_view()),
	# path('<int:pk>/', get_post),
  path('<slug:post_slug>/', get_post)
]

# from django.conf.urls import url
# from .views import PostsView, CategoriesView, get_post, TagsView

# urlpatterns = [
# 	# url(r'^messages/(?P<pk>[0-9]+)/$', MessageListAPIView.as_view({'get': 'retrieve'}), name="messages"),
# 	url(r'^tags$', TagsView.as_view(), name="tags"),
# 	url(r'^categories$', CategoriesView.as_view(), name="categories"),
# 	url(r'^posts$', PostsView.as_view(), name="posts"),
# 	url(r'^(?P<pk>[0-9]+)/$', get_post, name="post")
# ]
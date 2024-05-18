from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name = "home"),
    path("post/create/", BlogCreateView.as_view(), name = "new_post"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name = "post_detail")
        
         ]

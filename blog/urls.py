"""simple_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from blog.views import index, categoryDetail, createCategory, updateCategory, deleteCategory, listPosts, detailPost, \
    createPost, updatePost, deletePost, file_upload, SendEmail, likePost, addComment;

urlpatterns = [
    path('', index, name='home'),
    path("category/<int:category_id>/detail",categoryDetail,name="category"),
    path("category/create", createCategory, name="create-category"),
    path("category/update", updateCategory, name="update-category"),
    path("category/<int:category_id>/delete", deleteCategory, name="delete-category"),
    path("post/",listPosts.as_view(),name="posts"),
    path("post/<int:pk>/detail", detailPost.as_view(), name="post-detail"),
    path("post/create", createPost.as_view(), name="post-create"),

    path("post/<int:pk>/update", updatePost.as_view(), name="post-update"),
    path("post/<int:pk>/delete", deletePost.as_view(), name="post-delete"),
    path("send_email", SendEmail,name="send_email"),
    path("file_upload", file_upload, name="file_upload"),
    path("likepost", likePost, name="like_post"),
    path("addComment", addComment, name="add_comment"),

]

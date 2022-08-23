from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    title_tag = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_Date = models.DateField(auto_now_add=True)
    snippet = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="post_like")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.post.title + " - " + self.user.username




class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        bio = models.TextField()
        website = models.CharField(max_length=200)

        def __str__(self):
            return self.user.first_name + " - " + self.user.last_name


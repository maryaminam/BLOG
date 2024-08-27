from django.db.models import Model
from django.urls import reverse
from datetime import datetime,date
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-details',args=(str(self.id)))

class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to='images/profile/')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title= models.CharField(max_length=90)
    header_image = models.ImageField(null=True,blank=True,upload_to='images/')
    title_tag= models.CharField(max_length=90, default='BlogGO')
    #this deletes the blog posts related to user the deleted their id (this is object so we have to change to string when using later)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body= models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, default='coding')
    snippet = models.CharField(max_length=50)
    #a post can have many likes and user can have many likes so a many-to-many relationship, related post is like foreign key
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-details',args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments' ,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

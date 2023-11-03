from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post")
    image=models.ImageField(upload_to="post_images")
    caption=models.CharField(max_length=255,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at',]

    # def __str__(self):
    #     return f"{self.user.username} - {self.created_at}"



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='liker')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='liked_post')
    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.user.username}'s post"

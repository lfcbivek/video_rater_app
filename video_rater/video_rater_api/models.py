from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length = 80)
    description = models.CharField(max_length= 300)
    url = models.URLField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    author = models.TextField(max_length=100)

    def rating_average(self):
        sum = 0
        ratings = Rating.objects.filter(video = self)
        for rating in ratings:
            sum = sum + rating.stars
        if len(ratings) > 0:
            avg = sum/len(ratings)
            return avg
        else:
            return 0

    def comments_list(self):
        all_comments = Rating.objects.filter(video=self)
        comments = []

        for comment in all_comments:
            comments.append(comment.comments)
        return comments

class Rating(models.Model):
    video = models.ForeignKey(Video,on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = (('user','video'))
        index_together = (('user','video'))

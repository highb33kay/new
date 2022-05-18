from pyexpat import model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


# class Story(models.Model):
#     story_id = models.IntegerField(blank=True, null=True)
#     story_type = models.CharField(null=True, blank=True, max_length=25)
#     story_by = models.CharField(blank=True, null=True, max_length=200)
#     story_score = models.IntegerField(null=True, blank=True)
#     story_descendants = models.IntegerField(null=True, blank=True)
#     story_title = models.CharField(blank=True, null=True, max_length=10000)
#     story_url = models.URLField(
#         default="http://stoplight.io/prism", blank=True, null=True)

#     def __str__(self):
#         return self.story_title


# class Comment(models.Model):
#     comment_by = models.CharField(max_length=200, null=True, blank=True)
#     comment_id = models.IntegerField(null=True, blank=True)
#     comment_type = models.CharField(max_length=200, null=True)
#     comment_parent = models.ForeignKey(
#         Story, related_name='comment_source', null=True, blank=True, on_delete=models.CASCADE)
#     comment_text = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.comment_parent.story_title

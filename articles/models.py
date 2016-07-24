from datetime import datetime
from model_utils.models import TimeStampedModel

from django.db import models


class Article(TimeStampedModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)
    hero_image = models.ImageField(upload_to='pic_folder/')
    additional_image = models.ImageField(upload_to='pic_folder/')

    class Meta:
        db_table = 'article'

    def __unicode__(self):
        return self.title

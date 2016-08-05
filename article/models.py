from django.db import models

# Create your models here.


class Article(models.Model):
    art_title = models.CharField(max_length=20)
    art_pub_date = models.DateTimeField('article published')
    art_content = models.TextField()
    art_type = models.CharField(max_length=20)
    art_view_num = models.IntegerField()
    art_reply_num = models.IntegerField()

    def __str__(self):
        return self.art_title


class Reply(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    rp_title = models.CharField(max_length=20)
    rp_content = models.TextField()
    rp_pub_date = models.DateTimeField()

    def __str__(self):
        return self.rp_title


class Drift(models.Model):

    dr_title = models.CharField(max_length=40)
    dr_content = models.TextField()
    dr_pub_date = models.DateTimeField()
    dr_type = models.CharField(max_length=20)

    def __str__(self):
        return self.dr_title



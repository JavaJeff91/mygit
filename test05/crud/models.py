from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100,blank=False)
    age = models.CharField(max_length=2)
    married = models.BooleanField(default=False)
    introduce = models.TextField()
    addTime = models.DateTimeField(auto_now=True)
    updateTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
        ordering = ('-addTime',)

class Book(models.Model):
    name = models.CharField(max_length=100,blank=False)
    info = models.TextField()
    type = models.IntegerField(blank=False,default=0)
    updateTime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    count = models.CharField(max_length=20)
    author = models.ForeignKey(Author,default=1)

    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'
        ordering = ('status',)

    def contract(self):
        return 'this method just a test'
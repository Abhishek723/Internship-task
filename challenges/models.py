from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Tags(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Challenge(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    end_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    active_solvers = models.IntegerField()
    price = models.IntegerField()
    tags = models.ManyToManyField(Tags)
    model_pic= models.ImageField(upload_to='upload_image', default='challenges/images/already.jpg')
    
    def upload_image(self, filename):
        return 'challenge/{}/{}'.format(self.title, filename)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
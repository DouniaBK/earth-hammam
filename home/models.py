from django.db import models

# Create your models here.


STATUS = ((0, "Draft"), (1, "Published"))


class Testimonial(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f'{self.name}'

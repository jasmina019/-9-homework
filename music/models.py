from django.db import models
from django.shortcuts import reverse

class Music(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.DateField()

    def get_detail_url(self):
        return reverse('music:music_detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('music:music_delete', args=[self.pk])

    def get_update_url(self):
        return reverse('music:music_update', args=[self.pk])
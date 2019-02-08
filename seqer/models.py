from django.db import models

class Sequences(models.Model):
    title = models.CharField(max_length=200, default = 'seq')
    sequence = models.TextField()
    def count(sequence):
        return print(len(sequence))

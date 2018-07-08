from __future__ import unicode_literals

from django.db import models
from django.core import validators


class Candidate(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    name = models.CharField(max_length=256)
    years_exp = models.PositiveSmallIntegerField(
        validators = [
            validators.MaxValueValidator(50),
        ]
    )
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=256)
    date_applied = models.DateTimeField()
    reviewed = models.BooleanField(default=False)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, *args, **kwargs):
        if self.status == 'accepted' or self.status == 'rejected':
            self.reviewed = True
        super(Candidate, self).save(*args, *kwargs)

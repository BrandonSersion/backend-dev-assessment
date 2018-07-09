from __future__ import unicode_literals

from django.db import models
from django.core import validators
from rest_framework.exceptions import ValidationError


class Status:
    """Valid choices for Candidate 'status' field."""
    NONE = '0'
    PENDING = '1'
    ACCEPTED = '2'
    REJECTED = '3'
    CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    )


class Candidate(models.Model):
    """Candidates for job posting."""
    name = models.CharField(max_length=256)
    years_exp = models.PositiveSmallIntegerField(
        validators = [
            validators.MaxValueValidator(50),
        ]
    )
    status = models.CharField(
        choices=Status.CHOICES,
        default=Status.PENDING,
        max_length=1,
    )
    date_applied = models.DateTimeField()
    reviewed = models.BooleanField(default=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, *args, **kwargs):
        """Override models.Model save function.
        
        Validate candidate can't update directly from 'accepted' into 'rejected',
        or vice versa - but can update into pending in between. 

        Auto update reviewed field to 'True' the first time a candidate
        updates from 'pending' to 'accepted' or 'rejected'.

        Argument force_insert=False fixes exception sometimes triggered on create:
        "Cannot force both insert and updating in model saving."
        """
        # Special validation on update.
        # Get status prior to update, compare it to update's status.
        try: prior_status = Candidate.objects.get(pk=self.pk).status
        except: prior_status = None

        if (prior_status == Status.ACCEPTED) and (self.status == Status.REJECTED):
            message = "Can't update accepted candidate directly into rejected. Update to pending first."
            raise ValidationError(message)
        if (prior_status == Status.REJECTED) and (self.status == Status.ACCEPTED):
            message = "Can't update rejected candidate directly into accepted. Update to pending first."
            raise ValidationError(message)

        if prior_status == Status.PENDING and (self.status == Status.ACCEPTED or self.status == Status.REJECTED):
            self.reviewed = True

        return super().save(*args, *kwargs)
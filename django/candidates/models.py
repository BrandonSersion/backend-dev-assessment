from __future__ import unicode_literals

import logging
from django.db import models
from django.core import validators
from rest_framework.exceptions import ValidationError

logger = logging.getLogger(__name__)


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
        validators=[
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

        Auto update reviewed field to 'True' when a candidate
        updates from 'pending' to 'accepted' or 'rejected'.

        Argument force_insert=False fixes exception sometimes triggered on create:
        "Cannot force both insert and updating in model saving."
        """
        # Check if the request pk matches a prior candidate in the database.
        # If yes, trigger custom logic meant for update requests only.
        prior_object = Candidate.objects.filter(pk=self.pk).first()
        is_update = True if prior_object else False

        if is_update:
            if (prior_object.status is Status.ACCEPTED) and (self.status is Status.REJECTED):
                message = "Can't update accepted candidate directly into rejected. Update to pending first."
                raise ValidationError(message)
            elif (prior_object.status is Status.REJECTED) and (self.status is Status.ACCEPTED):
                message = "Can't update rejected candidate directly into accepted. Update to pending first."
                raise ValidationError(message)

            elif (prior_object.status is Status.PENDING) and (self.status is Status.ACCEPTED or self.status is Status.REJECTED):
                if not self.reviewed:
                    self.reviewed = True
                    logger.info(f'Candidate {self.name} set to reviewed - primary key {self.pk}.')

        return super().save(*args, *kwargs)
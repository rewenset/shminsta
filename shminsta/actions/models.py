from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey(User, related_name='actions', db_index=True)   # who performed the action
    verb = models.CharField(max_length=255)                                 # describing the action

    target_ct = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj')
    target_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')

    created = models.DateTimeField(auto_now_add=True, db_index=True)        # when this was created

    class Meta:
        ordering = ('-created',)

from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    # a user can post multiple images, but each image is posted by a single user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created')
    # a user might like multiple images and each image can be liked by multiple users
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # when no slug is provided
            self.slug = slugify(self.title)  # generate the image slug for the given title
            super(Image, self).save(*args, **kwargs)
from django.db import models
from django.contrib.auth.models import User
from .slug import unique_slugify
from django.utils import timezone

class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        slug = '%s' % (self.name)
        unique_slugify(self, slug)
        super(State, self).save()


class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        slug = '%s' % (self.name)
        unique_slugify(self, slug)
        super(Hospital, self).save()


class Update(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    ventilators = models.IntegerField(null=True)
    ventilators_total = models.IntegerField(null=True)
    masks = models.IntegerField(null=True)
    masks_total = models.IntegerField(null=True)
    gloves = models.IntegerField(null=True)
    gloves_total = models.IntegerField(null=True)
    respirators = models.IntegerField(null=True)
    respirators_total = models.IntegerField(null=True)
    pui = models.IntegerField(null=True)
    confirmed = models.IntegerField(null=True)
    acute_care = models.IntegerField(null=True)
    acute_care_total = models.IntegerField(null=True)
    icu = models.IntegerField(null=True)
    icu_total = models.IntegerField(null=True)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.created)



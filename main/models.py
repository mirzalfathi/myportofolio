import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.IntegerField()
    ended_at = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    LEVEL_CHOICES = [
        ('smp', 'SMP'),
        ('sma', 'SMA/SMK'),
        ('s1', 'S1'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution_name = models.CharField(max_length=255)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='S1')
    major = models.CharField(max_length=255, blank=True, default="")
    description = models.CharField(max_length=255, blank=True, default="")
    image = models.URLField(max_length=500, blank=True, default="")
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution_name} - {self.get_level_display()}"

    @property
    def is_ongoing(self):
        return self.end_year is None
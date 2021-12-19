from django.db import models

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=400)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    # published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=500)

    vid_id = models.CharField(max_length=100, unique=True)

    class Meta:
        # indexing databasefor faster queries:
        # like searching and sorting
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['vid_id'])
        ]


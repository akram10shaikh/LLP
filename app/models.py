from django.db import models

class Section8(models.Model):
    client_name = models.CharField(max_length=100)
    client_role = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='Section8/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=5)
    message = models.TextField()
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.client_name} - {self.client_role}"

class Section7(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='trusted_clients/')
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title

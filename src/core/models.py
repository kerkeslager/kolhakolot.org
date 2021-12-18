from django.db import models

class ApprovedEmail(models.Model):
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email

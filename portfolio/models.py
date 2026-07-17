from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, help_text="Short headline summary of the solution.")
    role = models.CharField(max_length=100, default="Product Manager & UX Designer")
    timeline = models.CharField(max_length=50, help_text="e.g., Q3 2025")
    impact_metric = models.CharField(max_length=100, help_text="e.g., +40% Conversion")
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Lower numbers display first.")

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title


class ActiveThought(models.Model):
    phrase = models.CharField(max_length=250, help_text="tell me what ya thinkin' bish")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.phrase
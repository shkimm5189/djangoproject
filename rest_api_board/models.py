from django.db import models

# Create your models here.

class MyBoard(models.Model):

    subject = models.CharField(max_length=30, null=False)
    content = models.TextField(max_length=300, null=False)
    author = models.CharField(max_length=30, null=False)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    create_by = models.CharField(max_length=20, null=False)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "board_test"

    def __str__(self):
        return self.subject



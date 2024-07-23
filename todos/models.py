from datetime import date
from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Titulo" ,max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Data de entrega" ,null=False, blank=False)
    finish_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finish_at:
            self.finish_at = date.today()
            self.save()


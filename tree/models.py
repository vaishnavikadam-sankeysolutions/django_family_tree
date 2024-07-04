from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    spouse = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='partner')

    def __str__(self):
        return self.name

    @property
    def parent_id(self):
        return self.parent.id if self.parent else None

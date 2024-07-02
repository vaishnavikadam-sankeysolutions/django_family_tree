from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Relationship(models.Model):
    RELATIONSHIP_CHOICES = [
        ('PARENT', 'Parent'),
        ('SPOUSE', 'Spouse'),
        ('CHILD', 'Child'),
    ]

    from_person = models.ForeignKey(Person, related_name='relationships_from', on_delete=models.CASCADE)
    to_person = models.ForeignKey(Person, related_name='relationships_to', on_delete=models.CASCADE)
    relationship_type = models.CharField(max_length=10, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return f"{self.from_person} -> {self.to_person} ({self.relationship_type})"
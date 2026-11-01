from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(
        max_digits=8,
        decimal_places=2
    )


def __str__(self):
return self.title

class Student(models.Model):

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=False,
        default="Unknown"
    )

    email = models.EmailField(
        unique=True
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
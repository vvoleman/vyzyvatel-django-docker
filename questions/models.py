from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    popularity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_numeric = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=255)
    wrong_answer1 = models.CharField(max_length=255)
    wrong_answer2 = models.CharField(max_length=255)
    wrong_answer3 = models.CharField(max_length=255)

    def __str__(self):
        return self.question

from email.policy import default
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    popularity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=Category.objects.get(id=1))
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, default=Type.objects.get(id=1))
    question = models.CharField(max_length=255)
    right_answer = models.CharField(max_length=255)
    wrong_answer1 = models.CharField(max_length=255)
    wrong_answer2 = models.CharField(max_length=255)
    wrong_answer3 = models.CharField(max_length=255)

    def __str__(self):
        return self.question

    def get_category(self):
        return self.category.name

    def get_type(self):
        return self.type.name

    def answers(self):
        return [self.right_answer, self.wrong_answer1, self.wrong_answer2, self.wrong_answer3]

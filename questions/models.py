from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    popularity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class PickQuestion(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    question = models.CharField(max_length=255, blank=False)
    right_answer = models.CharField(max_length=64, blank=False)
    wrong_answer_1 = models.CharField(max_length=64, blank=False)
    wrong_answer_2 = models.CharField(max_length=64, blank=False)
    wrong_answer_3 = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.question

    def get_category(self):
        return self.category.name

    def wrong_answers(self):
        return [self.wrong_answer_1, self.wrong_answer_2, self.wrong_answer_3]


class NumericQuestion(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    question = models.CharField(max_length=255, blank=False)
    right_answer = models.IntegerField(blank=False)

    def __str__(self):
        return self.question

    def get_category(self):
        return self.category.name


class ImageQuestion(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    image_url = models.CharField(max_length=255, blank=False)

    question = models.CharField(max_length=255, blank=False)
    right_answer = models.CharField(max_length=64, blank=False)
    wrong_answer_1 = models.CharField(max_length=64, blank=False)
    wrong_answer_2 = models.CharField(max_length=64, blank=False)
    wrong_answer_3 = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.question

    def get_category(self):
        return self.category.name

    def wrong_answers(self):
        return [self.wrong_answer_1, self.wrong_answer_2, self.wrong_answer_3]

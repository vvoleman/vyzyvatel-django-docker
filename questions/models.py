from django.db import models
from PIL import Image
import io
from django.core.files import File
import random
import string


class Category(models.Model):
    name = models.CharField(max_length=64)
    popularity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-popularity', )

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

    def save(self, *args, **kwargs):
        if not self.category:
            latest_question = NumericQuestion.objects.latest('id')
            self.category = latest_question.category
        super().save(*args, **kwargs)


class ImageQuestion(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='image_question/')

    question = models.CharField(
        max_length=255, blank=False, default='Co je na obrázku?')
    right_answer = models.CharField(max_length=64, blank=False)
    wrong_answer_1 = models.CharField(max_length=64, blank=False)
    wrong_answer_2 = models.CharField(max_length=64, blank=False)
    wrong_answer_3 = models.CharField(max_length=64, blank=False)

    def __str__(self):
        return self.question

    def image_url(self):
        return self.image.url

    def get_category(self):
        return self.category.name

    def wrong_answers(self):
        return [self.wrong_answer_1, self.wrong_answer_2, self.wrong_answer_3]

    def save(self, *args, **kwargs):
        try:
            original_image = ImageQuestion.objects.get(pk=self.pk).image
        except ImageQuestion.DoesNotExist:
            original_image = None

        if original_image is None or self.image != original_image:
            img = Image.open(self.image).convert("RGB")

            img.thumbnail((1400, 400))

            img_io = io.BytesIO()
            img.save(img_io, 'JPEG', quality=70)
            img_io.seek(0)

            random_name = ''.join(random.choice(
                string.ascii_letters + string.digits) for _ in range(16)) + ".jpeg"

            self.image = File(img_io, name=random_name)

        super().save(*args, **kwargs)

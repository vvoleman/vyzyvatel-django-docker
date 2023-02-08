from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id, name', 'popularity')


class PickQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'right_answer',
                    'wrong_answers')
    list_filter = [
        "category",
    ]


class NumericQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'right_answer')
    list_filter = [
        "category",
    ]


class ImageQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'right_answer',
                    'wrong_answers', 'image_url')
    list_filter = [
        "category",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(PickQuestion, PickQuestionAdmin)
admin.site.register(NumericQuestion, NumericQuestionAdmin)
admin.site.register(ImageQuestion, ImageQuestionAdmin)

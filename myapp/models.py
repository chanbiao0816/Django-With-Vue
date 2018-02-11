# encoding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name

class Option(models.Model):
    option_desc = models.CharField(max_length=64)
    option_value = models.CharField(max_length=64)

    def __str__(self):
        return self.show_desc_value()

    def show_desc_value(self):
        return self.option_desc + '_' + self.option_value

    class Meta:
        verbose_name = "选项"
        verbose_name_plural = "选项"

class Question(models.Model):
    question_desc = models.CharField(max_length=64)
    option = models.ManyToManyField(Option,
        related_name='question',
        blank=True, null=True,
        verbose_name='选项',)

    def __str__(self):
        return self.question_desc

    def options(self):
       return self.option.all()

    def show_options(self):
       return ','.join([ele.show_desc_value() for ele in self.options()])

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "问题"

class Answer(models.Model):
    user = models.CharField(max_length=64)
    question = models.ForeignKey(Question,
        related_name='answer',
        on_delete=models.CASCADE,)
    option = models.ForeignKey(Option,
        related_name='answer',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "答案"
        verbose_name_plural = "答案"

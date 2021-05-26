import datetime

from django.db import models

# Create your models here.

# 설문내용(제목, 날짜)
# 이 설문에 대한 답변(답변, 개수)
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    #question_description = models.CharField(max_length=1000, verbose_name='설명', null=True)
    question_description = models.TextField(null=True, verbose_name="설명")
    pub_date = models.DateTimeField('등록 일자')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.short_description = '최근 질문 여부'
    was_published_recently.boolean = True

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

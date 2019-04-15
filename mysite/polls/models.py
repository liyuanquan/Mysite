# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200) #问题描述
    pub_date = models.DateTimeField('date published') #退出时间

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #外键关联
    choice_text = models.CharField(max_length=200) #选择内容
    votes = models.IntegerField(default=0)#选择计数

    def __str__(self):
        return self.choice_text
#coding=utf-8
from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import Permission

input_formats = ['%d-%m-%Y']
YEAR_CHOICES = ('2015', '2016')

class TermManager(models.Manager):
    def for_user(self, user):
        return super(TermManager, self).get_query_set().filter(user=user)

class Term(models.Model):
	term = models.DateField('Срок')
	date = models.DateField('Дата закрытия')
	user = models.ForeignKey('auth.User')
	objects = TermManager()
	
	class Meta:
		verbose_name = 'KPI'
		verbose_name_plural = 'KPI сотрудников'

	def __unicode__(self):
		return str(self.term)[:7]


class Kpi(models.Model):
	name = models.CharField('KPI', max_length=200)
	dates = models.ForeignKey(Term)

	def __unicode__(self):
		return self.name

class Aim(models.Model):
	POSITIVE = 'Pos'
	NEUTRAL = 'Neu'
	NEGATIVE = 'Neg'
	DIFFERENCE_CHOICES = (
		(NEGATIVE, 'Отрицательно'),
		(NEUTRAL, 'Норма'),
		(POSITIVE, 'Положительно'),
    )

	aim_name = models.CharField('Задача', max_length=200)
	value = models.CharField('Значение', max_length=200)
	difference = models.CharField('Разница', max_length=200, 
		choices=DIFFERENCE_CHOICES, default=NEGATIVE)
	commentary = models.CharField('Комментарии', max_length=500)
	kpi = models.ForeignKey(Kpi)

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'
		

	def __unicode__(self):
		return self.aim_name
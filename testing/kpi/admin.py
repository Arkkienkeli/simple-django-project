#coding=utf-8
from django.contrib import admin
from django import forms
from .models import Kpi, Term, Aim, TermManager
import nested_admin


class AimInline(nested_admin.NestedStackedInline):
	model = Aim
	extra = 1

	def get_readonly_fields(self, request, obj=None):
		if not request.user.is_superuser and request.user.is_staff:
			return self.readonly_fields + ('aim_name', 'value', 'differnce', 'commentary',)
		return self.readonly_fields

class KpiInline(nested_admin.NestedStackedInline):
	model = Kpi
	extra = 1
	inlines = [
		AimInline,
	]
	
	def get_readonly_fields(self, request, obj=None):
		if not request.user.is_superuser and request.user.is_staff:
			return self.readonly_fields + ('name',)
		return self.readonly_fields

class TermAdmin(nested_admin.NestedAdmin):
	list_filter = ('user',)
	inlines = [
		KpiInline,
	]

	def get_queryset(self, request):
		qs = super(TermAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(user=request.user)
	
	def get_readonly_fields(self, request, obj=None):
		if not request.user.is_superuser and request.user.is_staff:
			return self.readonly_fields + ('user','term','date')
		return self.readonly_fields
	
admin.site.register(Term, TermAdmin)
from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
  search_fields = ['subject', 'content']

class AnswerAdmin(admin.ModelAdmin):
  search_fields = ['subject', 'content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
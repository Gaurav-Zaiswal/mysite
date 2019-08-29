# from django.contrib import admin
# from .models import Question
# from .models import Choice

# admin.site.register(Question)  # Questioin ko UI will be created on the admin panel to add que easily.
# admin.site.register(Choice)

from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


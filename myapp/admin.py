from django.contrib import admin

# Register your models here.
from myapp import models as app_models

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_desc', 'show_options']

class OptionAdmin(admin.ModelAdmin):
    list_display = ['option_desc', 'option_value']

admin.site.register(app_models.Book)
admin.site.register(app_models.Question, QuestionAdmin)
admin.site.register(app_models.Option)
admin.site.register(app_models.Answer)

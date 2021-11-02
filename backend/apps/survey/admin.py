from django.contrib import admin
from apps.survey.models import (
    Survey,
    Question,
    Answer,
    SubmitAnswer,
    SubmitSurvey
)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ["title", "data_start", "data_end", "published"]
    ordering = ["title", 'data_start', 'data_end']
    search_fields = ["title"]


@admin.register(Question)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ["text", "type"]
    ordering = ["type"]
    search_fields = ["text"]


@admin.register(Answer)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(SubmitSurvey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(SubmitAnswer)
class SurveyAdmin(admin.ModelAdmin):
    pass

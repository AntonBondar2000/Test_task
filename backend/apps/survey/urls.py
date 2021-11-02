from django.urls import path, include
from apps.survey.views import (
    SurveyViewSet,
    AdministrationSurveyViewSet,
    AdministrationAnswerViewSet,
    AdministrationQuestionViewSet,
    SubmitSurveys,
    CompletedSurveysViewSet,
    RemainingSurveysViewSet,
    CompletingSurveyViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'surveys', SurveyViewSet, basename='general_survey')
router.register(r'completed-surveys', CompletedSurveysViewSet, basename='completed_surveys')
router.register(r'remaining-surveys', RemainingSurveysViewSet, basename='remaining-surveys')
router.register(r'completing-surveys', CompletingSurveyViewSet, basename='remaining-surveys')

administration_router = DefaultRouter()
administration_router.register(r'surveys', AdministrationSurveyViewSet, basename="administration_survey")
administration_router.register(r'questions', AdministrationQuestionViewSet, basename="administration_question")
administration_router.register(r'answers', AdministrationAnswerViewSet, basename="administration_answer")

urlpatterns = [
    path('administration/', include(administration_router.urls)),
    path('general/', include(router.urls)),
    path('general/submit-surveys', SubmitSurveys.as_view()),
]
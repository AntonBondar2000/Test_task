from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from apps.survey.models import Survey, Question, Answer, SubmitSurvey, SubmitAnswer
from apps.survey.mixins import MultiSerializerMixin
from apps.survey.serializers import (
    SurveyListSerializer,
    SurveyDetailSerializer,
    SurveyBaseSerializer,
    QuestionBaseSerializer,
    AnswerBaseSerializer,
    CompletingSurveySerializer,
)


class CompletingSurveyViewSet(ReadOnlyModelViewSet):
    """ (user) Completing the survey """
    serializer_class = CompletingSurveySerializer
    authentication_classes = []
    permission_classes = []
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        survey_id = self.request.query_params.get('survey_id')
        return SubmitSurvey.objects.filter(user_id=user_id, survey_id=survey_id)


class SurveyViewSet(MultiSerializerMixin):
    """ (users) List and Retrieve published Survey """
    serializer_classes = {
        'list': SurveyListSerializer,
        'retrieve': SurveyDetailSerializer
    }
    queryset = Survey.objects.filter(published=True)
    default_serializer_class = SurveyListSerializer
    authentication_classes = []
    permission_classes = []


class CompletedSurveysViewSet(MultiSerializerMixin):
    """ (users) List and Retrieve completed Survey """
    serializer_classes = {
        'list': SurveyListSerializer,
        'retrieve': SurveyDetailSerializer
    }
    default_serializer_class = SurveyListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Survey.objects.filter(submit_survey__user_id=user_id)


class RemainingSurveysViewSet(MultiSerializerMixin):
    """ (users) List and Retrieve Remaining Survey """
    serializer_classes = {
        'list': SurveyListSerializer,
        'retrieve': SurveyDetailSerializer
    }
    default_serializer_class = SurveyListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Survey.objects.exclude(submit_survey__user_id=user_id)


class AdministrationSurveyViewSet(ModelViewSet):
    """ (administration) CRUD model Survey """
    queryset = Survey.objects.all()
    serializer_class = SurveyBaseSerializer
    authentication_classes = []
    permission_classes = []

    def perform_update(self, serializer):
        serializer.validated_data.pop('data_start', None)
        serializer.validated_data.pop('data_end', None)
        serializer.save()


class AdministrationQuestionViewSet(ModelViewSet):
    """ (administration) CRUD model Question """
    queryset = Question.objects.all()
    serializer_class = QuestionBaseSerializer
    authentication_classes = []
    permission_classes = []


class AdministrationAnswerViewSet(ModelViewSet):
    """ (administration) CRUD model Answer """
    queryset = Answer.objects.all()
    serializer_class = AnswerBaseSerializer
    authentication_classes = []
    permission_classes = []


class SubmitSurveys(APIView):
    """ Adding the completed survey """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:
            user_id = request.data['user_id']
            answers = request.data['answer']
            survey_id = request.data['survey_id']
            if SubmitSurvey.objects.filter(user_id=user_id, survey_id=survey_id).count() > 0:
                raise Exception('The current user has already passed the survey ')
            user_survey = SubmitSurvey(
                user_id=user_id,
                survey_id=survey_id
            )
            user_survey.save()
            for item in answers:
                submit_answer = SubmitAnswer(
                    submit_survey=user_survey,
                    text_into_textfield=item['text'],
                    question_id=item['question_id'],
                )
                submit_answer.save()
                submit_answer.answer_choices.add(*item['answer_choice'])
                submit_answer.save()
            return Response("successful")
        except Exception:
            raise "Invalid data"

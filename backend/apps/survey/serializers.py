from rest_framework import serializers
from apps.survey.models import Survey, Question, Answer, SubmitSurvey, SubmitAnswer


class SurveyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            "id",
            "title",
            "description",
            "data_start",
            "data_end"
        ]


class SurveyDetailSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = [
            "id",
            "title",
            "description",
            "data_start",
            "data_end",
            "questions"
        ]

    def get_questions(self, instance):
        return QuestionsSerializer(instance.questions.all(), many=True).data


class QuestionsSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "id",
            "text",
            "type",
            "answer"
        ]

    def get_answer(self, instance):
        return AnswersSerializer(instance.answer.all(), many=True).data

    def get_type(self, instance):
        return instance.get_type_display()


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "text",
        ]


class SubmitAnswerSerializer(serializers.ModelSerializer):
    question = QuestionsSerializer()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = SubmitAnswer
        fields = [
            "question",
            'answer'
        ]

    def get_answer(self, instance):
        if instance.text_answer and instance.question.type == 1:
            return instance.text_answer
        return AnswersSerializer(instance.answer_choices.all(), many=True).data


class CompletingSurveySerializer(serializers.ModelSerializer):
    survey = SurveyListSerializer()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = SubmitSurvey
        fields = [
            "id",
            "survey",
            "answer"
        ]

    def get_answer(self, instance):
        return SubmitAnswerSerializer(instance.submit_answer.all(), many=True).data


class SurveyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = "__all__"


class QuestionBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"

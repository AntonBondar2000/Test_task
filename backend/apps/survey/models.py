from django.db import models


class Answer(models.Model):
    text = models.CharField(
        max_length=250
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


class Question(models.Model):
    TYPE_CHOICES = (
        (1, "Text"),
        (2, "Single choice"),
        (3, "Multiple choice")
    )
    text = models.CharField(
        max_length=250
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES,
        default=1
    )
    answer = models.ManyToManyField(
        Answer,
        blank=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"


class Survey(models.Model):
    published = models.BooleanField()
    title = models.CharField(
        max_length=150
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    data_start = models.DateTimeField()
    data_end = models.DateTimeField()
    questions = models.ManyToManyField(
        Question
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Survey"
        verbose_name_plural = "Surveys"
        ordering = ["-data_start"]


class SubmitSurvey(models.Model):
    user_id = models.IntegerField()
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE,
        related_name="submit_survey"
    )

    def __str__(self):
        return self.survey.title

    class Meta:
        verbose_name = "Submit survey"
        verbose_name_plural = "Submit surveys"


class SubmitAnswer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    submit_survey = models.ForeignKey(
        SubmitSurvey,
        on_delete=models.CASCADE,
        related_name="submit_answer"
    )
    text_answer = models.TextField(
        blank=True,
        null=True
    )
    answer_choices = models.ManyToManyField(
        Answer,
        blank=True
    )

    def __str__(self):
        return self.question.text

    class Meta:
        verbose_name = "Submit answer"
        verbose_name_plural = "Submit answers"

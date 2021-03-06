from django.db import models

from quests.fields import DefaultStaticImageField
from users.models import User


class Quest(models.Model):
    DEFAULT_PREVIEW_PATH = "/quest_previews/default.png"

    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    preview = DefaultStaticImageField(upload_to='quest_previews', default_image_path=DEFAULT_PREVIEW_PATH, blank=True)
    welcome_text = models.CharField(max_length=1000)
    farewell_text = models.CharField(max_length=1000)
    penalty_1 = models.TimeField()
    penalty_2 = models.TimeField()


class Task(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    tip_1 = models.CharField(max_length=1000, blank=True)
    tip_2 = models.CharField(max_length=1000, blank=True)


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='answers')
    answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.answer)


class TeamStatistic(models.Model):
    team = models.OneToOneField(User, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='teams_statistic')
    first_task = models.IntegerField(default=0)


class TaskStatistic(models.Model):
    team_statistic = models.ForeignKey(TeamStatistic, on_delete=models.CASCADE, related_name='tasks_statistic')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='statistic')
    tip_1_used = models.BooleanField(default=False)
    tip_2_used = models.BooleanField(default=False)
    lead_time = models.TimeField(blank=True, null=True)

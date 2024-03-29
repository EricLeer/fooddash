import datetime

from django.db import models
from django.utils import timezone

class Recipes(models.Model):
    recipe_url = models.CharField(max_length=200)
    recipe_titel = models.CharField(max_length=200)
    recipe_img_url = models.CharField(max_length=200, default="https://www.takeoutlist.com/assets/images/food_default.png")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.recipe_titel

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

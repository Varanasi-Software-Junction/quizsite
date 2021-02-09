from django.db import models

# Create your models here.

class QuizModel(models.Model):

   question = models.CharField(max_length = 300)
   opta = models.CharField(max_length = 50)
   optb = models.CharField(max_length = 50)
   optc = models.CharField(max_length = 50)
   optd = models.CharField(max_length = 50)
   correctanswer = models.IntegerField()


   class Meta:
      db_table = "questions"

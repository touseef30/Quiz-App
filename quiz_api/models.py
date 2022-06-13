from django.db import models
from profiles_api.models import UserProfile
# Create your models here.

# Create your models here.
class Quiz(models.Model):
    name = models.CharField(max_length=100)
    teacher=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        """String"""
        return str(self.id) +':'+self.name


class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=1000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    def __str__(self):
        """String"""
        return self.question
    
class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    student=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    score=models.IntegerField()
    def __str__(self):
        """String"""
        return self.student.email+" "+self.quiz.name+" "+str(self.score)

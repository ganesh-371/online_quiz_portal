from django.db import models

from student.models import Student
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Aptitude(models.Model):
    name=models.CharField(max_length=50)
    number_of_questions = models.PositiveIntegerField()
    marks = models.PositiveIntegerField()
    def __str__(self):
        return self.marks


class Question1(models.Model):
    aptitude=models.ForeignKey(Aptitude,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    query=models.CharField(max_length=600)
    optionA=models.CharField(max_length=200)
    optionB=models.CharField(max_length=200)
    optionC=models.CharField(max_length=200)
    optionD=models.CharField(max_length=200)
    cat=(('OptionA','OptionA'),('OptionB','OptionB'),('OptionC','OptionC'),('OptionD','OptionD'))
    answer=models.CharField(max_length=200,choices=cat)


class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

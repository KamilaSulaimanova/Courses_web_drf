from re import S
from django.db import models
from account.models import User
from datetime import date
from dateutil import relativedelta


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Student's fullname")


    def __str__(self):
        return self.name


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Mentor's fullname")


    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Course name")
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, through='CourseFlow')
    month = models.SmallIntegerField()

    def __str__(self):
        return self.name


class CourseFlow(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.end_date = date.today() + relativedelta(month=self.course.month)
        super(CourseFlow, self).save(*args, **kwargs)


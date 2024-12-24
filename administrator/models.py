from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=30, null=True,blank=True) 
    password=models.CharField(max_length=30, null=True,blank=True) 
    type=models.CharField(max_length=30, null=True,blank=True) 
    status=models.CharField(max_length=30, null=True,blank=True) 

class StudentTable(models.Model):
    LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
    studentname = models.CharField(max_length=30, null=True,blank=True) 
    department=models.CharField(max_length=30,null=True,blank=True)  
    regno=models.IntegerField(null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=30,null=True,blank=True)
    semester=models.IntegerField(null=True,blank=True)
    
class facultyTable(models.Model):
    LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True,blank=True)
    department=models.CharField(max_length=30,null=True,blank=True)
    subject=models.CharField(max_length=30,null=True,blank=True)
    qualification=models.CharField(max_length=30,null=True,blank=True)
    phoneno=models.BigIntegerField(null=True,blank=True)

class complaintTable(models.Model):
    LOGIN=models.ForeignKey(logintable, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    reply=models.CharField(max_length=200,null=True,blank=True)

class Timetable(models.Model):
     department=models.CharField(max_length=200,null=True,blank=True)
     hour=models.IntegerField(null=True,blank=True)

class notificationTable(models.Model):
     post=models.CharField(max_length=200,null=True,blank=True)
     date = models.DateTimeField(auto_now_add=True)


class markupTable(models.Model):
    FACULTY=models.ForeignKey(facultyTable, on_delete=models.CASCADE)
    STUDENT=models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    mark=models.IntegerField(null=True,blank=True)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TimetableEntry(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(facultyTable, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # Monday, Tuesday, etc.
    time_slot = models.CharField(max_length=50)  # For example, "09:00-10:00"

    def __str__(self):
        return f"{self.subject.name} by {self.teacher.name} in {self.classroom.name} on {self.day_of_week} at {self.time_slot}"




  
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
    date=models.DateField(auto_now_add=True, null=True,blank=True)
    reply=models.CharField(max_length=200,null=True,blank=True)

class notificationTable(models.Model):
     post=models.CharField(max_length=200,null=True,blank=True)
     date = models.DateTimeField(auto_now_add=True)


class markupTable(models.Model):
    FACULTY=models.ForeignKey(facultyTable, on_delete=models.CASCADE)
    mark=models.CharField(null=True, max_length=100,blank=True)
    STUDENT=models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


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
class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    CLASS = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    slot_9_10 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_9_10")
    slot_10_11 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_10_11")
    slot_11_12 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_11_12")
    slot_1_2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_1_2")
    slot_2_3 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_2_3")
    slot_3_4 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_3_4")

    def _str_(self):
        return f"{self.day} Timetable"

class TimetableEntry(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # Monday, Tuesday, etc.
    time_slot = models.CharField(max_length=50)  # For example, "09:00-10:00"

    # def __str__(self):
    #     return f"{self.subject.name} by {self.teacher.name} in {self.classroom.name} on {self.day_of_week} at {self.time_slot}"


# class fac_registrationTable(models.Model):
#     FirstName =models.CharField(max_length=200,null=True,blank=True)
#     LastName =models.CharField(max_length=200,null=True,blank=True)
#     Email=models.CharField(max_length=200,null=True,blank=True)
#     PhoneNumber=models.IntegerField(null=True,blank=True)
#     Department=models.CharField(max_length=200,null=True,blank=True)
#     BriefBiography=models.CharField(max_length=300, null=True,blank=True) 
#     LOGINID=models.ForeignKey(logintable,on_delete=models.CASCADE,blank=True,null=True)
class marklistTable(models.Model):
    studentid = models.ForeignKey(StudentTable, on_delete=models.CASCADE) 
    mark=models.IntegerField(null=True,blank=True)
    
class taskTable(models.Model):  
    facultyid=models.ForeignKey(facultyTable,on_delete=models.CASCADE)
    task=models.CharField(max_length=100, null=True,blank=True)

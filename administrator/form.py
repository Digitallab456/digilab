from django.forms import ModelForm

from administrator.models import *

class StudentForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['studentname','department','regno','phoneno','dob','address','semester']


class StudentForm_edit(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['studentname','department','regno','phoneno','dob','address','semester']


class facultyform(ModelForm):
    class Meta:
        model=facultyTable
        fields=['name','department','subject','qualification','phoneno']

class complaintform(ModelForm):
    class Meta:
        model=complaintTable
        fields= ['complaint','date','reply'] 

class Notification_form(ModelForm):
    class Meta:
        model = notificationTable
        fields = ['post']
# class registrationform(ModelForm):
#     class Meta:
#         model = fac_registrationTable
#         fields=['FirstName','LastName','Email','PhoneNumber','Department','BriefBiography','LOGINID']
class marklistForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['studentname','department','regno','phoneno','dob','address','semester']
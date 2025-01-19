from django.contrib import admin

from administrator.models import *

# Register your models here.
admin.site.register(logintable)
admin.site.register(StudentTable)
admin.site.register(facultyTable)
admin.site.register(complaintTable)
admin.site.register(Timetable)
admin.site.register(notificationTable)
admin.site.register(markupTable)


admin.site.register(taskTable)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(TimetableEntry)


from django.urls import path

from .views import *


urlpatterns = [
    # ///////////////////////////// admin ///////////////////////////////////////
    path("", LoginPage.as_view(), name="login"),
    path("addstudent", StudentPage.as_view(), name="addstudent"),
    path("add_faculty",FacultyPage.as_view(),name="add faculty"),
    path("complaint/<int:id>/", ComplaintPage.as_view(),name="complaint"),
    path("editstudent/<int:id>/", StudentEdit.as_view(),name="editstudent"),
    path("removestudent/<int:id>/", StudentRemove.as_view(),name="removestudent"),
    path("editfaculty/<int:id>/", facultyEdit.as_view(),name="editfaculty"),
    path("removefaculty/<int:id>/", facultyRemove.as_view(),name="removefaculty"),
    path("adminhome_page",Adminp.as_view(),name="admin_homepage"),
    path("timetable",Timep.as_view(),name="timetable"),
    path("student",stdp.as_view(),name="student"),
    path("reply",Reply.as_view(),name="reply"),
    path("faculty",Facpage.as_view(),name="faculty"),
    path("postnotification",notificationp.as_view(),name="notification"),
    # path("timetable",timetablep.as_view(),name="timetable"),
    path("insert_timetable/",insert_timetable.as_view(), name='insert_timetable'),
    path("logout",logout.as_view(), name='logout'),


    
    
    

    # //////////////////////////////faculty ////////////////////////////////////////

    path("editstudent", editpage.as_view(), name="edit student"),
    path("homepage", homepage.as_view(), name="faculty_homepage"),
    path("markupload", markupp.as_view(), name="mark_upload"),
    path("notification", notificationpage.as_view(), name="notification"),
    path("studentList", studentListp.as_view(), name="studentList"),
    path("fac_reg", regpage.as_view(), name="registration"),
    path("post", postcomplaintpage.as_view(), name="post"),
    path("marklist",marklistPage.as_view(), name="marklist"),
    path("logout",logout.as_view(), name='logout'),

   
   
    #//////////////////////////////student//////////////////////////////////////////
    path("postcomplaint", postcomplaintpage.as_view(), name="complaintpage"),
    path("studenthomepage", studpage.as_view(), name="homepage"),
    # path("timetbl", timetblpage.as_view(), name="timetbl"),
    #////////////////////////////// 
    
    


    
]



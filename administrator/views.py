from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View

from .form import *
from.models import *

# Create your views here.


# ///////////////////////////////////// admin////////////////////////////
class LoginPage(View):
    def get(self, request):
        return render(request, "admin/login_page.html")
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj=logintable.objects.get(username=username,password=password)
        request.session['user_id']=obj.id
        if obj.type=='admin':
            return HttpResponse('''<script>alert("welcome to home");window.location="adminhome_page"</script>''')
        elif obj.type=='faculty':
            return HttpResponse('''<script>alert("welcome to home");window.location="homepage"</script>''')
        

class logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert("logout successfully");window.location="/"</script>''')

        #     elif obj.type=='user':
        #         return render(request,'userdashboard.html')
        #     else:
        #         return HttpResponse("User type not recognized")
        # except logintable.DoesNotExit:
        #     messages.error(request,"invalid username or password")
        #     return redirect('login')
        
class StudentPage(View):
    def get(self,request):
        return render(request,"admin/addstudent.html")
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Done"); window.location="/"</script>''')
class StudentEdit(View):
    def get(self,request,id):
        obj=StudentTable.objects.get(id=id)
        return render(request,"admin/edit student.html",{'val':obj})
    def post(self,request,id):
        obj=StudentTable.objects.get(id=id)
        form=StudentForm_edit(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Done"); window.location="/student"</script>''')
class StudentRemove(View):
    def get(self, request, id):
        obj=logintable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Done"); window.location="/student"</script>''')


class FacultyPage(View):
    def get(self, request):
        return render(request,"admin/add faculty.html")
    def post(self,request):
        form=facultyform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Done"); window.location="/"</script>''')

class facultyEdit(View):
    def get(self, request,id):
        obj=facultyTable.objects.get(id=id)
        return render(request,"admin/edit faculty.html",{'val':obj})
    def post(self,request,id):
        obj=facultyTable.objects.get(id=id)
        form=facultyform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Done"); window.location="/faculty"</script>''')
               
class facultyRemove(View):
    def get(self, request, id):
        obj=logintable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Done"); window.location="/faculty"</script>''')


class ComplaintPage(View):
    def get(self, request, id):
        return render(request,"admin/complaint.html")

    def post(self,request,id):
        reply=request.POST['reply']
        obj=complaintTable.objects.get(id=id)
        obj.reply=reply
        obj.save()
        return HttpResponse('''<script>alert("Done");window.location="/reply"</script>''')

class Adminp(View):
    def get(self, request):
        return render(request,"admin/admin_homepage.html")

class Timep(View):
    def get(self,request):
        return render(request,"admin/timetable.html")
class stdp(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        return render(request,"admin/student.html",{'val':obj})
class Reply(View):
    def get(self,request):
        obj=complaintTable.objects.all()
        return render(request,"admin/complaint reply.html",{'val':obj})
    

class Facpage(View):
    def get(self,request):
        obj=facultyTable.objects.all()
        return render(request,"admin/faculty.html",{'val':obj})
    
    
class notificationp(View):
    def get(self,request):
        return render(request,"admin/post notification.html")
    def post(self,request):
        c= Notification_form(request.POST)
        if c.is_valid():
            c.save()
        return HttpResponse('''<script>alert("Done");window.location="/notification"</script>''')

        
   

class timetablep(View):
    def get(self,request):
        return render(request,"admin/timetable.html")
    



    
    
    
    
    #////////////////////////// faculty///////////////////////////
class editpage(View):
    def get(self,request):
        
        return render(request,"faculty/edit _student.html")
    
class homepage(View):
    def get(self,request):
        return render(request,"faculty/faculty_homepage.html")
    

class markupp(View):
    def get(self,request, id):
        obj = StudentTable.objects.filter(id=id)
        print(obj)
        c = facultyTable.objects.get(LOGIN__id = request.session['user_id'])
        return render(request,"faculty/mark_upload.html",{'val':obj, 'a':c})
    
    def post(self, request, id):
        k = marklistForm(request.POST)
        if k.is_valid():
            k.save()
            return HttpResponse('''<script>alert("mark added successfully");window.location="/marklist"</script>''')

    
class notificationpage(View):
    def get(self,request):
        c= notificationTable.objects.all()
        return render(request,"faculty/notification.html", {'a':c})

class studentListp(View):
    def get(self,request):
        c= StudentTable.objects.all() 
        return render(request,"faculty/student_ list.html",{'farhana':c})

class regpage(View):
    def get(self,request):
        return render(request,"faculty/registration.html")
    def post(self,request):
        form=facultyform(request.POST)
        if form.is_valid():
               login_instance=logintable.objects.create(
                   type='faculty',
                   username=request.POST['username'],
                   password=request.POST['password'],
               )
               reg_form=form.save(commit=False)
               reg_form.LOGIN=login_instance
               reg_form.save()
               return HttpResponse('''<script>alert("Registered successfully");window.location="/"</script>''')
class marklistPage(View):
    def get(self,request):
        c=StudentTable.objects.all()
        return render(request,"faculty/marklist.html",{'b':c})
  
class logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert("logout successfully");window.location="/"</script>''')

#///////////////////////////////////student////////////////////////////////////////////

class postcomplaintpage(View):
    def get(self,request):
        return render(request,"student/post.html")
class studpage(View):
    def get(self,request):
        return render(request,"student/student_homage.html")
class insert_timetable(View):
    def get(self,request):
        subjects = Subject.objects.all()
        teachers = Teacher.objects.all()
        classrooms = Class.objects.all()

        return render(request, 'admin/insert_timetable.html', {
            'subjects': subjects,
            'teachers': teachers,
            'classrooms': classrooms
        })
    

    # def post(self,request):
    #     subject_id = request.POST.get('subject')
    #     teacher_id = request.POST.get('teacher')
    #     classroom_id = request.POST.get('classroom')
    #     day_of_week = request.POST.get('day_of_week')
    #     time_slot = request.POST.get('time_slot')

    #     # Create a new TimetableEntry
    #     timetable_entry = TimetableEntry(
    #         subject_id=subject_id,
    #         teacher_id=teacher_id,
    #         classroom_id=classroom_id,
    #         day_of_week=day_of_week,
    #         time_slot=time_slot
    #     )
    #     timetable_entry.save()

    #     return redirect("/timetable")


    def post(self,request):
        subject_id = request.POST.get('subject')
        teacher_id = request.POST.get('teacher')
        classroom_id = request.POST.get('classroom')
        day_of_week = request.POST.get('day_of_week')
        time_slot = request.POST.get('time_slot')

        print(f"Subject: {subject_id}, Teacher: {teacher_id}, Classroom: {classroom_id}, Day: {day_of_week}, Time Slot: {time_slot}")


        # Create a new TimetableEntry
        timetable_entry = TimetableEntry(
            subject_id=subject_id,
            teacher_id=teacher_id,
            classroom_id=classroom_id,
            day_of_week=day_of_week,
            time_slot=time_slot
        )
        timetable_entry.save()

        return redirect("/timetable")



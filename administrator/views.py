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
        elif obj.type=='student':
            return HttpResponse('''<script>alert("welcome to Student home");window.location="studenthomepage"</script>''')
        



      
        #         return render(request,'userdashboard.html')
        #         else:
        #         return HttpResponse("User type not recognized")
        #         except logintable.DoesNotExit:
        #         messages.error(request,"invalid username or password")
                #    return redirect('login')
class logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert("logout successfully");window.location="/"</script>''')
        
class StudentPage(View):
    def get(self, request):
        return render(request, "admin/addstudent.html")

    def post(self, request):
        form1 = StudentForm(request.POST)
        
        if form1.is_valid():
            # Create a new logintable entry
            c = logintable.objects.create(
                username=request.POST.get('email'),
                password=request.POST.get('password'),
                type='student'
            )
            print(c)  # Log the created entry for debugging
            c.save()  # Save the logintable entry
            
            # Now, associate the created logintable entry with the StudentTable record
            student = form1.save(commit=False)  # Don't save to DB yet
            student.LOGINID = c  # Assign the logintable entry as LOGINID for the student
            
            # Save the student record
            student.save()

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
        obj=StudentTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Done"); window.location="/student"</script>''')


class FacultyPage(View):
    def get(self, request):
        return render(request,"admin/add faculty.html")
    def post(self, request):
        form1 = facultyform(request.POST)
        
        if form1.is_valid():
            # Create a new logintable entry
            c = logintable.objects.create(
                username=request.POST.get('email'),
                password=request.POST.get('password'),
                type='faculty'
            )
            print(c)  # Log the created entry for debugging
            c.save()  # Save the logintable entry
            
            # Now, associate the created logintable entry with the StudentTable record
            faculty = form1.save(commit=False)  # Don't save to DB yet
            faculty.LOGIN = c  # Assign the logintable entry as LOGINID for the student
            
            # Save the student record
            faculty.save()

        return HttpResponse('''<script>alert("Done"); window.location="/faculty"</script>''')

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

class stdp(View):
    def get(self,request):
        obj=StudentTable.objects.all()
        print(obj)
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

            
class select_class(View):
    def get(self, request):
        obj = Class.objects.all()
        return render(request, "admin/select_class.html", {'obj': obj})
                  
class manage_timetable(View):
    def post(self, request):
        class_id=request.POST['class_id']
        request.session['class_id']=class_id
        class_obj = Class.objects.get(id=class_id)
        subjects = Subject.objects.all()
        existing_days = Timetable.objects.filter(CLASS_id=class_obj).values_list('day', flat=True)
        all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        available_days = [day for day in all_days if day not in existing_days]
        return render(request, 'admin/manage_timetable.html', {'subjects': subjects,'available_days': available_days})

class add_timetable_action(View):
    def post(self, request):
        day = request.POST['day']
        slot_9_10 = request.POST['slot_9_10']
        slot_10_11 = request.POST['slot_10_11']
        slot_11_12 = request.POST['slot_11_12']
        slot_1_2 = request.POST['slot_1_2']
        slot_2_3 = request.POST['slot_2_3']
        slot_3_4 = request.POST['slot_3_4']
        obj = Timetable()
        obj.CLASS=Class.objects.get(id=request.session['class_id'])
        obj.day =day
        obj.slot_9_10=Subject.objects.get(id=slot_9_10)
        obj.slot_10_11=Subject.objects.get(id=slot_10_11)
        obj.slot_11_12=Subject.objects.get(id=slot_11_12)
        obj.slot_1_2=Subject.objects.get(id=slot_1_2)
        obj.slot_2_3=Subject.objects.get(id=slot_2_3)
        obj.slot_3_4=Subject.objects.get(id=slot_3_4)
        obj.save()
        return HttpResponse('''<script>alert("successfully added");window.location="/select_class#about"</script>''')
        
    
class select_class1(View):
    def get(self, request):
        obj = Class.objects.all()
        return render(request, "admin/select_class1.html", {'obj': obj})
                  
class view_timetable(View):
    def post(self, request):
        class_id=request.POST['class_id']
        # Query all timetable entries from the database
        timetable_entries = Timetable.objects.filter(CLASS_id=class_id).order_by('day')
        # Render the timetable in a template
        return render(request, 'admin/timetable.html', {'timetable_entries': timetable_entries})  
      #////////////////////////// faculty///////////////////////////
class editpage(View):
    def get(self,request):
        
        return render(request,"faculty/edit _student.html")
    
class homepage(View):
    def get(self,request):
        return render(request,"faculty/faculty_homepage.html")
    

class markupp(View):
    def get(self,request, id):
        obj = StudentTable.objects.filter(id=id).first()
        print(obj)
        c = facultyTable.objects.get(LOGIN__id = request.session['user_id'])
        return render(request,"faculty/mark_upload.html",{'obj':obj, 'a':c})
    
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
    def get(self, request):
        print("Entered the view function")  #
        c= StudentTable.objects.all 
        print(c)
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
    def get(self, request):
        # Retrieve all students
        students = StudentTable.objects.all()

        # Get the related marks for each student (if they exist)
        for student in students:
            mark_entry = markupTable.objects.filter(STUDENT=student).first()  # Assuming one entry per student
            if mark_entry:
                student.mark = mark_entry.mark  # Assign mark to student object
            else:
                student.mark = None  # If no marks are found

        return render(request, "faculty/marklist.html", {'students': students})

  
class logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert("logout successfully");window.location="/"</script>''')
class viewcomplaint(View):
    def get(self,request):
        return render(request,"faculty/f_reply.html")
    
class task(View):
   def get(self,request):
        c = facultyTable.objects.get(LOGIN__id = request.session['user_id'])
        return render(request,"faculty/task.html", {'s':c})
   def post(self, request):
       d = TaskForm(request.POST)
       if d.is_valid():
           d.save()
           return HttpResponse('''<script>alert("task added successfully");window.location="/task"</script>''')

class taskman(View):
    def get(self,request):
        c = taskTable.objects.filter(facultyid__LOGIN_id=request.session['user_id'])
        return render(request,"faculty/taskMan.html",{'a':c})


class postcomplaintpage(View):
    def get(self,request):
        c = logintable.objects.get(id=request.session['user_id'])
        return render(request,"faculty/post.html",{'z':c})
    def post(self, request):
       d = cForm(request.POST)
       if d.is_valid():
           d.save()
           return HttpResponse('''<script>alert("complaint added successfully");window.location="/"</script>''')

    

#///////////////////////////////////student////////////////////////////////////////////

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
    

class TaskListView(View):
    def get(self, request):
        # Fetch all tasks (or filter by faculty if needed)
        tasks = taskTable.objects.all()  # You can add filters to show tasks by specific faculty or by date
        return render(request, "student/taskview.html", {'tasks': tasks})
class Taskanswerupload(View):
    def get(self, request,):
        return render(request, "student/taskansupload.html")
    def post(self, request,id):
      task=taskTable.objects.get(id=id)
      k=answer(request.POST,instance=task)
      if k.is_valid():
           k.save()
           return HttpResponse('''<script>alert("complaint added successfully");window.location="/"</script>''')
     

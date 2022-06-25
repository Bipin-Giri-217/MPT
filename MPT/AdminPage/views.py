from audioop import reverse
import genericpath
from typing import Generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from accounts.models import StudentProfile, User, MentorProfile, StudentDetails, StudentHobbies,GuardianDetails,StudentExtraCurricular,StudentMedicalReport
# from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from EditUser.views import studentcontext

# student dashboard view
@login_required
def student(request, pk):
    if request.user.is_authenticated and not(request.user.is_staff):
        user = User.objects.get(usr_id=pk)
        student=StudentProfile.objects.get(user=user)
        context={'user':user,'student':student} 
        try:
            details=StudentDetails.objects.get(student_id=student.id)
            hobbies=StudentHobbies.objects.get(student_id=student.id)
            guardian=GuardianDetails.objects.get(student_id=student.id)
            Medical=StudentMedicalReport.objects.get(student_id=student.id)
            extraCurr=StudentExtraCurricular.objects.get(student_id=student.id)
            achievements=[i for i in extraCurr.achievements.split(',')]
            clubs=[i for i in extraCurr.clubs.split(',')]
            hobbies=[i for i in hobbies.hobby.split(',')]
            organizations=[i for i in extraCurr.organization.split(',')]
            context = {'student' : student,'details':details,'hobbies':hobbies,'guardian':guardian,'clubs':clubs,'hobbies':hobbies,'achievements':achievements,'orgs':organizations,'Medical':Medical}
        except:
            pass
        return render(request, 'student-dashboard.html', context)

# Create your views here for admin page

@login_required
def Adminpage(request):
    if request.user.is_superuser:
        users = User.objects.all()
        context = {'users': users} 
        return render(request,'AdminPage/admin-user.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

# view all the students in the database in the admin page
@login_required
def Adminstudent(request):
    if request.user.is_superuser:
        students = User.objects.filter(is_staff=False)
        context = {'users': students} 
        return render(request,'AdminPage/admin-student.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Adminmentor(request):
    if request.user.is_superuser:
        mentors = User.objects.filter(is_staff=True,is_superuser=False)
        context = {'users': mentors} 
        return render(request,'AdminPage/admin-mentor.html',context)
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def Activity(request):
    if request.user.is_superuser:
        return render(request,'AdminPage/admin-activities.html')
    else:
        return HttpResponse("You are not authorized to view this page")

@login_required
def deleteuser(request,id):
    if request.user.is_superuser:
        if request.method=='POST':
            # User.objects.filter(pk=id).delete()
            user=User.objects.get(pk=id)
            check=user.is_staff
            user.delete()
            if check:
                return redirect('admin-mentor')
            else:
                return redirect('admin-student')

    return HttpResponse("You are not authorized to view this page")

@login_required
def updateuserprofile(request,usr_id):
    if request.user.is_superuser:
        user=User.objects.get(usr_id=usr_id)
        context={'user':user}
        if not user.is_staff:
            profile = StudentProfile.objects.get(user__usr_id=usr_id)
            details,created=StudentDetails.objects.get_or_create(student_id=profile.id)
            hobbies,created=StudentHobbies.objects.get_or_create(student_id=profile.id)
            guardian,created=GuardianDetails.objects.get_or_create(student_id=profile.id)
            extraCurr,created=StudentExtraCurricular.objects.get_or_create(student_id=profile.id)
            Medical,created=StudentMedicalReport.objects.get_or_create(student_id=profile.id)
            context.update({
                'student': profile,
                'pk': request.user.usr_id,
                'details':details,
                'hobbies':hobbies,
                'guardian':guardian,
                'extraCurr':extraCurr,
                'Medical':Medical})
            context.update(studentcontext)
            if request.method=='POST':
                fName = request.POST['fName']
                Lname = request.POST['lName']
                Mname = request.POST['mName']
                stuid = request.POST['sId']
                Addr = request.POST['Address']
                religion = request.POST['Religion']
                motherTongue = request.POST['mTongue']
                phone = request.POST['phone']
                try:
                    if request.POST['rNo'] :
                        Rno=request.POST['rNo']
                        details.current_rollNo=Rno
                except:
                    pass
                try:
                    if request.POST['dept'] :
                        department = request.POST['dept']
                        profile.Branch = department
                except:
                    pass
                try:
                    if request.POST['year'] :
                        year = request.POST['year']
                        details.current_year = year
                except:
                    pass
                try:
                    if request.POST['blood_group']:
                        blood_group = request.POST['blood_group']
                        profile.Blood_grp = blood_group
                except:
                    pass
                try:
                    if request.POST['gender']:
                        gender = request.POST['gender']
                        profile.Gender = gender
                except:
                    pass
                try:
                    if request.POST['dob']:
                        DateofBirth = request.POST['dob']
                        profile.DateofBirth = DateofBirth
                except:
                    pass
                try:
                    if request.POST['Yoa']:
                        yearOfAdd = request.POST['Yoa']
                        details.YearOfAdmission = yearOfAdd
                except:
                    pass

                # guardian info
                FatherName = request.POST['FatherName']
                MotherName = request.POST['MotherName']
                try:
                    if request.POST['Fqualification']:
                        Fqualif= request.POST['Fqualification']
                        guardian.fatherHighestEducation=Fqualif
                except:
                    pass
                try:
                    if request.POST['Mqualification']:
                        Mqualif= request.POST['Mqualification']
                        guardian.motherHighestEducation=Mqualif
                except:
                    pass
                try:
                    if request.POST['Foccup']:
                        Foccupation= request.POST['Foccup']
                        guardian.fatherOccupation=Foccupation
                except:
                    pass
                try:
                    if request.POST['Moccup']:
                        Moccupation= request.POST['Moccup']
                        guardian.motherOccupation=Moccupation
                except:
                    pass
                try:
                    if request.POST['income']:
                        income= request.POST['income']
                        guardian.yearlyIncome=income
                except:
                    pass

                guardian.father_name=FatherName
                guardian.mother_name=MotherName

                # health info
                addiction= request.POST['addiction']
                illness= request.POST['illness']
                phobia= request.POST['phobia']
                treatment= request.POST['treatment']
                Medical.addiction=addiction
                Medical.illness=illness
                Medical.phobia=phobia
                Medical.treatment=treatment
                
                #Goals, Hobbies, Extra Curricular Activities
                aim= request.POST['aim']
                hobbie= request.POST['hobby']
                ReasonForEngg= request.POST['ReasonForEngg']
                Achievements= request.POST['achievements']
                clubs= request.POST['clubs']
                orgs= request.POST['orgs']

                details.reason_of_engg=ReasonForEngg
                details.AimOfLife=aim
                extraCurr.clubs=clubs
                extraCurr.achievements=Achievements
                extraCurr.organization=orgs
                hobbies.hobby=hobbie

                # user = User.objects.get(usr_id=stu_id)
                try:
                    if 'profileImg' in request.FILES:
                        profile_img = request.FILES['profileImg']
                        # if user already has profile image then delete it
                        if str(user.profile_img) != 'logo.png':
                            user.profile_img.delete()
                        user.profile_img = profile_img
                except:
                    pass
                user.first_name = fName
                user.usr_id= stuid
                user.middle_name=Mname
                user.last_name = Lname
                user.phone = phone
                user.save()

                profile.Address= Addr
                profile.religion = religion
                profile.mother_tongue = motherTongue
                details.save()
                profile.save()
                guardian.save()
                hobbies.save()
                extraCurr.save()
                Medical.save()
                return redirect('admin-student')
            return render(request, 'AdminPage/admin-student-edit.html', context)
        
        elif user.is_staff and not user.is_superuser:
            profile = MentorProfile.objects.get(user__usr_id=usr_id)
            context = {
                'department_list': [
                    'Computer Engineering',
                    'Electronics and Telecommunication Engineering',
                    'Information Technology',
                    'Mechanical Engineering'
                ],
                'bloodGroup_list': [
                    'A+',
                    'A-',
                    'B+',
                    'B-',
                    'AB+',
                    'AB-',
                    'O+',
                    'O-'
                ],
                'profile': profile,
                'user':user
            }

            if request.method == "POST":
                fName = request.POST['fName']
                Lname = request.POST['lName']
                Mname = request.POST['mName']
                motherTongue = request.POST['mTongue']
                religion = request.POST['Religion']
                phone = request.POST['phone']
                State = request.POST['state']
                Country = request.POST['country']
                Addr = request.POST['Address']
                Qualification = request.POST['Quali']
                Teacherid = request.POST['usr_id']
                city= request.POST['city']
                try:
                    if request.POST['dept'] :
                        department = request.POST['dept']
                        profile.Branch = department
                except:
                    pass
                try:
                    if request.POST['blood_group']:
                        blood_group = request.POST['blood_group']
                        profile.Blood_grp = blood_group
                except:
                    pass
                try:
                    if request.POST['gender']:
                        gender = request.POST['gender']
                        profile.Gender = gender
                except:
                    pass
                try:
                    if request.POST['dob']:
                        DateofBirth = request.POST['dob']
                        profile.DateofBirth = DateofBirth
                except:
                    pass

                try:
                    if request.POST['doj']:
                        DateofJoining= request.POST['doj']
                        profile.DateofJoining = DateofJoining
                except:
                    pass

                try:
                    if 'profileImg' in request.FILES:
                        profile_img = request.FILES['profileImg']
                        # if user already has profile image then delete it
                        if str(user.profile_img) != 'logo.png':
                            user.profile_img.delete()
                        user.profile_img = profile_img
                except:
                    pass
            
                user.first_name = fName
                user.usr_id= Teacherid
                user.middle_name=Mname
                user.last_name = Lname
                user.phone = phone
                user.save()
                
                profile.City = city
                profile.qualification= Qualification
                profile.State = State
                profile.Address= Addr
                profile.Country= Country
                profile.mother_tongue = motherTongue
                profile.religion = religion
                profile.save()
                return redirect('admin-mentor')
            return render(request, 'AdminPage/admin-mentor-edit.html', context)

        else:
            return HttpResponse(" You are Admin ")
    else:
        return HttpResponse("You are not authorized to view this page")
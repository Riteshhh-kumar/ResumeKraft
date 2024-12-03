from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,letter
from ResumeKraft.models import * 

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from . import template1,template2
from io import BytesIO

tempt=template1
@login_required
def chooseTemplate(request):
    if request.method =="POST":
        global tempt
        tempt=eval(request.POST.get("template1"))
        print(tempt)

        return render(request,"details.html")
    return render(request,"details.html")
    

@login_required
def createResume(request):    
    buffer = BytesIO()
    canv = []
    doc = SimpleDocTemplate(buffer,pagesize=letter)
    global tempt
    
    if request.method == "POST":
        name = request.POST.get("name")
        mail = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        p = Personal(email=request.user.email,name=request.user.first_name,lanme=request.user.last_name,phone=phone,address=address)
        p.save()
        canv = tempt.heading(name,canv)
        canv = tempt.contactInfo(str(address)+' | '+str(mail)+' | '+str(phone),canv)   

        
        if request.POST.get("aboutme")!="":
            canv = tempt.sectionTitle("About Me",canv)
            about = str(request.POST.get("aboutme"))
            a = AboutMe(email=request.user.email,about_me=about)
            a.save()
            aboutme = about.splitlines()
            for i in aboutme:
                canv = tempt.sectionContent(i,canv)
                   
        x=0


        school10 = request.POST.get("school10th")
        school12 = request.POST.get("school12th")
        score10 = request.POST.get("score10th")
        score12 = request.POST.get("score12th")
        ugcourse = request.POST.get("ugcourse")
        ugcollege = request.POST.get("ugcollege")
        ugscore = request.POST.get("ugscore")

        pgcourse = request.POST.get("pgcourse")
        pgcollege = request.POST.get("pgcollege")
        pgscore = request.POST.get("pgscore")
        canv = tempt.sectionTitle("Education",canv)
        e = Education(email=request.user.email,school_10th=school10,school_12th=school12,score_10th=score10,score_12th=score12,UG_college=ugcollege,UG_course=ugcourse,score_UG=ugscore)

        if request.POST.get("pgcollege")!=None:
            canv = tempt.sectionContent(pgcollege,canv)
            canv = tempt.twoColumn('       '+pgcourse,pgscore+" CGPA",canv)
            e.PG_coollege=pgcollege
            e.PG_course=pgcourse
            e.score_PG=pgscore
        e.save()
        
        
        canv = tempt.educationalInformation('       '+school10,'       '+school12,score10,score12,ugcollege,'       '+ugcourse,ugscore,canv)

        if request.POST.get("company0")!="":
            canv = tempt.sectionTitle("Experiences",canv)
            try:
                while request.POST.get("company"+str(x))!=None:
                    company = request.POST.get("company"+str(x))
                    start = str(request.POST.get("startdate"+str(x))).replace("-",'/')
                    end = str(request.POST.get("enddate"+str(x))).replace("-",'/')
                    role = request.POST.get("role"+str(x))
                    desc = str(request.POST.get("description"+str(x)))
                    desclist = desc.splitlines()
                    ex = Experience(email=request.user.email,company_name=company,job_role=role,start_date=start,end_date=end,decription=desc)
                    ex.save()
                    canv = tempt.subSection(str(company),canv)
                    canv = tempt.twoColumn(role,start+"-"+end,canv)
                    for i in desclist:
                        canv = tempt.sectionContent('* '+i,canv)
                    x=x+1
                x=0
            except:
                x=0

        if request.POST.get("projectname0")!="":
            canv = tempt.sectionTitle("Projects",canv)
            try:
                while request.POST.get("projectname"+str(x))!=None:
                    projectname = request.POST.get("projectname"+str(x))
                    desc = str(request.POST.get("projectdesc"+str(x)))
                    desclist = desc.splitlines()
                    pr = Projects(email=request.user.email,project_name=projectname,project_description=desc)
                    pr.save()
                    canv = tempt.subSection(str(projectname),canv)
                    for i in desclist:
                        canv = tempt.sectionContent('* '+i,canv)                    
                    x=x+1
                x=0
            except:
                x=0
        
        
        if request.POST.get("skill0")!="":
            canv = tempt.sectionTitle("Skills",canv)
            try:
                while request.POST.get("skill"+str(x))!=None:
                    skill = request.POST.get("skill"+str(x))
                    s = Skills(email=request.user.email,skill_name=skill)
                    s.save()
                    canv = tempt.sectionContent('* '+str(skill),canv)
                    x=x+1
                x=0
            except:
                x=0
        
        if request.POST.get("achievement0")!="":
            canv = tempt.sectionTitle("Achievements",canv)
            try:
                while request.POST.get("achievement"+str(x))!=None:
                    achieve = request.POST.get("achievement"+str(x))
                    ac = Achievements(email=request.user.email,achievement=achieve)
                    ac.save()
                    canv = tempt.sectionContent('* '+str(achieve),canv)
                    x=x+1
                x=0
            except:
                x=0
        if request.POST.get("lang0")!="":
            canv = tempt.sectionTitle("Languages",canv)
            try:
                while request.POST.get("lang"+str(x))!=None:
                    lang = request.POST.get("lang"+str(x))
                    l = Languages(email=request.user.email,language=lang)
                    l.save()
                    canv = tempt.sectionContent('* '+str(lang),canv)
                    x=x+1
                x=0
            except:
                x=0

        if request.POST.get("socialname0")!="":
            canv = tempt.sectionTitle("Socials",canv)
            try:
                while request.POST.get("socialname"+str(x))!=None:
                    socailname = request.POST.get("socialname"+str(x))
                    socaillink = request.POST.get("sociallink"+str(x))
                    so = SocailLinks(email=request.user.email,link_name=socailname,link=socaillink)
                    so.save()
                    canv = tempt.twoColumn(socailname,socaillink,canv)
                    x=x+1
                x=0
            except:
               pass
        t = Template(email=request.user.email,template_id=tempt)

        try:        
            doc.build(canv)
            
            # Get the value from the buffer
            pdf = buffer.getvalue()
            buffer.close()

            # Create an HTTP response with PDF content
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] =  'inline;filename=mypdf.pdf'
            response.write(pdf)
            return response
        
        except:
            # Prepare the response with the correct content type
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] =  'inline;filename=mypdf.pdf'
            

            return response
    
    else:
        return render(request,"index.html")
    


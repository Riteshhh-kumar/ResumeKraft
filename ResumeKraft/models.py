from django.db import models

class Personal(models.Model):
    # id = models.BigAutoField(primary_key=True)
    email=models.CharField(max_length=50,default="",primary_key=True)
    name=models.CharField(max_length=50,default="")
    lanme=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    school_10th=models.CharField(max_length=50,null=True,default="")
    school_12th=models.CharField(max_length=50,null=True,default="")
    score_10th=models.CharField(max_length=50,null=True,default="")
    score_12th=models.CharField(max_length=50,null=True,default="")
    
    UG_college=models.CharField(max_length=50,null=True,default="")
    UG_course=models.CharField(max_length=50,null=True,default="")
    score_UG=models.CharField(max_length=50,null=True,default="")
    PG_coollege=models.CharField(max_length=50,null=True,default="")
    PG_course=models.CharField(max_length=50,null=True,default="")
    score_PG=models.CharField(max_length=50,null=True,default="")
    def __str__(self):
        return self.name

class Skills(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    skill_name=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Projects(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    project_name=models.CharField(max_length=50,default="")
    project_description=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Achievements(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="",)
    achievement=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Experience(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    company_name=models.CharField(max_length=50,default="")
    job_role=models.CharField(max_length=50,default="")
    start_date=models.CharField(max_length=50,default="")
    end_date=models.CharField(max_length=50,default="")
    decription=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.name

class Template(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    template_name=models.CharField(max_length=50,default="")
    template_id=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class SocailLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    link_name=models.CharField(max_length=50,default="")
    link=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class AboutMe(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    about_me=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.name

class Languages(models.Model):
    id = models.BigAutoField(primary_key=True)
    email= models.CharField(max_length=30,null=True,default="")
    language=models.CharField(max_length=20,default="")
    def __str__(self):
        return self.name


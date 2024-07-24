from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name="학수번호", max_length=15, unique = True)
    name = models.CharField(verbose_name="과목명", max_length=40)
    grade = models.CharField(verbose_name="학년", max_length=10, default="0")
    credit = models.DecimalField(verbose_name="학점", max_digits=2, decimal_places=1, default= 0.0)
    professor = models.CharField(verbose_name="담당교수", max_length=10, default="담당교수 미정")
    remarks = models.CharField(verbose_name="비고", max_length=10, default="")
    vacancy = models.CharField(verbose_name="여석", max_length=200, default="미정")
    time_and_classroom = models.CharField(verbose_name="시간 및 강의실", max_length=200, default="미정")
    major_name = models.CharField(verbose_name="전공 이름", max_length=20, default="미정")
    evaluation_method = models.CharField(verbose_name="평가방식", max_length=10, default="미정")
    subject = models.CharField(verbose_name="과목구분", max_length=5, default="미정")
    
    def __str__(self):
        return self.code + "/" + self.name

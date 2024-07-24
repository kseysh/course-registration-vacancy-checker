from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name="학수번호", max_length=15, unique = True)
    name = models.CharField(verbose_name="과목명", max_length=40)
    grade = models.CharField(verbose_name="학년", max_length=10, default="0")
    credit = models.DecimalField(verbose_name="학점", max_digits=2, decimal_places=1, default= 0.0)
    classroom = models.CharField(verbose_name="강의실", max_length=256, default="")
    professor = models.CharField(verbose_name="담당교수", max_length=10, default="담당교수 미정")
    remarks = models.CharField(verbose_name="비고", max_length=10, default="")
    vacancy = models.CharField(verbose_name="여석", max_length=200, default="미정")
    major_name = models.CharField(verbose_name="전공 이름", max_length=20, default="미정")

    evaluation_method_type = [
    ('절대평가', 'ABSOLUTE'),
    ('상대평가', 'RELATIVE'),
    ('미정', 'UNDETERMINED'),
    ]
    evaluation_method = models.CharField(verbose_name="평가방식", choices=evaluation_method_type, max_length=10, default="미정")

    day_of_weeks_choices = [
    ('교양선택', 'GENERAL_ELECTIVE'),
    ('교양필수', 'GENERAL_REQUIRED'),
    ('전공선택', 'MAJOR_ELECTIVE'),
    ('전공필수', 'MAJOR_REQUIRED'),
    ('미정', 'UNDETERMINED'),
    ]
    subject = models.CharField(verbose_name="과목구분", choices=day_of_weeks_choices, max_length=5, default="미정")
    
    def __str__(self):
        return self.name

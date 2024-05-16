from django.db import models

class Subject(models.Model):
    subject = models.CharField(verbose_name="과목구분 id", max_length=4, default="정보 없음")

class Major(models.Model):
    name = models.CharField(verbose_name="학부 전공", max_length=20, default="전공")

class CourseTime(models.Model):
    day_of_weeks_choices = [
    ('월', 'MONDAY'),
    ('화', 'TUESDAY'),
    ('수', 'WEDNESDAY'),
    ('목', 'THURSDAY'),
    ('금', 'FRIDAY'),
    ('토', 'SATURDAY'),
    ('일', 'SUNDAY')
]
    day_of_week = models.CharField(verbose_name="강의 요일", choices= day_of_weeks_choices, max_length=8, default="?")
    period = models.SmallIntegerField(verbose_name="교시")

class Course(models.Model):
    code = models.CharField(verbose_name="학수번호", max_length=15, unique = True)
    name = models.CharField(verbose_name="과목명", max_length=40)
    grade = models.CharField(verbose_name="학년", max_length=10, default="0")
    credit = models.DecimalField(verbose_name="학점", max_digits=2, decimal_places=1, default= 0.0)
    
    time = models.CharField(verbose_name="시간", max_length=256, default="")
    classroom = models.CharField(verbose_name="강의실", max_length=256, default="")
    professor = models.CharField(verbose_name="담당교수", max_length=10, default="담당교수 미정")
    evaluation_method = models.CharField(verbose_name="평가방식", max_length=10, default="")
    remarks = models.CharField(verbose_name="비고", max_length=10, default="")

    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)
    course_time = models.ManyToManyField(CourseTime)

    enrollment_count = models.IntegerField(verbose_name="신청 인원수", default=0)
    enrollment_capacity = models.IntegerField(verbose_name="신청 정원", default=0)    

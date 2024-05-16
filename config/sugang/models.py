from django.db import models

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    day_of_weeks_choices = [
    ('교양선택', 'GENERAL_ELECTIVE'),
    ('교양필수', 'GENERAL_REQUIRED'),
    ('전공선택', 'MAJOR_ELECTIVE'),
    ('전공필수', 'MAJOR_REQUIRED'),
    ('미정', 'UNDETERMINED'),
    ]
    subject = models.CharField(verbose_name="과목구분 id", max_length=4, default ="미정")

    def __str__(self):
        return self.subject

class Major(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="학부 전공", max_length=20, default="전공")

    def __str__(self):
        return self.name

class CourseTime(models.Model):
    id = models.AutoField(primary_key=True)
    day_of_weeks_choices = [
    ('월', 'MONDAY'),
    ('화', 'TUESDAY'),
    ('수', 'WEDNESDAY'),
    ('목', 'THURSDAY'),
    ('금', 'FRIDAY'),
    ('토', 'SATURDAY'),
    ('일', 'SUNDAY'),
    ('미정', 'UNDETERMINED'),
    ]
    day_of_week = models.CharField(verbose_name="강의 요일", choices= day_of_weeks_choices, max_length=8, default="미정")
    period = models.SmallIntegerField(verbose_name="교시", default=0)

    def __str__(self):
        return self.day_of_week + "요일 " + str(self.period) + "교시"

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(verbose_name="학수번호", max_length=15, unique = True)
    name = models.CharField(verbose_name="과목명", max_length=40)
    grade = models.CharField(verbose_name="학년", max_length=10, default="0")
    credit = models.DecimalField(verbose_name="학점", max_digits=2, decimal_places=1, default= 0.0)
    
    evaluation_method_type = [
    ('절대평가', 'ABSOLUTE'),
    ('상대평가', 'RELATIVE'),
    ('미정', 'UNDETERMINED'),
    ]

    classroom = models.CharField(verbose_name="강의실", max_length=256, default="")
    professor = models.CharField(verbose_name="담당교수", max_length=10, default="담당교수 미정")
    evaluation_method = models.CharField(verbose_name="평가방식", choices=evaluation_method_type, max_length=10, default="미정")
    remarks = models.CharField(verbose_name="비고", max_length=10, default="")

    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)
    course_time = models.ManyToManyField(CourseTime)

    enrollment_count = models.IntegerField(verbose_name="신청 인원수", default=0)
    enrollment_capacity = models.IntegerField(verbose_name="신청 정원", default=0)    

    def __str__(self):
        return self.name

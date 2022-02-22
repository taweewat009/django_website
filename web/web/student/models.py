from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Grade(models.Model):
    grade_list = (('4','4'),
                  ('3.5','3.5'),
                  ('3','3'),
                  ('2.5','2.5'),
                  ('2','2'),
                  ('1.5','1.5'),
                  ('1','1'),
                  ('0','0'),)
    
    subject_list = (
        ('วิทยาการคำนวณ','วิทยาการคำนวณ'),
        ('คอมพิวเตอร์พื้นฐาน','คอมพิวเตอร์พื้นฐาน'),
    )
    
    card_id  = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100,choices=subject_list)
    score = IntegerField()
    Grade = models.CharField(max_length=50,choices=grade_list)
    
    def __str__(self):
        return self.name

# ฐานข้อมูล ม.1
class Grade7(models.Model):
    
    card_id  = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    subject1 = models.CharField(max_length=100)
    subject2 = models.CharField(max_length=100)
    # วิทยาการคำนวณ
    comsci_score = IntegerField()
    comsci_Grade = models.CharField(max_length=50)
    # การออกแบบและเทคโนโลยี
    tech_score = IntegerField()
    tech_Grade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
# ฐานข้อมูล ม.2
class Grade8(models.Model):
    
    card_id  = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    subject1 = models.CharField(max_length=100)
    subject2 = models.CharField(max_length=100)
    # วิทยาการคำนวณ
    comsci_score = IntegerField()
    comsci_Grade = models.CharField(max_length=50)
    # การออกแบบและเทคโนโลยี
    tech_score = IntegerField()
    tech_Grade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

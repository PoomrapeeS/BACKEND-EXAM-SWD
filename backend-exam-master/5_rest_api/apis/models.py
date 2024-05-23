from django.db import models


# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=250, unique=True)
    abbreviation = models.CharField(max_length=10)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def classroom_count(self):
        return self.classroom_set.count()

    def teacher_count(self):
        return self.teacher_set.count()

    def student_count(self):
        return self.student_set.count()


class Classroom(models.Model):
    year = models.CharField(max_length=2)
    room = models.CharField(max_length=3)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["school", "year", "room"]

    def __str__(self):
        return f"{self.school}: {self.year}/{self.room}"

    def teachers(self):
        return [str(teacher) for teacher in self.teacher_set.all()]

    def students(self):
        return [str(student) for student in self.student_set.all()]


class Teacher(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    classroom = models.ManyToManyField(Classroom, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["name", "surname"]

    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["name", "surname"]

    def __str__(self):
        return f"{self.name} {self.surname}"

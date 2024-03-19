from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username


class Register(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    uname = models.CharField(max_length=15, blank=False, default="xyz")
    password = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=50, blank=False)

    class Meta:
        db_table = "register_table"

    def __str__(self):
        return self.name


class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    tourcode = models.CharField(max_length=10, blank=False, unique=True)
    tourname = models.CharField(max_length=30, blank=False)
    tourpackage = models.CharField(max_length=30, blank=False)
    desc = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = "package_table"

    def __str__(self):
        return self.tourname

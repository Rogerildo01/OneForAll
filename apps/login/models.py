# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class LoginTb(models.Model):
    id_login = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    id_loja = models.IntegerField(blank=True, null=True)
    id_cargo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_tb'
       

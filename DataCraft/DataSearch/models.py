from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
import datetime
from .search import PublishserDataIndex

class Client(models.Model):
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Publisher', 'Publisher'),
        ('Consumer', 'Consumer'),
    )

    DEPARTMENT_TYPE = (
        ('1', 'IT'),
        ('2', 'Engineering'),
        ('3', 'Enterprise Analytics'),
        ('4', 'CGSO')
    )
    first_name = models.CharField(max_length = 200, null = True, blank = True, verbose_name = "First Name")
    last_name = models.CharField(max_length  = 200, null = True, blank = True, verbose_name = "Last Name")
    # phone_number = models.CharField(max_length = 256, null = True, blank = True, verbose_name = "Phone Number")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name ="User")
    user_role= models.CharField(max_length=200 ,choices = USER_TYPE, default = '---', null=True, blank=True, verbose_name='User Role')
    department= models.CharField(max_length=200 ,choices = DEPARTMENT_TYPE, default = '---',null=True, blank=True, verbose_name='Departmnet Type')
    super_consumer=models.BooleanField(default=False, blank=True )
    
    def __str__(self):
        return str(self.first_name)


class Department(models.Model):
    name = models.CharField(max_length=225, verbose_name="Department_name")
    def __str__(self):
        return str(self.name)

class SubDepartment(models.Model):
    
    name = models.CharField(max_length=225,verbose_name="Sub_department")
    code=models.CharField(max_length=225,verbose_name='Code_values',null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='department', null=True, blank=True, related_name='department')
    def __str__(self):
            return "%s"%(self.name)

class PublishserData(models.Model):

    DATA_CLASIFICATION_TYPE = (
            ('Public', 'Public'),
            ('Sensitive', 'Sensitive'),
            ('Protected', 'Protected'),
        )

    CATEGORY_TYPE=(
            ('Members', 'Members'),
            ('Providers', 'Providers'),
            ('Claims', 'Claims'),
            ('Care Management', 'Care Management'),
            ('Employers', ' Employers'),
            ('Agents', 'Agents'),
            ('Plans', 'Plans'),
            ('Customer Service', 'Customer Service')
        )

    DATA_CHANGE_TYPE=(

            ('Not updated (historical only)', 'Not updated (historical only)'),
            ('As needed','As needed'),
            ('Annually','Annually'),
            ('Bi-annually','Bi-annually'),
            ('Quarterly', 'Quarterly'),
            ('Bi-monthly', 'Bi-monthly'),
            ('Monthly', 'Monthly'),
            ('Bi-weekly', 'Bi-weekly'),
            ('Weekly', 'Weekly'),
            ('Daily', 'Daily'),
            ('Hourly', 'Hourly'),
            ('Multiple times hourly', 'Multiple times hourly'),
            ('Streaming', 'Streaming'),
        )
    AUTOMATED_FASHION_CHOICES=(

            ('Yes', 'Yes'),
            ('No', 'No'),
            ('Unsure', 'Unsure')
        )

    DATASET_CHOICES=(
            ('API connect','API connect'),
            ('Hadoop','Hadoop'),
            ('EDW','EDW'),
            ('Reltio','Reltio'),
            ('EODS','EODS'),
            ('Other','Other')

        )

    publisher=models.ForeignKey(Client, on_delete=models.CASCADE,related_name="publisher" ,blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='department_id', null=True, blank=True, related_name='department_id')
    subdepartment = models.ForeignKey(SubDepartment, on_delete=models.CASCADE, null= True ,blank=True, verbose_name ='sub_department_id', related_name='sub_department_id')
    inventory_ID = models.CharField(max_length = 1000, null= True ,blank=True,verbose_name = "inventory_ID")
    title=models.CharField(max_length = 500, verbose_name = "title")
    description=models.CharField(max_length = 1000, verbose_name = "description")
    data_classification=models.CharField(max_length=200 ,choices = DATA_CLASIFICATION_TYPE, verbose_name='data_classification')
    category =models.CharField(max_length=200 ,choices = CATEGORY_TYPE, null=True, blank=True, verbose_name='category_type')
    data_change_frequency=models.CharField(max_length=200 ,choices = DATA_CHANGE_TYPE, verbose_name='data_change_frequency ')
    automated_fashion=models.CharField(max_length=200, choices=AUTOMATED_FASHION_CHOICES,verbose_name='Automated_Fashion')
    dataset_come_from=models.CharField(max_length=200, choices=DATASET_CHOICES,verbose_name='Sataset_Come_From')
    automation_option=models.BooleanField(default=False )
    
    api_endpoint = models.CharField(max_length = 200, null= True ,blank=True,verbose_name = "API_Endpoint")
    
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True, blank=True)
    data_classification_comments=models.CharField(max_length=500, verbose_name='classification_comment',null=True, blank=True,)
    def __str__(self):
            return "%s%s%s"%(self.title,self.category,self.inventory_ID)

    def indexing(self):
       obj = PublishserDataIndex(
          meta={'id': self.id},
          publisher=self.publisher.first_name,
          department=self.department.name if self.department else '',
          subdepartment=self.subdepartment.name,
          inventory_ID=self.inventory_ID,
          title=self.title,
          description=self.description,
          data_classification=self.data_classification,
          category=self.category,
          data_change_frequency=self.data_change_frequency,
          automated_fashion=self.automated_fashion,
          dataset_come_from=self.dataset_come_from, 
          api_endpoint=self.api_endpoint,
          automation_option=self.automation_option,
          data_classification_comments=self.data_classification_comments,
       )
       obj.save(index='publishserdata-index')
       return obj.to_dict(include_meta=True)
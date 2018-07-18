from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory, modelformset_factory

from DataSearch.models import Client,PublishserData,Department,SubDepartment


class ClientSignupForm(forms.ModelForm):
    """
    it is a user model form when user type client it will create user in user model as a client.
    """
    user_role = forms.ChoiceField(label="User Type", choices=())
    department = forms.ChoiceField(label="Department Type Type", choices=())

    reenter_password = password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(ClientSignupForm, self).__init__(*args, **kwargs)
        self.fields['user_role'].choices = (    
                                                ('Select Provider','Select Provider'),
                                                ('Admin', 'Admin'),
                                                ('Publisher', 'Publisher'),
                                                ('Consumer', 'Consumer'),
                                            )

        self.fields['department'].choices=(
                                    ('Select Department','Select Department'),
                                    ('1', 'IT'),
                                    ('2', 'Engineering'),
                                    ('3', 'Enterprise Analytics'),
                                    ('4', 'CGSO')
                                )

        self.fields['first_name'].required = False
        self.fields['last_name'].required = False


    def save(self,commit=True):
        """
            By this save method we create user and make a relationship with contact model and secoud depend on conatc type. 
        """
        instance = super(ClientSignupForm, self).save(commit=False)
        if commit:
            instance.username = self.cleaned_data['email']
            instance.is_active = False
            instance.save()
            contact = Client.objects.create(first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'],
                                            user_role=self.cleaned_data['user_role'],
                                            department=self.cleaned_data['department'],
                                            user=instance)
        return instance
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','reenter_password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = Client
        fields=("first_name","last_name","user_role","department")


class PublishserDataForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        super(PublishserDataForm, self).__init__(*args, **kwargs)
    
        self.fields['title'].required = True
        self.fields['description'].required = True
        self.fields['data_classification'].required = True
        self.fields['category'].required = True   
        self.fields['data_change_frequency'].required = True
        self.fields['automated_fashion'].required = True
        self.fields['dataset_come_from'].required = True   
        self.fields['automation_option'].required = True
        self.fields['inventory_ID'].required=True
        self.fields['upload'].required = False   
        self.fields['data_classification_comments'].required = False
        self.fields['api_endpoint'].required=True


        self.fields['data_classification'].choices = (

                    ('',''),                    
                    ('Public', 'Public'),
                    ('Sensitive', 'Sensitive'),
                    ('Protected', 'Protected'),
                                        )
        self.fields['category'].choices = (

                    ('',''),                    
                    ('Members', 'Members'),
                    ('Providers', 'Providers'),
                    ('Claims', 'Claims'),
                    ('Care Management', 'Care Management'),
                    ('Employers', ' Employers'),
                    ('Agents', 'Agents'),
                    ('Plans', 'Plans'),
                    ('Customer Service', 'Customer Service')
                )
        self.fields['data_change_frequency'].choices = (
            
                    ('',''),                    
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

        self.fields['automated_fashion'].choices =  (
                    ('Yes', 'Yes'),
                    ('No', 'No'),
                    ('Unsure', 'Unsure')
                )  

        self.fields['dataset_come_from'].choices = (
                    ('API connect','API connect'),
                    ('Hadoop','Hadoop'),
                    ('EDW','EDW'),
                    ('Reltio','Reltio'),
                    ('EODS','EODS'),
                    ('Other','Other')
                ) 
    class Meta:
        model = PublishserData
        fields = (
                    'title','description','department',
                    'data_classification','subdepartment',
                    'category','data_change_frequency',
                    'automated_fashion','dataset_come_from',
                    'automation_option','inventory_ID','api_endpoint',
                    'upload','data_classification_comments'
                )
        widgets = {
        # 'contact_type':forms.RadioSelect,
        # 'freelancer_type':forms.RadioSelect,
        'automated_fashion':forms.RadioSelect,
        'dataset_come_from':forms.RadioSelect,
        'description':forms.Textarea,
        # 'required_time':forms.RadioSelect,
             }


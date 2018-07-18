from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.models import Site
from .tasks import send_varification_email,welcome_note
from .models import Client

def show_list(userlist):
    """"
    """
    user_data=[]
    for user in userlist:
        client=Client.objects.get(user=user)
        if client:
            user_data.append({
                'id':client.id,
                'is_active':user.is_active,
                'is_staff':user.is_staff if client else'',
                'first_name':client.first_name if client else '',
                'last_name':client.last_name if client else '',
                'department':client.get_department_display() if client else'',
                'user_role':client.user_role if client else '',
                'email':user.email,
                })
    return user_data

def show_client_list(userlist):
    """
    """
    user_data=[]
    for user in userlist:
            user_data.append({
                'id':user.id,
                'is_active':user.user.is_active,
                'is_staff':user.user.is_staff if user else'',
                'first_name':user.first_name if user else '',
                'last_name':user.last_name if user else '',
                'department':user.get_department_display() if user else'',
                'user_role':user.user_role if user else '',
                'email':user.user.email,
                })
    return user_data


def show_consumer_list(userlist):
    """
    """
    user_data=[]
    for user in userlist:
            user_data.append({
                'id':user.id,
                'is_active':user.user.is_active,
                'is_staff':user.user.is_staff if user else'',
                'first_name':user.first_name if user else '',
                'last_name':user.last_name if user else '',
                'department':user.get_department_display() if user else'',
                'user_role':user.user_role if user else '',
                'email':user.user.email,
                'Super_consumer':user.super_consumer if user else '',
                })
    return user_data


def user_role(user):
    """
    """
    import pdb; pdb.set_trace()
    try:
        client = user.client
    except Exception as e:
        contact = ""
    if client:
        return client.user_role
    return ""
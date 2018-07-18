from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from django.contrib.sites.models import Site
from DataSearch.models import Client,PublishserData


@receiver(post_save, sender=PublishserData)
def index_data(sender, instance, **kwargs):
    print ('Signal working properly')
    instance.indexing()




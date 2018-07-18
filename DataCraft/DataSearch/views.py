import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django import template
from django.contrib.auth import get_user_model
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Client,Department,SubDepartment,PublishserData
from .forms import ClientSignupForm,ClientProfileForm,PublishserDataForm
from .tasks import send_varification_email,welcome_note,success_full
from .utils import user_role,show_list,show_client_list,show_consumer_list
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import login_required
from DataSearch.search import *
from elasticsearch_dsl.query import MultiMatch, Match
# DRF import here
from rest_framework import generics
from rest_framework.generics import CreateAPIView,  ListAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from .serializers import DataCatalogSerializer,SubDepartmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route, list_route
from django.shortcuts import get_list_or_404, get_object_or_404
# from rest_framework.pagination import PaginationSerializer

#get all Publisher data
class DataCatalog(generics.ListCreateAPIView):
    # serializer_class = SittingSerializer

    queryset = models.PublishserData.objects.all()
    serializer_class = serializers.DataCatalogSerializer
    # paginate_by = 4
    # paginate_by_param = 'page_size'
    # max_paginate_by = 100

#Retrive perticular data
class DetailDataCatalog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PublishserData.objects.all()
    serializer_class = serializers.DataCatalogSerializer

# Get subdepartment accoding to department
class SubDepartmentViewSet(viewsets.ViewSet):
    serializers_class= serializers.SubDepartmentSerializer
    model = SubDepartment
    def create(self,request):
        publisher_data = SubDepartment.objects.filter(department=request.data['department'])
        serializer = SubDepartmentSerializer(publisher_data, many=True)
        return Response(serializer.data)

#Get Department data
class SubDepartmentCodeViewSet(viewsets.ViewSet):
    serializers_class= serializers.SubDepartmentSerializer
    model = SubDepartment
    def create(self,request):
        publisher_data = SubDepartment.objects.filter(id=request.data['id'])
        serializer = SubDepartmentSerializer(publisher_data, many=True)
        return Response(serializer.data)

#Save Publihser data 
class PublishDataViewSet(viewsets.ViewSet):
    serializers_class= serializers.DataCatalogSerializer
    model = PublishserData
    
    def create(self, request):
        serializer = self.serializers_class(data=request.data)
        import pdb; pdb.set_trace()
        if serializer.is_valid(raise_exception=True):
            serializer.save(publisher=Client.objects.all()[0])
            return Response({
               "status": '200',
               "success" : True,
               "message" : "Successfully Data Saved",
              } )
    def retrieve(self,request,pk):
        publisher_data = PublishserData.objects.all()
        publisher_data = get_object_or_404(publisher_data, pk=pk)
        serializer = DataCatalogSerializer(publisher_data)
        return Response(serializer.data)

    def list(self,request):
        publisher_data=PublishserData.objects.all()
        serializer = DataCatalogSerializer(publisher_data, many=True)
        return Response(serializer.data)

class SearchViewSet(viewsets.ViewSet):
    serializers_class= serializers.DataCatalogSerializer
    model = PublishserData
    
    def create(self, request):
        d_list=[]
        data={}
        data=request.data
        data=search(title=data['query'].lower())
        if data:
            for out in data:
                title=out.title
                description=out.description
                d_id=out.meta.id
                d_list.append({
                    'id':d_id,
                    'title':title,
                    'description':description,
                    })
            return Response({
               "status": '200',
               "success" : True,
               "data" : d_list,
              } )
        return Response({
               "status": '402',
               "success" : False,
               "data" : 'Data Not Found',
              } )




def index(request):
    return render(request,"index.html")

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        try:
            try:
                user=User.objects.get(email=username,password=password)
            except:
                user=authenticate(email=username, password=password)
            if user is not None:
                if user.is_active and user.is_staff:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    redirect_to = settings.LOGIN_REDIRECT_URL
                    return redirect(redirect_to)
                else:
                    return HttpResponseRedirect(reverse('account_login'))
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponseRedirect(reverse('account_login'))
        except:
            return HttpResponseRedirect(reverse('account_login'))    
    else:
        return HttpResponseRedirect(reverse('account_login'))

def account_signup(request):
    """
    This function to SingUp user
    """
    if request.method == "POST":
        form = ClientSignupForm(request.POST) 
        user_exist = User.objects.filter(username=request.POST['email']).exists()
        if not user_exist:
            if form.is_valid():
                user=form.save()
                site=Site.objects.filter(id=1)
                email=user.email
                domain = site[0].domain
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.id))
                subject ="Conform your email address "
                message = render_to_string('EmailTemplates/Email_verification.html', {
                    'email':user.email,
                    'link': "{0}{1}{2}/{3}/".format(domain, "/validate/", uid.decode("utf-8"), token),
                    'user_display':user.first_name,
                    'domain':"{0}".format(domain),
                     })
                send_varification_email.delay(subject, message, email)
                messages.add_message(request, 
                    messages.SUCCESS, 'Successfully sigin up.we sent verification mail on your email id.please verify your email address')
                return HttpResponseRedirect(reverse('account_login'))
            
            return render(request, 'DataSearch/sign_up.html', {'form':form})
        # messages.error(request, 'User all ready exists.')    
        return render(request, 'DataSearch/sign_up.html', {'form':form})

    form = ClientSignupForm()
    return render(request, 'DataSearch/sign_up.html', {'form':form})

@login_required
def home(request):
    '''
    User Profile pages
    '''
    return render(request, 'DataSearch/home.html')

from django.contrib.auth.decorators import user_passes_test
@user_passes_test(lambda u: u.is_superuser)
def userlist(request):
    return render(request, 'DataSearch/user_list.html')
    

def validate(request, uidb64, token):
    templates_data = ""
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        try:
            user_model = get_user_model()
            user = user_model.objects.get(pk=uid)
            if default_token_generator.check_token(user, token) and user.is_active == 0:
                user.is_active = True
                user.save()
                site = Site.objects.filter(id=1),
                domain = site[0],
                subject = "Welcome Email",
                message = render_to_string('EmailTemplates/welcome_email.html', {
                        'email':user.email,
                        'user_display':user.first_name,
                        'link': "{0}{1}".format(domain,"/accounts/login/"),
                        'domain':"{0}".format(domain[0][0]),
                        })
                welcome_note.delay(subject, message, user.email)
                return HttpResponseRedirect(reverse('account_login'))
        except:
            pass
    return HttpResponseRedirect(reverse('account_login'))


@login_required
def all_userlist(request):
    '''
     show user list
    '''
    user_list = []
    user_data = {}
    userlist=User.objects.filter(is_staff=False).filter(is_active=True).filter(is_superuser=False)
    if userlist:
        user_list=show_list(userlist)
        user_data = {'data':list(user_list)}
        return HttpResponse(json.dumps(user_data), content_type='application/json' )
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")


@login_required
def delete_user(request,user_id):
    '''
       Delete Perticular user
    '''
    user_list = []
    user_data = {}
    if user_id:
        try:
            user=Client.objects.get(id=user_id).user
            user.delete()
            userlist=User.objects.filter(is_staff=False).filter(is_active=True)
            if userlist:
                user_list=show_list(userlist)
                user_data = {'data':list(user_list), 'status':'success'}
                return HttpResponse(json.dumps(user_data) ,content_type='application/json' )
            user_data = {'data':list(user_list), 'status':'success'}
            return HttpResponse(json.dumps(user_data) ,content_type='application/json' )
        except Exception as e:
            pass
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")


@login_required
def validate_user(request,user_id):
    user_list = []
    user_data = {}
    if user_id:
        try:
            user=Client.objects.get(id=user_id).user
            user.is_staff=True
            user.save()
            site = Site.objects.filter(id=1),
            domain = site[0],
            subject = "Welcome to Blue DataCraft",
            message = render_to_string('EmailTemplates/UserRole.html', {
                    'email':user.email,
                    'user_display':user.first_name,
                    'link': "{0}{1}".format(domain,"/accounts/login/"),
                    'domain':"{0}".format(domain[0][0]),
                    })
            success_full.delay(subject, message, user.email)
            userlist=User.objects.filter(is_staff=False).filter(is_active=True)
            if userlist:
                user_list=show_list(userlist)
                user_data = {'data':list(user_list), 'status':'success'}
                return HttpResponse(json.dumps(user_data), content_type='application/json' )
            user_data = {'data':list(user_list),'status':'success'}
            return HttpResponse(json.dumps(user_data),content_type="application/json")
        except:
            pass
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")


@login_required
def user_role(request):
    user_list = []
    user_data = {}
    user_role=request.GET.get('user_role')
    user_id=request.GET.get('id')
    if user_role and user_id:
        try:
            user=Client.objects.get(id=user_id)
            user.user_role=user_role
            user.save()
            userlist=User.objects.filter(is_staff=False).filter(is_active=True)
            if userlist:
                user_list=show_list(userlist)
                user_data = {'data':list(user_list), 'status':'success'}
                return HttpResponse(json.dumps(user_data), content_type='application/json' )
            user_data = {'data':list(user_list), 'status':'success'}
            return HttpResponse(json.dumps(user_data),content_type="application/json")
        except:
            user_data = {'message':'Data not found','status':403}
            return HttpResponse(json.dumps(user_data),content_type="application/json")
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")



@login_required
def all_admin(request):
     return render(request, 'DataSearch/Show-all-admin.html')


@login_required
def show_all_admin(request):
    user_list = []
    user_data = {}
    userlist=Client.objects.filter(user_role='Admin')
    if userlist:
        user_list=show_client_list(userlist)
        user_data = {'data':list(user_list)}
        return HttpResponse(json.dumps(user_data), content_type='application/json' )
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")

@login_required
def delete_admin(request,user_id):
    user_list = []
    user_data = {}
    if user_id:
        try:
            admin=Client.objects.get(id=user_id).user
            admin.delete()
            userlist=Client.objects.filter(user_role='Admin')
            user_list=show_client_list(userlist)
            user_data = {'data':list(user_list),'status':'success'}
            return HttpResponse(json.dumps(user_data), content_type='application/json' )
        except Exception as e:
            pass
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")


@login_required
def publisher(request):
     return render(request, 'DataSearch/Show-all-publisher.html')

@login_required
def show_all_publisher(request):
    user_list = []
    user_data = {}
    userlist=Client.objects.filter(user_role='Publisher')
    if userlist:
        user_list=show_client_list(userlist)
        user_data = {'data':list(user_list)}
        return HttpResponse(json.dumps(user_data), content_type='application/json' )
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")

@login_required
def consumer(request):
     return render(request, 'DataSearch/Show-all-consumer.html')

@login_required
def show_all_consumer(request):
    user_list = []
    user_data = {}
    userlist=Client.objects.filter(user_role='Consumer')
    if userlist:
        user_list=show_consumer_list(userlist)
        user_data = {'data':list(user_list)}
        return HttpResponse(json.dumps(user_data), content_type='application/json' )
    user_data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(user_data),content_type="application/json")

@login_required
def manage_consumer(request):
    '''
     Manage super conuser
    '''
    consumer_type=request.GET['parameter']
    consumer_id=request.GET['id']
    if consumer_type and consumer_id:
        client=Client.objects.filter(id=consumer_id)
        if client:
            client=client[0]
            if consumer_type == 'false':
                 client.super_consumer=True
            else:
                 client.super_consumer=False
            client.save()
            data = {'status':'success'}
            return HttpResponse(json.dumps(data),content_type="application/json")
    data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(data),content_type="application/json") 

###################################################################
#                 Start Working to Result page                    #
###################################################################

@login_required
def search_result(request):
    """
    """
    if request.method=="POST":
        data=search(title=request.POST['data'].lower())
        return render(request, 'DataSearch/ResultSetpage.html',{ 'data': data })
 
    data_list=PublishserData.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(data_list, 5)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request, 'DataSearch/ResultSetpage.html',{ 'data': data })



@login_required
def publisher_form (request):
    """
    """
    try:
        user = request.user.client.user_role=='Consumer'
    except:
        user = None
    if user is not True:
        if request.method == "POST":
            form = PublishserDataForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit = False)
                data.publisher = request.user.client
                data = data.save()
                messages.success(request, 'Data Published Successfully')
                return HttpResponseRedirect(reverse('publisher_form'))
            form=PublishserDataForm()
            return render(request,'DataSearch/Publisher-data.html',{'form' :form})
        form=PublishserDataForm()
        return render(request,'DataSearch/Publisher-data.html',{'form' :form})
    return render(request, 'DataSearch/ResultSetpage.html')


@login_required
def get_sub_department(request,d_id):
    """
    Show all subdepartment name
    """
    sub_list=[]
    data={}
    if d_id:
        subdepartment=SubDepartment.objects.filter(department=d_id)
        if subdepartment:
            for subdepartment in subdepartment:
                sub_list.append({
                    'id':subdepartment.id,
                    'name':subdepartment.name
                    })
            data = {'data':list(sub_list),'status':'success'}
            return HttpResponse(json.dumps(data),content_type="application/json")
    data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(data),content_type="application/json")

@login_required
def get_sub_department_code(request,d_id):
    if d_id:
        subdepartment=SubDepartment.objects.filter(id=d_id)
        data={'code':subdepartment[0].code,'status':'success'}
        return HttpResponse(json.dumps(data),content_type="application/json")
    data={'message':'Data not fount','status':403}
    return HttpResponse(json.dumps(data),content_type="application/json")

@login_required
def searching(request):
    """
    Basic Searching
    """
    d_list=[]
    data={}
    val=request.GET['val'].lower()
    pdata=search(title=val)
    if pdata:
        for out in pdata:
            title=out.title
            description=out.description
            d_id=out.meta.id
            d_list.append({
                'id':d_id,
                'title':title,
                'description':description,
                })
        data = {'data':list(d_list),'status':'success'}
        return HttpResponse(json.dumps(data),content_type="application/json")
    data = {'message':'Data not found','status':403}
    return HttpResponse(json.dumps(data),content_type="application/json")

@login_required
def service_data(request,d_id):
    if d_id:
        pdata=PublishserData.objects.filter(id=d_id)
        return render(request, 'DataSearch/Servicepage.html',{'data':pdata[0]})



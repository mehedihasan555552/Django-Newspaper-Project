from django.shortcuts import render,redirect
from . models import *
from django.views.generic import  DetailView
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
now = timezone.now()


def index(request):
    header=[]

    l=LatestPost.objects.filter(header=True).filter(published__lte=now).distinct().order_by('-date_posted')[:1]
    ll=LatestPost.objects.filter(published__lte=now).distinct().order_by('-date_posted')[1:3]
   
    posts =LatestPost.objects.filter(published__lte=now).distinct().order_by('date_posted').reverse()

    


    try:
        query = request.GET.get('Q')
        if query:
            posts =LatestPost.filter(published__lte=now).filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()

    except:
        pass

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result)==1:
        print('User exits')
    elif len(result)>1:
        print('User exits more ..')
    else:
        u.save()
        print("User is Unique.")
    count = User.objects.all().count()
    print('Total user is',count)

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page',1)
    posts=paginator.get_page(page_number)


    context={'posts':posts,'l':l,'ll':ll,'count':count,'paginator':paginator,'page_number':page_number}
    return render(request, 'base/index1.html',context)


def Programing(request):
    category=['1']
    posts=LatestPost.objects.filter(published__lte=now).distinct().order_by('-date_posted').filter(category=category)

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page',1)
    posts=paginator.get_page(page_number)

    context={'posts':posts,'paginator':paginator,'page_number':page_number}
    return render(request, 'base/gas.html',context)





def Tech(request):
    category=['2']
    posts=LatestPost.objects.filter(published__lte=now).distinct().order_by('-date_posted').filter(category=category)
   

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page',1)
    posts=paginator.get_page(page_number)

    context={'posts':posts,'paginator':paginator,'page_number':page_number}
    return render(request, 'base/gas.html',context)


def International(request):
    category=['3']
    posts=LatestPost.objects.filter(published__lte=now).distinct().order_by('-date_posted').filter(category=category)
   

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page',1)
    posts=paginator.get_page(page_number)

    context={'posts':posts,'paginator':paginator,'page_number':page_number}
    return render(request, 'base/gas.html',context)


def IT(request):
    category=['5']
    posts=LatestPost.objects.filter(published__lte=now).distinct().order_by('-date_posted').filter(category=category)
    

    paginator = Paginator(posts,10)
    page_number = request.GET.get('page',1)
    posts=paginator.get_page(page_number)

    context={'posts':posts,'paginator':paginator,'page_number':page_number}
    return render(request, 'base/gas.html',context)

class LatestPostt(DetailView):
    model = LatestPost



def Search(request):
	query = request.GET['query']
	title = LatestPost.objects.filter(title__icontains=query)
	content = LatestPost.objects.filter(content__icontains=query)
	posts = title.union(content)
	context = {'posts':posts}
	return render(request,'base/search.html', context)




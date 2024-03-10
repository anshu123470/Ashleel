from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from django.http import HttpResponse

# def robots_txt(request):
#     lines = [
#         "User-Agent: *",
#         "Disallow: /admin/",  # Example rule, adjust as needed
#         # Add more rules here as needed
#     ]
#     return HttpResponse("\n".join(lines), content_type="text/plain")

def index(request):
    vdata = Video.objects.all()
    paginator = Paginator(vdata, 2)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')

    try:
        ServicesDatafinal = paginator.get_page(page_number)  # returns the desired page object
        total = ServicesDatafinal.paginator.num_pages
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        ServicesDatafinal = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page'
        ServicesDatafinal = paginator.page(paginator.num_pages)
    data = {
        'cd': vdata,
        'ServicesData': ServicesDatafinal,
        'totalpagelist': [n + 1 for n in range(total)]
    }
    return render(request, 'app/index.html', data)

def playpage(request,slug):
    last_10_data = Video.objects.order_by('-id')[:10]
    pp= Video.objects.get(slug_v=slug)
    return render(request,'app/video.html',{'ap':pp,'last_10_data': last_10_data})

def photo(request):
    photo=Photo.objects.all()
    paginator = Paginator(photo, 2)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')

    try:
        ServicesDatafinal = paginator.get_page(page_number)  # returns the desired page object
        total = ServicesDatafinal.paginator.num_pages
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        ServicesDatafinal = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page'
        ServicesDatafinal = paginator.page(paginator.num_pages)
    data = {
        'p': photo,
        'ServicesData': ServicesDatafinal,
        'totalpagelist': [n + 1 for n in range(total)]
    }
    return render(request,'app/photo.html',data)

def search(request):
    query = request.GET.get("query")
    if len(query)>80:
        qs = Video.objects.none()
    else:
        video = Video.objects.all()
        qs = video.filter(titel__icontains = query)

    return render(request,'app/search.html',{'a':qs,'query':query})


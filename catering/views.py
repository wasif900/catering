from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse  # new
from django.http import JsonResponse
from .models import Service, gigs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import ImageForm
from django.db.models.query import QuerySet


def index(request):  # new

    if request.method == 'POST':

        request.session['uname'] = request.POST.get('name', '')
        request.session['uuname'] = request.POST.get('uname', '')
        request.session['uemail'] = request.POST.get('email', '')
        request.session['upnumber'] = request.POST.get('pnumber', '')
        request.session['upassword'] = request.POST.get('password', '')

        return redirect('register2')

    return render(request, 'register.html')


def register2(request):  # new
    print(request.session['uname'])

    if request.method == 'POST':

        request.session['service_country'] = request.POST.get(
            'service_country')
        request.session['service_city'] = request.POST.get('service_city')
        request.session['service_area'] = request.POST.get('service_area')
        return redirect('register3')

    return render(request, 'register2.html')


def register3(request):  # new
    if request.method == 'POST':
        service = Service(ser_prov_name=request.session['uname'],  ser_prov_username=request.session['uuname'], ser_prov_email_address=request.session['uemail'],  ser_prov_phone_number=request.session['upnumber'],
                          ser_prov_password=request.session['upassword'], ser_prov_service_country=request.session['service_country'], ser_prov_service_city=request.session['service_city'], ser_prov_service_area=request.session['service_area'])
        service.save()

        nuser = User.objects.create_user(
            request.session['uname'],  request.session['uemail'],  request.session['upassword'])
        nuser.save()
        print(nuser)
        print("usr created")
        return redirect('loginPage')

    return render(request, 'register3.html')


def loginPage(request):  # new
    if request.method == "POST":
        email1 = request.POST.get('email', '')
        password1 = request.POST.get('password', '')

        user = authenticate(request, username=email1, password=password1)
        print("outside")
        if user is not None:
            login(request, user)

            messages.success(request, "logged in")
            return redirect('home')
        else:

            messages.error(request, "sorry")

    return render(request, 'loginPage.html')


def home(request):
    print("hello")
    username = 'none'
    username = request.user.username
    return render(request, 'home.html', {'username': username})


def logoutuser(request):
    logout(request)
    username = 'none'
    return render(request, 'home.html', {'username': username})


def sellergig(request):
    all_gigs = gigs.objects.filter(gig_user=request.user.username)
    # print(len(all_gigs))

    return render(request, 'sellerGig.html', {"all_gigs": all_gigs})


def createNewGig(request):
   
   
    if request.method == "POST":
        
        request.session['gigtitle'] = request.POST.get(
            'gigtitle')
        request.session['gigcategory'] = request.POST.get(
            'gigcategory')
        request.session['gigsubcategory'] = request.POST.get(
            'gigsubcategory')
        request.session['gigkeywords'] = request.POST.get(
            'gigkeywords')

        return redirect('gigPricing')

    return render(request, 'CreateNewGig.html')


def gigPricing(request):
   
    if request.method == "POST":
       
        request.session['packagenameb'] = request.POST.get(
            'packagenameb')
        print(request.session['packagenameb'])
        request.session['packagenames'] = request.POST.get(
            'packagenames')
        print(request.POST.get(
            'packagenames'))
        request.session['packagenamep'] = request.POST.get(
            'packagenamep')
        request.session['packagedb'] = request.POST.get(
            'packagedb')
        request.session['packageds'] = request.POST.get(
            'packageds')
        request.session['packagedp'] = request.POST.get(
            'packagedp')
        request.session['packagerevisionsb'] = request.POST.get(
            'packagerevisionsb')
       
        request.session['packagerevisionss'] = request.POST.get(
            'packagerevisionss')
        request.session['packagerevisionsp'] = request.POST.get(
            'packagerevisionsp')
        request.session['packagecity'] = request.POST.get(
            'packagerevisionsp')
      
        request.session['packageprices'] = request.POST.get(
            'packageprices')
        request.session['packagepricep'] = request.POST.get(
            'packagepricep')
        print(request.POST.get(
            'packagepricep'))
        return redirect('gigDescription')
    return render(request, 'gigPricing.html')


def gigDescription(request):
    if request.method == "POST":
        request.session['gigdesc'] = request.POST.get(
            'gigdescq')

        return redirect('gigGallery')

    return render(request, 'gigDescription.html')


def gigGallery(request):
    current_user = Service.objects.filter(ser_prov_username=request.user.username)
   
    for i in current_user:
        cuur_city = i.ser_prov_service_city
        cuur_area = i.ser_prov_service_area
    print("dbhsjabfhjsabfhjds")
    if request.method == "POST":
        imageform = ImageForm(request.POST, request.FILES)

        if imageform.is_valid():
            imageform.save()

            print("hellonjnkjnkjkj")

        gig = gigs(gig_title=request.session['gigtitle'], gig_category=request.session['gigcategory'], gig_sub_category=request.session['gigsubcategory'], gig_search_tags=request.session['gigkeywords'], gig_package_detail_basic_name=" ", gig_package_detail_standard_name="", gig_package_detail_premium_name="", gig_package_detail_basic_detail='', gig_package_detail_standard_detail='', gig_package_detail_premium_detail="", gig_package_detail_basic_delivery_time=request.session['packagerevisionsb'], gig_package_detail_standard_delivery_time=request.session['packagerevisionsb'], gig_package_detail_premium_delivery_time=request.session['packagerevisionsb'], gig_package_detail_basic_price='',
        gig_package_detail_standard_price='', gig_package_detail_premium_price='',  gig_package_details='', gig_city =  cuur_city ,gig_country =  cuur_area, gig1_image=imageform.cleaned_data['gig1_image'], gig2_image=imageform.cleaned_data['gig2_image'], gig3_image=imageform.cleaned_data['gig3_image'], gig_user=request.user.username)
        gig.save()
        return redirect('home')
    else:
       form = ImageForm()

       return render(request, 'gigGallery.html', {"imageform": form})


def search(request):
     print("uff allpost11")
     query = request.POST.get('search')
   
    #  print(request.session['searchquery'])
     if query == None:
         print("if")
         gigcity= gigs.objects.filter(gig_city__icontains= request.session['searchcity'])
         gigarea= gigs.objects.filter(gig_country__icontains=request.session['searcharea'])
         print( gigcity)
         print(gigarea)
       
         if (len(gigcity)>0 and len(gigarea)>0 ):
              
              allPosts  =   gigcity.intersection( gigarea)
              print('allpost')
              print(allPosts)
             
        
         return render(request, 'search.html', {'allPosts': allPosts})
         
     else:
       if   len(query)>78:
          allPosts=gigs.objects.none()
       else:
          gigTitle= gigs.objects.filter(gig_title__icontains=query)
          gigCat= gigs.objects.filter(gig_category__icontains=query)
          gigSuCat =gigs.objects.filter(gig_sub_category__icontains=query)
          gigSearchTag = gigs.objects.filter(gig_search_tags__icontains=query)

          allPosts =   gigTitle.union( gigCat, gigSuCat,gigSearchTag)
       if allPosts.count()==0:
          print("uff")
          messages.warning(request, "No search results found. Please refine your query.")
     print("uff allpost")
     return render(request, 'search.html', {'allPosts': allPosts})


def searchPage(request):
       print("hello ites main search")
       if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
          request.session['searchcountry'] = request.POST.get('country')
          request.session['searchcity'] = request.POST.get('city')
          request.session['searcharea'] = request.POST.get('area')
          request.session['searchquery'] = request.POST.get('searchquery')
          print(request.session['searcharea'])

        # Perform any necessary logic with the input values

        # Return a JSON response if needed
          return JsonResponse({'success': True})

    # Return an error response if the request is not valid
       return JsonResponse({'success': False}, status=400)


 
   

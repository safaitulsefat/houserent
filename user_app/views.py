import os
import time

from django.db.models import Q

from account.models import NewUser
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404

from .models import OwnerRent, Sell_flat, Sell_land,VehicleOwner

# Create your views here.

# this "identifyUser" view identyfies whether the user is a land owner or a normal user.
# after identifying the user type it redirects the user to it's corresponding route.


def identifyUser(request):
    if request.user.is_authenticated:
        if request.user.is_land_owner:
            return redirect('/dashboard/owner-home')
        elif request.user.is_furniture_delivery :
            return redirect('/dashboard/furniture-home')
        else:
            return redirect('/dashboard/user-home')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')

# belows views handles the normal user routes

def userAccount(request) :
        return render(request, "OwnerDashboard/userAccount.html")

def userDashboard(request):
    if request.user.is_authenticated:
        if not request.user.is_land_owner:
            my_post=OwnerRent.objects.all()
            all_Sell_flat=Sell_flat.objects.all()
            Sell_land_flat=Sell_land.objects.all()
            vh_post=VehicleOwner.objects.all()

            context={
                'allpost':my_post,
                'all_Sell_flat':all_Sell_flat,
                'Sell_land':Sell_land_flat,
                'vehiclepost':vh_post,
            } 
            return render(request, "TenantDashboard/user_base.html",context)
        else:
            return render(request, 'UserDashboard/unauthorized_user.html')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')


def userBuy(request):
    return render(request, "TenantDashboard/user_buy.html")


def userShow(request):
    return render(request, "TenantDashboard/user_sell.html")


def userRent(request):
    return render(request, "TenantDashboard/user_rent.html")


# belows views handles the property owners route

def ownerDashboard(request):
    if request.user.is_authenticated:
        if request.user.is_land_owner:
    
            my_post=OwnerRent.objects.all()
            all_Sell_flat=Sell_flat.objects.all()
            Sell_land_flat=Sell_land.objects.all()
            vh_post=VehicleOwner.objects.all()

            context={
                'allpost':my_post,
                'all_Sell_flat':all_Sell_flat,
                'Sell_land':Sell_land_flat,
                'vehiclepost':vh_post,
            } 
            return render(request, "OwnerDashboard/owner_base.html",context)
        else:
          return render(request, 'UserDashboard/unauthorized_user.html')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')

def furnituredashboard(request):
    if request.user.is_authenticated:
        if request.user.is_furniture_delivery:
            vh_post=VehicleOwner.objects.all()
            

            context={
                'vehiclepost':vh_post,
                
            } 
            return render(request, "furniture/furniture_base.html",context)
        else:
          return render(request, 'UserDashboard/unauthorized_user.html')
    else:
        return render(request, 'UserDashboard/unauthorized_user.html')


def ownerBuy(request):
    return render(request, "OwnerDashboard/owner_buy.html")




def ownerSellFlat(request):
    if request.user.is_authenticated and request.method == "POST":
        get_method = request.POST.copy()
        property_type = request.POST.get("property_type")
        divission = get_method.get("divission")
        district = get_method.get("district")
        location = get_method.get("location")
        price = get_method.get("price")
        ammount = get_method.get("ammount")
        floors_count = get_method.get("floors_count")
        floor_face = get_method.get("floor_face")
        details = get_method.get("details")
        flat_image = request.FILES["photo_url"]

        flat_data = Sell_flat(property_type=property_type, divission=divission, district=district, location=location, price=price, ammount=ammount, floors_count=floors_count, floor_face=floor_face, details=details, flat_image=flat_image, user_id=request.user.id)
        flat_data.save()

        messages.success(request, "Your flat selling post added successfully!")
        return render(request, "OwnerDashboard/sell_flat.html")
    return render(request, "OwnerDashboard/sell_flat.html")
def ownerSellLand(request):
    if request.user.is_authenticated and request.method == "POST":
        get_method = request.POST.copy()
        property_type = request.POST.get("property_type")
        division = get_method.get("division")
        district = get_method.get("district")
        location = get_method.get("location")
        price = get_method.get("price")
        ammount = get_method.get("ammount")
        plots_count = get_method.get("plots_count")
        land_type = get_method.get("land_type")
        details = get_method.get("details")
        land_image = request.FILES["photo_url"]

        land_data = Sell_land(property_type=property_type, division=division, district=district, location=location, price=price, ammount=ammount, plots_count=plots_count, land_type=land_type, details=details, land_image=land_image, user_id=request.user.id)
        land_data.save()

        messages.success(request, "Your land selling post added successfully!")
        return render(request, "OwnerDashboard/sell_land.html")
    return render(request, "OwnerDashboard/sell_land.html")


def ownerRent(request):

    user_email = None
    if request.user.is_authenticated:
        user_email = request.user.email
    if request.method == "POST" and request.FILES['rentimage']:
        get_method = request.POST.copy()
        property_type = request.POST.get("property_type")
        rent_type = request.POST.get("rent_type")
        division = get_method.get("division")
        district = get_method.get("district")
        property_location = get_method.get("location")
        available_month = get_method.get("available_month")
        rent_money = get_method.get("money")
        money_type = get_method.get("money_type")
        floor_no = get_method.get("floor_no")

        floor_face = get_method.get("floor_face")
        plot_size = get_method.get("numerical_value_plot")
        numerical_value_type = get_method.get("numerical_value_type")
        area_description = get_method.get("details")
        phone_no=get_method.get("phoneNumber")
        rent_photo = request.FILES['rentimage']
        
        rent_data = OwnerRent(property_type=property_type, rent_type=rent_type, division=division, district=district, property_location=property_location,available_month=available_month, rent_money=rent_money, money_type=money_type,
                              floor_no=floor_no, floor_face=floor_face, plot_size=plot_size, numerical_value_type=numerical_value_type, area_description=area_description, rent_photo=rent_photo,user_email=user_email,phone_no=phone_no)
        rent_data.save()
        messages.success(request, "Your Rental Post added sucessfully!")

        return render(request, "OwnerDashboard/owner_rent.html")

    return render(request, "OwnerDashboard/owner_rent.html")


def owner_post(request):
    user_email = None
    user_id=None
   
    if request.user.is_authenticated:
        user_email = request.user.email
        user_id = request.user.id
    
    my_post=OwnerRent.objects.filter(user_email=user_email)
    all_Sell_flat=Sell_flat.objects.filter(user_id=user_id)
    Sell_land_flat=Sell_land.objects.filter(user_id=user_id)

    context={
        'allpost':my_post,
        'all_Sell_flat':all_Sell_flat,
        'Sell_land':Sell_land_flat
    } 
    return render(request, "OwnerDashboard/owner_post.html",context)


def delete_post(request, id):
    property_type =  request.GET.getlist('type')[0]
    if property_type == "rent" :
        try : 
            OwnerRent.objects.get(id=id).delete()
            time.sleep(1)
            messages.success(request,"Rent post deleted Sucesfully!!")
        except :
            messages.error(request,"Rent post doesn't exist.")
    elif property_type == "flat" :
        try :
            Sell_flat.objects.get(id=id).delete()
            time.sleep(1)
            messages.success(request,"Flat post deleted Sucesfully!!")
        except :
            messages.error(request,"Flat post doesn't exist.")
    elif property_type == "land" :
        try :
            Sell_land.objects.get(id=id).delete()
            time.sleep(1)
            messages.success(request, "Land post deleted Sucesfully!!")
        except :
            messages.error(request,"Land post doesn't exist.")

    return owner_post(request)

def updatepost(request,id):
    property_type =  request.GET.getlist('type')[0]
    if property_type == "rent" :
        single_post= OwnerRent.objects.get(id=id)
    elif property_type == "flat" :
        single_flat = Sell_flat.objects.get(id=id)
    elif property_type == "land" :
        single_land = Sell_land.objects.get(id=id)

    if request.method == "POST" and property_type == "rent" :
        if len(request.FILES) !=0:
            if single_post.rent_photo:
                os.remove(single_post.rent_photo.path)
            single_post.rent_photo=request.FILES['rentimage']    
        get_method = request.POST.copy()
        single_post.property_type = request.POST.get("property_type")
        single_post.rent_type = request.POST.get("rent_type")
        single_post.division = get_method.get("division")
        single_post.district = get_method.get("district")
        single_post.property_location = get_method.get("location")
        single_post.rent_money = get_method.get("money")
        single_post.money_type = get_method.get("money_type")
        single_post.floor_no = get_method.get("floor_no")

        single_post.floor_face = get_method.get("floor_face")
        single_post.plot_size = get_method.get("numerical_value_plot")
        single_post.numerical_value_type = get_method.get("numerical_value_type")
        single_post.area_description = get_method.get("details")
        single_post.phone_no=get_method.get("phoneNumber")
        single_post.save()
        messages.success(request,"Post updated Sucesfully!!")
        
        return owner_post(request)
    
    elif request.method == "POST" and property_type == "flat" :
        if len(request.FILES) !=0:
            if single_flat.flat_image:
                os.remove(single_flat.flat_image.path)
            single_flat.flat_image=request.FILES['photo_url']   
        get_method = request.POST.copy()
        single_flat.price = get_method.get("price")
        single_flat.ammount = get_method.get("ammount")
        single_flat.floors_count = get_method.get("floors_count")
        single_flat.floor_face = get_method.get("floor_face")
        single_flat.details = get_method.get("details")
        single_flat.save()
        messages.success(request,"Flat data updated successfully!")
        return owner_post(request)
    
    elif request.method == "POST" and property_type == "land" :
        single_land = Sell_land.objects.get(id=id)
        if len(request.FILES) !=0:
            if single_land.land_image:
                os.remove(single_land.land_image.path)
            single_land.land_image=request.FILES['photo_url']   
        get_method = request.POST.copy()
        single_land.price = get_method.get("price")
        single_land.ammount = get_method.get("ammount")
        single_land.plots_count = get_method.get("plots_count")
        single_land.land_type = get_method.get("land_type")
        single_land.details = get_method.get("details")
        single_land.save()
        messages.success(request,"land data updated successfully!")
        return owner_post(request)
    
    if property_type == "rent" :
        context={
            'single_post': single_post
        }
        return render(request, "OwnerDashboard/updatePost.html", context)
    elif property_type == "flat" :
        context={
            'single_flat':single_flat
        }
        return render(request, "OwnerDashboard/updateFlat.html", context)
    elif property_type == "land" :
        context={
            'single_land':single_land
        }
        return render(request, "OwnerDashboard/updateLand.html", context)
    
    
#def userSearch(request):
#    return render(request, "TenantDashboard/search.html")
    
def flatDetails(request):
    return render(request, "TenantDashboard/details_flat.html")

def deletesellland(request,id):
    pass

def deletesellflat(request,id):
    pass


def userAccount(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name
        user_phone = request.user.phone_number
        user_address = request.user.address
        land_owner = request.user.is_land_owner
        user_image = request.user.user_image

        if request.method == "POST" :
            user_obj = NewUser.objects.get(id=request.user.id)

            updated_first_name = request.POST.get('first_name')
            updated_last_name = request.POST.get('last_name')
            updated_email = request.POST.get('email')
            updated_phone_number = request.POST.get('phone')
            updated_address = request.POST.get('address')

            if user_obj :
                if len(request.FILES) !=0:
                    if user_obj.user_image:
                        os.remove(user_obj.user_image.path)
                    user_obj.user_image = request.FILES['photo_url']   
                user_obj.first_name = updated_first_name
                user_obj.last_name = updated_last_name
                user_obj.email = request.user.email
                user_obj.phone_number = updated_phone_number
                user_obj.address = updated_address
                if not request.user.is_land_owner :
                    land_ownership = request.POST.get("is_land_owner")
                    if land_ownership == "true":
                        user_obj.is_land_owner = True
                user_obj.save()
                messages.success(request,"Account updated sucesfully!")
                updated_user_obj = NewUser.objects.get(id=request.user.id)

                context = {
                    'user_first_name' : updated_user_obj.first_name,
                    'user_last_name' : updated_user_obj.last_name,
                    'user_email' : updated_user_obj.email,
                    'user_phone_number' : updated_user_obj.phone_number,
                    'user_address' : updated_user_obj.address,
                    'land_owner' : updated_user_obj.is_land_owner,
                    'user_image' : updated_user_obj.user_image
                }
                return render(request, "OwnerDashboard/userAccount.html" , context)


    context = {
        'user_first_name' : first_name,
        'user_last_name' : last_name,
        'user_email' : user_email,
        'user_phone_number' : user_phone,
        'user_address' : user_address,
        'land_owner' : land_owner,
        'user_image' : user_image
    }

    return render(request, "OwnerDashboard/userAccount.html" , context)


def userUpdate(request):
        if request.method == "POST" :
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")

def rent_view(request, id):
        rentdetails = OwnerRent.objects.get(id=id)
        return render(request, 'OwnerDashboard/rentdetails.html', {'rentdetails': rentdetails})
def flat_view(request, id):
        flatdetails = Sell_flat.objects.get(id=id)
        return render(request, 'OwnerDashboard/flatdetails.html', {'flatdetails': flatdetails})
def land_view(request, id):
        landdetails = Sell_land.objects.get(id=id)
        return render(request, 'OwnerDashboard/landdetails.html', {'landdetails': landdetails})
        


def search_house_rent(request):
    query = request.GET.get('query')
    query_division = request.GET.get('query_division')
    house_rent_list = []
    house_rent_list1 = []
    house_rent_list2 = []

    if query and query_division:
        house_rent_list = OwnerRent.objects.filter(
            Q(property_type__icontains=query) &
            Q(division__icontains=query_division)
             
            # Add more fields for searching, e.g., district__icontains=query, division__icontains=query, etc.
        ) 
        house_rent_list1=Sell_land.objects.filter(
            Q(property_type__icontains=query) &
            Q(division__icontains=query_division)
            # Add more fields for searching, e.g., district__icontains=query, division__icontains=query, etc.
        ) 
        house_rent_list2=Sell_flat.objects.filter(
            Q(property_type__icontains=query) &
            Q(divission__icontains=query_division)
            # Add more fields for searching, e.g., district__icontains=query, division__icontains=query, etc.
        )

    context = {
        'query': query,
        'query_division':query_division,
        'house_rent_list': house_rent_list,
        'house_rent_list1': house_rent_list1,
        'house_rent_list2': house_rent_list2
    }

    return render(request, 'OwnerDashboard/search_results.html', context)


def search_type_rent(request):
    query = request.GET.get('query')
   
    house_rent_type = []
    

    if query:
        house_rent_type = OwnerRent.objects.filter(
            Q(rent_type__icontains=query) 
           
             
            # Add more fields for searching, e.g., district__icontains=query, division__icontains=query, etc.
        ) 
       
    context = {
        'query': query,
        
        'house_rent_type': house_rent_type,
        
    }

    return render(request, 'OwnerDashboard/renttype_results.html', context)



def vehicleOwner(request):

    user_email = None
    if request.user.is_authenticated:
        user_email = request.user.email
    if request.method == "POST" and request.FILES['vehicleimage']:
        get_method = request.POST.copy()
        vehicle_type = request.POST.get("vehicle_type")
        division = get_method.get("division")
        district = get_method.get("district")
        vehicle_location = get_method.get("location")
        available_time = get_method.get("available_time")
        km_price = get_method.get("money")
        vehicle_description = get_method.get("details")
        phone_no=get_method.get("phoneNumber")
        vehicle_photo = request.FILES['vehicleimage']
        
        vehicle_data = VehicleOwner(vehicle_type=vehicle_type,division=division, district=district,vehicle_location=vehicle_location,available_time=available_time, km_price=km_price, 
                             vehicle_description=vehicle_description, vehicle_photo=vehicle_photo,user_email=user_email,phone_no=phone_no)
        vehicle_data.save()
        messages.success(request, "Your Rental Post added sucessfully!")

        return render(request, "furniture/vehicle_owner.html")

    return render(request, "furniture/vehicle_owner.html")


def vehicle_post(request):
    user_email = None
    user_id=None
   
    if request.user.is_authenticated:
        user_email = request.user.email
        user_id = request.user.id
    
    vh_post=VehicleOwner.objects.filter(user_email=user_email)
   

    context={
        'vehiclepost':vh_post,
        
    } 
    return render(request, "furniture/vehicle_post.html",context)



def vehicle_update_post(request,id):
    vehicle = VehicleOwner.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) !=0:
            if vehicle.vehicle_photo:
                os.remove(vehicle.vehicle_photo.path)
            vehicle.vehicle_photo=request.FILES['vehicleimage']    
        get_method = request.POST.copy()
        vehicle.vehicle_type = request.POST.get("vehicle_type")
        vehicle.division = get_method.get("division")
        vehicle.district = get_method.get("district")
        vehicle.vehicle_location = get_method.get("location")
        vehicle.km_price = get_method.get("money")
        vehicle.vehicle_description = get_method.get("details")
        vehicle.phone_no=get_method.get("phoneNumber")
        vehicle.save()
        messages.success(request,"Post updated Sucesfully!!")
        
        return vehicle_post(request)
    
    context={
        'vehicle':vehicle
    }
    return render(request, "furniture/vehicle_update.html", context)


def delete_vehicle_post(request, id):
        try : 
            VehicleOwner.objects.get(id=id).delete()
            time.sleep(1)
            messages.success(request,"vehicle post deleted Sucesfully!!")
        except :
            messages.error(request,"vehicle post doesn't exist.")

        return vehicle_post(request)
from re import search
from django.urls import path

from .views import ( delete_post, delete_vehicle_post, deletesellflat, deletesellland, flat_view,flatDetails, furnituredashboard,
                    identifyUser, land_view, owner_post, ownerBuy, ownerDashboard,
                    ownerRent, ownerSellFlat, ownerSellLand, rent_view, search_house_rent, search_type_rent, updatepost, userAccount, userBuy,
                    userDashboard, userRent, userShow, vehicle_post, vehicle_update_post, vehicleOwner)

urlpatterns =[
    path("", identifyUser, name="identify-user"),
    path("account", userAccount, name="account"),
    path("user-home", userDashboard, name="user-home"),
    path("user-buy",userBuy,name="user-buy"),
    path("user-show",userShow, name="user-show"),
    path("user-rent",userRent, name="user-rent"),
    path("owner-home", ownerDashboard, name="owner-home"),
    path("furniture-home", furnituredashboard, name="furniture-home"),
    path("vehicle-post",vehicle_post, name="vehicle-post"),
    path("owner-buy",ownerBuy,name="buy"),
    path("owner-sellFlat",ownerSellFlat, name="flat"),
    path("owner-sellLand",ownerSellLand, name="land"),
    #path("owner-sell/<str:property_type>/", ownerSell, name="sell_property"),
    #path("owner-rent",ownerRent, name="rent"),
    path("owner-rent",ownerRent, name="rent"),
    path("owner-post",owner_post, name="posts"),
    path("post_delete/<int:id>/",delete_post, name="deletepost"),
    path("post_delete_vehicle/<int:id>/",delete_vehicle_post, name="deletepostvehicle"),
    path("update_vehicle/<int:id>/",vehicle_update_post, name="updatepost_vehicle"),
     path("update/<int:id>/",updatepost, name="updatepost"),
    path("vehicle",vehicleOwner, name="vehicle"),
    
    # path("", userDash, name="dash"),
    # path("user-Buy",userBuy, name="buy"),
    # path("user-Sell",userShow, name="sell"),
    # path("user-Rent",userRent, name="rent"),
    #path("search",userSearch, name="search"),
    path("search/details",flatDetails, name="details"),
    path("deletesellflat/<int:id>/",deletesellflat, name="deletesellflat"),

    path("deletesellland/<int:id>/",deletesellland, name="deletesellland"),
    path('rentdetails/<int:id>/', rent_view, name='rentdetails'),
    path('flatdetails/<int:id>/', flat_view, name='flatdetails'),
    path('landdetails/<int:id>/', land_view, name='landdetails'),
   path('search/', search_house_rent, name='search_house_rent'),
   path('renttypesearch/', search_type_rent, name='search_type_rent'),

]
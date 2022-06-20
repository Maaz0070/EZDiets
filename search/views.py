from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import json
import http.client
import pprint
import requests
import sys

# Create your views here.

def index(request):
    return render(request, "search/search.html")


def results(request):
    #searchQuery = "N/A"
    if request.method == "POST": #user has just searched for something
        #call the API with the query to get restruarants and send it to the url
        # list resturants = values from API 
        # list grocery items = values from API 

        
        search = request.POST["searchQuery"]


        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/menuItems/search"

        querystring = {"query":search,"offset":"0","number":"10","minCalories":"0","maxCalories":"5000","minProtein":"0","maxProtein":"100","minFat":"0","maxFat":"100","minCarbs":"0","maxCarbs":"100"}

        headers = {
            'x-rapidapi-key': "1ffc8f17damshb4b7a69a1efd1a1p14a269jsn5273f42924dc",
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring) 
        rect = response.text
        response_dict = json.loads(response.text)

        sys.stdout = open('declare.js', 'w')

        jsonobj = json.dumps(response_dict)

        #var jsonstr = [{x : y: }]
        print("var jsonstr = '{}' ".format(jsonobj) )


        #print(response.text)

        return render(request, "search/results.html", {
           # "data": data,
            "searchQuery": search,
            "responseText": jsonobj,
           # "List": List,
            "Responsei": response_dict,
            "Response_json": response
            #"Res": res
            #"items": #value from API
        })
    else: 
        search = "N/A"

        return render(request, "search/results.html", {
            "searchQuery": search
        })



def register(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "search/signUp.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(firstName, lastName, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/signUp.html", {
                "message": "Username already taken."
            })
        login(request, user) #logs in user 
        return HttpResponseRedirect(reverse("index")) #takes to index

        

    return render(request, "search/signUp.html")

def login(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "search/login.html", {
                "message": "Invalid username and/or password."
            })

    else:
        return render(request, "search/login.html")

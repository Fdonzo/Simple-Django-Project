from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january"  : "Eat right for the entire month!" ,
    "february" : "Watch motivation lectures 20 minuates every day!",
    "march"    : "Learn Django for at least 20 minuates every day!",
    "april"    : "Learn Html for at least 20 minuates every day!",
    "may"      : "Learn Css for at least 20 minuates every day!",
    "june"     : "Learn SQl for at least 20 minuates every day!",
    "july"     : "Learn React for at least 20 minuates every day!",
    "august"   : "Learn Material UI for at least 20 minuates every day!",
    "september": "Learn internet and server for at least 20 minuates every day!",
    "october"  : "Learn gitHub for at least 20 minuates every day!",
    "november" : "Learn AWS for at least 20 minuates every day!",
    "december" : "Learn ci/cd for at least 20 minuates every day!"
}

def index(request):
  list_items = ""
  months = generate_list_of_months() 

  for month in months:
     capitalised_month = month.capitalize()
     month_path = reverse("month-challenge", args=[month])
     list_items += f"<li><a href=\"{month_path}\">{capitalised_month}</a></li>"
  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

def month_challenges_by_number(request, month):
   months = generate_list_of_months()
   if month > len(months):
      return HttpResponseNotFound("<h2>Invalid month</h2>")
   redirect_month = months[month-1]
   redirect_path  = reverse("month-challenge", args=[redirect_month])
   return HttpResponseRedirect(redirect_path)

def month_challenges(request, month):
   try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h2>{challenge_text}</h2>"
    return HttpResponse(response_data)
   except:
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")
    
def generate_list_of_months():
   return list(monthly_challenges.keys())
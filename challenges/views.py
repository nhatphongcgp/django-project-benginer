from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def january(request):
#  return HttpResponse("Thang mot")

# def february(request):
#  return HttpResponse("Thang hai")
monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Learn Django for at least 20 minutes every day!',
    'may': 'Learn Django for at least 20 minutes every day - may!',
    'june': 'Learn Django for at least 20 minutes every day! - june',
    'july': 'Learn Django for at least 20 minutes every day! - july',
    'august': 'Learn Django for at least 20 minutes every day! - august',
    'september': 'Learn Django for at least 20 minutes every day! - sep',
    'october': 'Learn Django for at least 20 minutes every day! oct',
    'november': 'Learn Django for at least 20 minutes every day! nov',
    'december': None,
}

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def dynamic_month_by_number(request, month):
  months = list(monthly_challenges.keys())
  if month > len(months) or month == 0:
    return HttpResponseNotFound("Invalid month")
  redirect_month = months[month -1]
  redirect_path = reverse("month-challenge" , args=[redirect_month]) # challenges/january
  return HttpResponseRedirect(redirect_path)

def dynamic_month(request, month):
     try:
       result_translate = monthly_challenges[month]
       return HttpResponse(result_translate)
     except:
        return HttpResponseNotFound("Thang nay chua ho tro")
    


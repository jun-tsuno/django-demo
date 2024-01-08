from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
  "january": "Learn Python",
  "february": "Do exercise for 20 min a day",
  "march": "Learn Python",
  "april": "Do exercise for 20 min a day",
  "may": "Learn Python",
  "june": "Do exercise for 20 min a day",
  "july": "Learn Python",
  "august": "Do exercise for 20 min a day",
  "september": "Learn Python",
  "october": "Do exercise for 20 min a day",
  "november": "Learn Python",
  "december": "Do exercise for 20 min a day",
}

def index(request):
  list_item = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_item += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"

  response_data = f"<ul>{list_item}</ul>"
  return HttpResponse(response_data)


# Redirect
def monthly_challenges_by_number(request, month):
  if month  > 12:
    return HttpResponseNotFound("Invalid month")

  months = list(monthly_challenges.keys())
  redirect_month = months[month - 1]
  # reverse: urlが変わっても変更しなくて済む
  redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenges/january

  return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"

    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("This month is not supported")
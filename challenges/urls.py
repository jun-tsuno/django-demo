from django.urls import path

from . import views # file name

urlpatterns = [
  # dynamic path: month -> passed to the function as an argument
  path("", views.index, name="index"),
  path("<int:month>", views.monthly_challenges_by_number),
  path("<str:month>", views.monthly_challenge, name="month-challenge" ) #reverse("month-challenge")
]

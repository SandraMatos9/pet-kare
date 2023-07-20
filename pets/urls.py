from django.urls import path
from pets.views import PetView,PetDetailsView


urlpatterns = [
    path("pets/", PetView.as_view()),
    path("pets/<int:pet_id>/", PetDetailsView.as_view()),

]

# from django.urls import path
# from electronics import views

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("update_data/<int:id>",views.update_data, name="update_data")
#     path("delete_data/<int:id>",views.delete_data, name="delete_data")
# ]
from django.urls import path
from electronics import views

urlpatterns = [
    path("", views.home, name="home"),
    path("update_data/<int:id>", views.update_data, name="update_data"),
    path("delete_data/<int:id>", views.delete_data, name="delete_data"),
]

from django.urls import path
from .views import create_interview,get_list_of_interviews,interview_details,delete_interview,edit_interview

app_name='interviews'


urlpatterns = [
    path('create-interview/',create_interview,name="create_interview"),
    path('get-all-interviews/',get_list_of_interviews,name="get_all_interviews"),
    path('get-interview-details/<int:interview_id>/',interview_details,name="get_interview_details"),
    path('edit-interview/<int:interview_id>/',edit_interview,name="edit_interview"),
    path('delete-interview/<int:interview_id>/',delete_interview,name="delete_interview"),
]
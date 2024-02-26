from django.urls import path
from .views import user_login, user_logout, quiz_home,start_quiz,submit_quiz

urlpatterns = [
    path('', user_login, name='login'),
    path('startquiz/<int:quiz_id>/',start_quiz, name='start_quiz'),
    path('submitquiz/<int:quiz_id>/',submit_quiz, name='submit_quiz'),
    path('logout/', user_logout, name='logout'),
    path('quiz/', quiz_home, name='quiz_home'),
]
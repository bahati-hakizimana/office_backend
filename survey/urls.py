from django.urls import path
from . import views

urlpatterns = [
    # Survey routes
    path('surveys/', views.survey_list, name='survey_list'),
    path('survey/create/', views.survey_list, name='survey_create'),
    path('survey/<int:id>/', views.survey_detail, name='survey_detail'),
    path('survey/update/<int:id>/', views.survey_detail, name='survey_update'),
    path('survey/delete/<int:id>/', views.survey_detail, name='survey_delete'),

    # Question routes
    path('questions/', views.question_list, name='question_list'),
    path('question/create/', views.question_list, name='question_create'),
    path('question/<int:id>/', views.question_detail, name='question_detail'),
    path('question/update/<int:id>/', views.question_detail, name='question_update'),
    path('question/delete/<int:id>/', views.question_detail, name='question_delete'),

    # Choice routes
    path('choices/', views.choice_list, name='choice_list'),
    path('choice/create/', views.choice_list, name='choice_create'),
    path('choice/<int:id>/', views.choice_detail, name='choice_detail'),
    path('choice/update/<int:id>/', views.choice_detail, name='choice_update'),
    path('choice/delete/<int:id>/', views.choice_detail, name='choice_delete'),

    # Answer routes
    path('answers/', views.answer_list, name='answer_list'),
    path('answer/create/', views.answer_list, name='answer_create'),
    path('answer/<int:id>/', views.answer_detail, name='answer_detail'),
    path('answer/update/<int:id>/', views.answer_detail, name='answer_update'),
    path('answer/delete/<int:id>/', views.answer_detail, name='answer_delete'),
]

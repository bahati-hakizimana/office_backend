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
    path('questions/by-survey/<int:survey_id>/', views.questions_by_survey, name='questions_by_survey'),

    # Choice routes
    path('choices/', views.choice_list, name='choice_list'),
    path('choice/create/', views.choice_list, name='choice_create'),
    path('choice/<int:id>/', views.choice_detail, name='choice_detail'),
    path('choice/update/<int:id>/', views.choice_detail, name='choice_update'),
    path('choice/delete/<int:id>/', views.choice_detail, name='choice_delete'),
    path('choices/comparison/', views.choice_comparison, name='choice_comparison'),
    path('choices/question/<int:question_id>/', views.choices_by_question, name='choices_by_question'),


    # Answer routes
    path('answers/', views.answer_list, name='answer_list'),
    path('answer/create/', views.answer_list, name='answer_create'),
    path('answer/<int:id>/', views.answer_detail, name='answer_detail'),
    path('answer/update/<int:id>/', views.answer_detail, name='answer_update'),
    path('answer/delete/<int:id>/', views.answer_detail, name='answer_delete'),
    
    # View answer by id with related information
    path('answer/related/<int:id>/', views.answer_detail_with_related, name='answer_detail_with_related'),
     path('answers/analytics/', views.answer_analytics, name='answer_analytics'),
]

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import HttpResponse, JsonResponse
from .models import Survey, Question, Choice, Answer
from .serializers import SurveySerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from django.db.models import Count, Q

# Home view
@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return HttpResponse("Welcome to the Survey App!")

# Survey views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def survey_list(request):
    if request.method == 'GET':
        surveys = Survey.objects.all()
        serializer = SurveySerializer(surveys, many=True)
        return JsonResponse({'surveys': serializer.data})
    elif request.method == 'POST':
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def survey_detail(request, id):
    survey = get_object_or_404(Survey, id=id)
    if request.method == 'GET':
        serializer = SurveySerializer(survey)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = SurveySerializer(survey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Question views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def question_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse({'questions': serializer.data})
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def question_detail(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def questions_by_survey(request, survey_id):
    try:
        survey = get_object_or_404(Survey, id=survey_id)
        questions = Question.objects.filter(survey=survey)
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse({'questions': serializer.data})
    except Survey.DoesNotExist:
        return Response({"error": "Survey not found"}, status=status.HTTP_404_NOT_FOUND)


# Choice views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def choice_list(request):
    if request.method == 'GET':
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return JsonResponse({'choices': serializer.data})
    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # View for getting choices by question ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def choices_by_question(request, question_id):
    try:
        question = get_object_or_404(Question, id=question_id)
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return JsonResponse({'choices': serializer.data})
    except Question.DoesNotExist:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def choice_detail(request, id):
    choice = get_object_or_404(Choice, id=id)
    if request.method == 'GET':
        serializer = ChoiceSerializer(choice)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    

# Answer views
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def answer_list(request):
    if request.method == 'GET':
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return JsonResponse({'answers': serializer.data})
    elif request.method == 'POST':
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def answer_detail(request, id):
    answer = get_object_or_404(Answer, id=id)
    if request.method == 'GET':
        serializer = AnswerSerializer(answer)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# View for answer details including related survey, question, and choice
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def answer_detail_with_related(request, id):
    answer = get_object_or_404(Answer, id=id)
    survey = answer.question.survey
    question = answer.question
    choice = answer.choice
    tenant = answer.tenant

    data = {
        'survey_title': survey.title,
        'survey_category': survey.get_category_display(),
        'question_text': question.text,
        'choice_text': choice.text,
        'is_positive': choice.is_positive,
        'tenant_username': tenant.username  
    }

    return JsonResponse(data)



# View for comparing choices
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def choice_comparison(request):
    choices = Choice.objects.all()
    
    positive_choices = choices.filter(is_positive=True)
    negative_choices = choices.filter(is_negative=True)
    
    data = {
        'positive_choices_count': positive_choices.count(),
        'negative_choices_count': negative_choices.count(),
        'positive_choices': ChoiceSerializer(positive_choices, many=True).data,
        'negative_choices': ChoiceSerializer(negative_choices, many=True).data
    }
    
    return JsonResponse(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def answer_analytics(request):
    # Aggregate the total number of positive and negative answers
    analytics = Answer.objects.select_related('choice').aggregate(
        total_positive=Count('id', filter=Q(choice__is_positive=True)),
        total_negative=Count('id', filter=Q(choice__is_positive=False))
    )
    
    data = {
        'total_positive_answers': analytics['total_positive'],
        'total_negative_answers': analytics['total_negative']
    }

    return JsonResponse(data)

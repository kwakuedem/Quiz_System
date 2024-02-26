from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# from .forms import RegistrationForm
from .models import Quiz, Question, Choice
from django.contrib.auth.decorators import login_required

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz_home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def quiz_home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_home.html', {'quizzes': quizzes})

@login_required
def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'start_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = Quiz.objects.get(pk=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        score = 0
        No_question=0
        
        for question in questions:
            No_question=Question.objects.count
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        return render(request, 'quiz_result.html', {'quiz': quiz, 'score': score,'no_question':No_question})
    return redirect('quiz_home')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
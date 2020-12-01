


from .models import Quiz
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuizApiSerializer

class QuizApiList(APIView):

	def get(self, request):
		quizapis = Quiz.objects.all()
		serializer = QuizApiSerializer(quizapis, many = True)
		return Response(serializer.data)

	def post(self):
		pass

def qpage(request):
	questions = Quiz.objects.all()

	return render(request, 'quiz/quiz.html', { 'questions': questions})


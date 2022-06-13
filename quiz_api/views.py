from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Quiz
from .models import Question
from .models import Result
from profiles_api.models import UserProfile
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict
from rest_framework.authentication import TokenAuthentication

# Quiz View
class QuizView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        if 'id' in request.query_params.keys():
            quiz=Quiz.objects.get(id=request.query_params['id'])
            quiz=model_to_dict(quiz)
            quiz['questions']=[]
            for question in Question.objects.filter(quiz=quiz['id']):
                quiz['questions'].append(model_to_dict(question))
            # return Response(quiz)
            print(quiz)
            return Response(quiz)
        quizs=Quiz.objects.all()
        quizs_list=[]
        for quiz in quizs:
            quiz_dict=model_to_dict(quiz)
            quiz_dict['teacher']=quiz.teacher.name
            quizs_list.append(quiz_dict)
        return Response(quizs_list)
    
    def post(self,request):
        quiz=Quiz(name=request.data['name'],teacher=request.user)
        quiz.save()
        # save questions
        for question in request.data['questions']:
            question_obj=Question(quiz=quiz,question=question['question'],option1=question['option1'],option2=question['option2'],option3=question['option3'],option4=question['option4'],answer=question['answer'])
            question_obj.save()
        return Response(model_to_dict(quiz))
    
    def put(self,request):
        quiz=Quiz.objects.get(id=request.data['id'])
        quiz.name=request.data['name']
        quiz.save()
        # save questions
        for question in request.data['questions']:
            # check if question exists
            if Question.objects.filter(id=question['id'],quiz=quiz).exists():
                question_obj=Question.objects.get(id=question['id'])
                question_obj.question=question['question']
                question_obj.option1=question['option1']
                question_obj.option2=question['option2']
                question_obj.option3=question['option3']
                question_obj.option4=question['option4']
                question_obj.answer=question['answer']
                # update question
                question_obj.save()
            else:
                # create question
                question_obj=Question(quiz=quiz,question=question['question'],option1=question['option1'],option2=question['option2'],option3=question['option3'],option4=question['option4'],answer=question['answer'])
                question_obj.save()
        return Response(model_to_dict(quiz))

    def delete(self,request):
        quiz=Quiz.objects.get(id=request.data['id'])
        quiz.delete()
        return Response(model_to_dict(quiz))

class ResultView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        results=Result.objects.all()
        results_list=[]
        for result in results:
            result_dict=model_to_dict(result)
            result_dict['student']=result.student.name
            result_dict['quiz']=result.quiz.name
            # total score= total number of questions in quiz
            result_dict['total']=len(Question.objects.filter(quiz=result.quiz))
            results_list.append(result_dict)
            print(results_list)
        return Response(results_list)
    
    def post(self,request):
        result=Result(quiz=Quiz.objects.get(id=request.data['quiz']),student=request.user,score=request.data['score'])
        result.save()
        return Response(model_to_dict(result))
    
    def put(self,request):
        result=Result.objects.get(id=request.data['id'])
        result.score=request.data['score']
        result.save()
        return Response(model_to_dict(result))
    
    def delete(self,request):
        result=Result.objects.get(id=request.data['id'])
        result.delete()
        return Response(model_to_dict(result))
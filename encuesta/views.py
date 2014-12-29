from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from encuesta.models import pregunta,campo
from django.template import RequestContext, loader

def volver(request):
	return HttpResponse("hola mundo")
def detail(request,question_id):
	question=get_object_or_404(pregunta,pk=question_id)
	return  render ( request ,  'encuesta/encuesta/detailds.html' ,  { 'question' :  question })

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def indice(request):
	lista_preguntas=pregunta.objects.all()
	pagina=loader.get_template("encuesta/encuesta/indice.html")
	contexto=RequestContext(request,{'lista_preguntas':lista_preguntas,})

	return HttpResponse(pagina.render(contexto))

def index(request):
    latest_question_list = pregunta.objects.all()
    template ='encuesta/encuesta/index.html'
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return render(request,template,{'latest_question_list':latest_question_list})

# Create your views here.

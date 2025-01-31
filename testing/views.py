from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "temp/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "temp/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "temp/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choce_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render (
            request,
            "temp/detail.html", {
                "question" : question,
                "error_massage" : "kamu tidak bisa mengakses pilihan"
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("testing:results"))
    
class IndexView(generic.ListView):
    template_name = "temp/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "temp/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "temp/results.html"

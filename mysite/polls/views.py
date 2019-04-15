# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.template import loader
# Create your views here.


# class IndexView(generic.ListView):
#     #latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template_name = "./polls/index.html"
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions"""
#         return Question.objects.order_by('-pub_date')[:5]
#     # context = {
#     #     "latest_question_list":latest_question_list,
#     # }
#     # #out_put = ",".join([q.question_text for q in latest_question_list])
#     # return render(request, "./polls/index.html", context=context)


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    print latest_question_list
    context = {
         "latest_question_list": latest_question_list,
     }
    return render(request, "./polls/index.html", context=context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "./polls/results.html"
     # question = get_object_or_404(Question, pk=question_id)
     # return render(request, "polls/results.html", {"question":question, })


class DetailView(generic.DetailView):
    model = Question
    template_name = "./polls/detail.html"
    # question = get_object_or_404(Question, pk=question_id)
    # context = {
    #     "question": question,
    # }
    # return render(request, "./polls/detail.html", context=context)


def vote(request, question_id):

    print request.POST["choice"]
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except(KeyError, Choice.DoesNotExist) as e:

        return render(request, "./polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", arges=(question.id, )))
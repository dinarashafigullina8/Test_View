from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

import core.models


class TitleMixin:
    title: str = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = self.get_title()
        return context

class IndexView(TitleMixin,TemplateView):
    template_name = 'core/index.html'
    title = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['info'] = self.get_info()
        return context

    def get_info(self):
        return 'Главная страница'




class Books(ListView):
    title = 'Книги'
    def get_queryset(self):
        name = self.request.GET.get('name')
        queryset = core.models.Book.objects.all()
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset



class BookDetail(TitleMixin,DetailView):
    queryset = core.models.Book.objects.all()

    def get_title(self):
        return str(self.get_object())


def book_detail(request, pk):
    book = get_object_or_404(core.models.Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

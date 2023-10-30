from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Car
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


class CarList(ListView):
    model = Car
    paginate_by = 10
    template_name = ""

    def get_queryset(self):
        return Car.objects.all()

    def get_context_data(self, request, **kwargs):
        context = super(CarList, self).get_context_data(**kwargs)
        cars = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(cars, self.paginate_by)
        try:
            cars = paginator.page(page)
        except PageNotAnInteger:
            cars = paginator.page(1)
        except EmptyPage:
            cars = paginator.page(paginator.num_pages)
        context['cars'] = cars
        return render(request, context, self.template_name)


class CarDetail(DetailView):
    model = Car
    template_name = ""
    context_object_name = "car"

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        return render(request, context, self.template_name)
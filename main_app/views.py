from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lego, Builder
from .forms import BuildingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def lego_index(request):
  lego = Lego.objects.all()
  return render(request, 'lego/index.html', {
    'lego': lego
  })

def lego_detail(request, lego_id):
  lego = Lego.objects.get(id=lego_id)
  id_list = lego.builders.all().values_list('id')
  builders_lego_doesnt_have = Builder.objects.exclude(id__in=id_list)
  building_form = BuildingForm()
  return render(
    request,
    'lego/detail.html',
    {
      'lego': lego,
      'building_form': building_form,
      'lego': builders_lego_doesnt_have
    }
  )

class LegoCreate(CreateView):
  model = Lego
  fields = ['name', 'description', 'pieces', 'cost', 'store_page', 'set_id']

class LegoUpdate(UpdateView):
  model = Lego
  fields = ['name', 'description', 'pieces', 'cost', 'store_page', 'set_id']

class LegoDelete(DeleteView):
  model = Lego
  success_url = '/lego/'

def add_building(request, lego_id):
  form = BuildingForm(request.POST)
  
  if form.is_valid():
    new_building = form.save(commit=False)
    new_building.lego_id = lego_id
    new_building.save()
  
  return redirect('detail', lego_id=lego_id)

def assoc_builder(request, lego_id, builder_id):
  lego = Lego.objects.get(id=lego_id)
  lego.builders.add(builder_id)
  return redirect('detail', lego_id=lego_id)

def unassoc_builder(request, lego_id, builder_id):
  Lego.objects.get(id=lego_id).builders.remove(builder_id)
  return redirect('detail', lego_id=lego_id)

class BuilderList(ListView):
  model = Builder

class BuilderDetail(DetailView):
  model = Builder

class BuilderCreate(CreateView):
  model = Builder
  fields = ['date', 'rating']

class BuilderUpdate(UpdateView):
  model = Builder
  fields = ['date', 'rating']

class BuilderDelete(DeleteView):
  model = Builder
  success_url = '/builders/'
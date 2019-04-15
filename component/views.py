from django.shortcuts import render
from .models import Component
import json
def main_view(request):
    if request.method == 'POST':
        borrower = request.POST.get('borrower')
        components_name = request.POST.getlist("component_name")
        components_count = request.POST.getlist("component_count")
        components = components_mapper(components_name,components_count)
        comp_obj = Component(borrower=borrower, components=components)
        # comp_obj.borrower = request.POST.get('borrower')
        # comp_obj.components = components
        comp_obj.save()
        print(comp_obj.date)

    return render(request, 'component/index.html')
    





def components_mapper(components_name, components_count):
    components = {}
    for each_comp, comp_count in zip(components_name, components_count):
        components[each_comp] = comp_count

    return components


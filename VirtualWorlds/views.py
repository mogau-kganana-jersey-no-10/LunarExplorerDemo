from django.shortcuts import render

# Create your views here.
def virtual_world(request):
    return render(request, 'VirtualWorlds/scene.html')
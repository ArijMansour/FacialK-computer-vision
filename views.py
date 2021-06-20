from django.shortcuts import render
import os 

def home(request):
    return render(request, "Formation.html")


def about(request):
    return render(request, "about.html")


def align(request):
    os.system('python facenet/align/align_dataset_yolo_gpu.py')
    return render(request,"home.html")
def hello(request):

    return render(request, "default.html")
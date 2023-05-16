from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'eduardo'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello world %s !</h1>" % username)


def tasks(request): # Como parámetro de la funcion id
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def projects(request): 
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)

    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=2
                            )
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        # return render(request, 'projects/create_project.html', {
        #     'form': CreateNewProject()
        # })
        return redirect('projects')
    
    



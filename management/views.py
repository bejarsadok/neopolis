from django.shortcuts import render
from .forms import ProjectForm, TaskForm
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.contrib.auth.models import User
from .tasks import send_task_notification_email


def project_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/management/project/list/")
    context['form'] = form
    return render(request, "project/create_view.html", context)


def project_list_view(request):
    context = {}
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    context = {'dataset': serializer.data}

    return render(request, "project/list_view.html", context)


# after updating it will redirect to detail_View
def project_detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Project.objects.get(id=id)

    return render(request, "project/detail_view.html", context)

# update view for details


def project_update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Project, id=id)

    # pass the object as instance in form
    form = ProjectForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/management/project/list/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "project/update_view.html", context)


# delete view for details
def project_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Project, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/management/project/list/")

    return render(request, "project/delete_view.html", context)


##### task views ####

def task_create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        if task.assiged_to:
            send_task_notification_email.delay(task.id, task.assiged_to.email)
        return HttpResponseRedirect("/management/task/list/")
    else:
        # Print form errors to the console for debugging
        print(form.errors)
    # context['form'] = form
    users = User.objects.all()
    projects = Project.objects.all()
    return render(request, "task/create_view.html", {'form': form, 'users': users, 'projects': projects})


def task_list_view(request):
    context = {}
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    context = {'dataset': serializer.data}

    return render(request, "task/list_view.html", context)


# after updating it will redirect to detail_View
def task_detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = Task.objects.get(id=id)

    return render(request, "task/detail_view.html", context)

# update view for details


def task_update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Task, id=id)

    # pass the object as instance in form
    form = TaskForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/management/task/list/")
    else:
        # Print form errors to the console for debugging
        print(form.errors)

    users = User.objects.all()
    projects = Project.objects.all()
    return render(request, "task/update_view.html", {'form': form, 'users': users, 'projects': projects})


# delete view for details
def task_delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Task, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/management/task/list/")

    return render(request, "task/delete_view.html", context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from .models import Worker, Position, Task, TaskType
from .forms import WorkerForm, PositionForm, TaskTypeForm, TaskForm, TaskCommentForm


def is_manager(user):
    return user.is_superuser or user.groups.filter(name='Manager').exists()


@login_required
def home(request):
    workers = Worker.objects.all()
    tasks = Task.objects.all()
    positions = Position.objects.all()
    task_types = TaskType.objects.all()
    return render(
        request,
        'home.html',
        {
            'workers': workers,
            'tasks': tasks,
            'positions': positions,
            'task_types': task_types,
        },
    )


@user_passes_test(is_manager)
def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.set_password(form.cleaned_data['password'])
            worker.save()
            return redirect('home')
    else:
        form = WorkerForm()
    return render(request, 'add_worker.html', {'form': form})


@user_passes_test(is_manager)
def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PositionForm()
    return render(request, 'add_position.html', {'form': form})


@user_passes_test(is_manager)
def add_task_type(request):
    if request.method == 'POST':
        form = TaskTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskTypeForm()
    return render(request, 'add_task_type.html', {'form': form})


@user_passes_test(is_manager)
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


@login_required
def task_list(request):
    q = request.GET.get('q', '')
    tasks = Task.objects.all()
    if q:
        tasks = tasks.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )
    sort = request.GET.get('sort', '')
    if sort:
        tasks = tasks.order_by(sort)
    return render(
        request,
        'task_list.html',
        {'tasks': tasks, 'q': q, 'sort': sort}
    )


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.select_related('author').order_by('-created')
    if request.method == "POST":
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskCommentForm()
    return render(
        request,
        "task_detail.html",
        {"task": task, "comments": comments, "form": form}
    )

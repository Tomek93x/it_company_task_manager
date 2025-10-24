from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Worker, Position, Task, TaskType
from .forms import WorkerForm, PositionForm, TaskTypeForm, TaskForm, TaskCommentForm


class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='Manager').exists()


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workers'] = Worker.objects.all()
        context['tasks'] = Task.objects.all()
        context['positions'] = Position.objects.all()
        context['task_types'] = TaskType.objects.all()
        return context


class AddWorkerView(ManagerRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = "add_worker.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        worker = form.save(commit=False)
        worker.set_password(form.cleaned_data['password'])
        worker.save()
        return super().form_valid(form)


class AddPositionView(ManagerRequiredMixin, CreateView):
    model = Position
    form_class = PositionForm
    template_name = "add_position.html"
    success_url = reverse_lazy("home")


class AddTaskTypeView(ManagerRequiredMixin, CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "add_task_type.html"
    success_url = reverse_lazy("home")


class AddTaskView(ManagerRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "add_task.html"
    success_url = reverse_lazy("home")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "")
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))
        sort = self.request.GET.get("sort", "")
        if sort:
            qs = qs.order_by(sort)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        context["sort"] = self.request.GET.get("sort", "")
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()
        comments = task.comments.select_related("author").order_by("-created")
        context["comments"] = comments

        if self.request.method == "POST":
            form = TaskCommentForm(self.request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.task = task
                comment.author = self.request.user
                comment.save()
                return redirect("task_detail", pk=task.pk)
        else:
            form = TaskCommentForm()
        context["form"] = form
        return context

    def post(self, *args, **kwargs):
        # Obsługa komentarza przez POST
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

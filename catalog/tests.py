from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Position, Worker, TaskType, Task

User = get_user_model()

class PositionModelTest(TestCase):
    def test_str(self):
        position = Position.objects.create(name="Developer")
        self.assertEqual(str(position), "Developer")

class WorkerVisibilityTest(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.user = User.objects.create_user(username='user', password='userpass')
        self.position = Position.objects.create(name="Dev")
        Worker.objects.create(first_name="Jan", last_name="Kowalski", position=self.position)

    def test_workers_visible_for_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('home'))  # domyślny adres - sprawdź czy inny!
        self.assertContains(response, "Workers")
        self.assertContains(response, "Jan Kowalski")

    def test_workers_hidden_for_normal_user(self):
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, "Workers")
        self.assertNotContains(response, "Jan Kowalski")

class TaskModelTest(TestCase):
    def setUp(self):
        self.type = TaskType.objects.create(name="Bugfix")
        self.task = Task.objects.create(name="Fix bug", deadline="2025-12-01", priority="low", task_type=self.type)

    def test_str(self):
        self.assertIn("Fix bug", str(self.task))


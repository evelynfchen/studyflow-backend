
from django.conf import settings
from django.db import models
from django.db.models import Q


class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories",
    )
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="uniq_category_name_per_user",
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Task(models.Model):
    class Priority(models.TextChoices):
        HIGH = "HIGH", "High"
        MEDIUM = "MEDIUM", "Medium"
        LOW = "LOW", "Low"

    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED", "Not Started"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(null=True, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_STARTED,
    )

    def __str__(self) -> str:
        return self.title


class Subtask(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="subtasks",
    )
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Resource(models.Model):
    class ResourceType(models.TextChoices):
        NOTE = "NOTE", "Note"
        LINK = "LINK", "Link"

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="resources",
    )
    type = models.CharField(max_length=10, choices=ResourceType.choices)

    content_text = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="resource_note_or_link_exclusive",
                check=(
                    Q(type="NOTE", content_text__isnull=False, url__isnull=True)
                    | Q(type="LINK", url__isnull=False, content_text__isnull=True)
                ),
            )
        ]

    def __str__(self) -> str:
        return f"{self.type}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"

from django.db import models
from django.utils import timezone


class GroupCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        GroupCategory,
        blank=True,
        null=True,
        related_name="groups",
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class GroupMember(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="members")

    def __str__(self) -> str:
        return self.name


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name


class Expense(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(
        ExpenseCategory,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="expenses",
    )
    members = models.ManyToManyField(GroupMember, related_name="expenses")
    amount = models.FloatField()
    date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

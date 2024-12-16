from django.db import models
from decimal import Decimal

"""
    Домашнее задание по теме "QuerySet запросы в базу данных"
    Цель: сделать первые записи в БД при помощи QuerySet запросов, закрепив знания о них.
    Задача "Я буду устанавливать все игры!":
    Студент: Крылов Эдуард Васильевич
    Дата: 16.12.2024г.
"""


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

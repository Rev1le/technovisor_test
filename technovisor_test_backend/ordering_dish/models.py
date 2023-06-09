from django.db import models


# Создание абстрактного класса для исправления warning в файле views.py
class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Worker(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Dish(BaseModel):
    title = models.CharField(max_length=128, unique=True)
    composition = models.TextField(default="Нет информации о составе продукта")
    price = models.FloatField()

    def __str__(self):
        return self.title


class Order(BaseModel):
    date = models.DateField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return self.worker.name

    def display_dishes(self):
        return ', '.join([dish.title for dish in self.dishes.all()[:3]])

    display_dishes.short_description = 'Dish'


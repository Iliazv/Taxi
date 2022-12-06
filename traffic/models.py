from pyexpat import model
from django.db import models
import json


class Order(models.Model):
    day = models.CharField(max_length=50)
    hour = models.IntegerField()
    minute = models.CharField(max_length=10)
    start = models.CharField(max_length=100)
    finish = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    interest = models.CharField(max_length=120)
    selected = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def set_foo(self, x):
        self.foo = json.dumps(x)

    def get_foo(self):
        return json.loads(self.foo)

class Car(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to = 'expert_images/', blank = True)
    year = models.IntegerField()

    CAR_CATEGORY = (
        ('ЭКОНОМ', 'Эконом'),
        ('КОМФОРТ', 'Комфорт'),
        ('УНИВЕРСАЛ', 'Универсал'),
        
    )

    category = models.CharField(max_length=50, choices=CAR_CATEGORY, default='ЭКОНОМ')

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=1800)
    date = models.DateTimeField('Published')
    
    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField(max_length=3000)
    date = models.DateTimeField('Send')

    def __str__(self):
        return str(self.date)
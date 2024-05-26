from django.db import models
from django.urls import reverse
class Dance(models.Model):
    type=models.CharField(max_length=50)
    comment=models.CharField(max_length=50)

    def __str__(self):
        return (f'[type:{self.type},'
                f'comment:{self.comment}]')
    class Meta:
        verbose_name = 'Dance'
        verbose_name_plural = 'Dances'

class Dancer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    def __str__(self):
        return (f'[name:{self.name} {self.surname},'
                f'contact:{self.contact}]')
    def get_absolute_url(self):
        return reverse('dances:detail', kwargs={'id': self.id})

    class Meta:
        verbose_name='Dancer'
        verbose_name_plural = 'Dancers'
class Action(models.Model):
    dance_id=models.ForeignKey(Dance,on_delete=models.CASCADE)
    dancer_id=models.ForeignKey(Dancer,on_delete=models.CASCADE)
    action_comment=models.CharField(max_length=100)
    def __str__(self):
        return (f'[dance_id:{self.dance_id},'
                f'dancer_id:{self.dancer_id},'
                f'action_commente:{self.action_comment}]')

class Place(models.Model):
    action_id=models.ForeignKey(Action,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    def __str__(self):
        return (f'[action_id:{self.action_id},'
                f'address:{self.address}]')
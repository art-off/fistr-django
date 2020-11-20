from django.db import models


class Organizer(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='ФИО организатора')

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='ФИО волонтера')

    def __str__(self):
        return self.name


class Grant(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='Название гранта')
    amount = models.IntegerField(verbose_name='Сумма гранта')

    def __str__(self):
        return f'({self.amount} рублей) {self.name}'


class Event(models.Model):
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, verbose_name='Название мероприятия')

    RATES = (
        ('а', 'Наивысший'),
        ('б', 'Высокий'),
        ('в', 'Средний'),
        ('г', 'Низкий'),
        ('д', 'Наинизший'),
    )
    rate = models.CharField(max_length=1, choices=RATES, default='в', verbose_name='Рейтинг мероприятия')

    organizers = models.ManyToManyField(Organizer, verbose_name='Организаторы')
    volunteers = models.ManyToManyField(Volunteer, verbose_name='Волонтеры')
    grant = models.ForeignKey(Grant, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Грант')

    def __str__(self):
        return self.name


class OrganizerRate(Organizer):
    class Meta:
        proxy = True

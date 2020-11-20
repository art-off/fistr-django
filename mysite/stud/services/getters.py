from ..models import Event, Organizer


class RateItem:
    def __init__(self, id, name, score_count):
        self.id = id
        self.name = name
        self.score_count = score_count

    def __str__(self):
        return f'{self.score_count} - {self.name}'


def __calc_cost(event: Event):
    cost = 0
    if event.rate == 'а':
        cost += 20
    elif event.rate == 'б':
        cost += 16
    elif event.rate == 'в':
        cost += 10
    elif event.rate == 'г':
        cost += 6
    elif event.rate == 'д':
        cost += 2

    if event.grant == None:
        return cost

    if event.grant.amount > 1000000:
        cost += 20
    elif event.grant.amount > 500000:
        cost += 16
    elif event.grant.amount > 250000:
        cost += 10
    elif event.grant.amount > 100000:
        cost += 6
    else:
        cost += 2

    return cost


def get_rate_organizers() -> [RateItem]:
    result = []

    for o in Organizer.objects.all():
        result.append(RateItem(o.id, o.name, 0))

    for e in Event.objects.all():
        e_cost = __calc_cost(e)
        for o in e.organizers.all():
            for i in range(len(result)):
                if result[i].id == o.id:
                    result[i].score_count += e_cost

    result.sort(key=lambda x: x.score_count, reverse=True)
    return result

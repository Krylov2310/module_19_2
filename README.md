# Открываем терминал
python manage.py shell

# Добавляем покупателей
from task1.models import *
Buyer.objects.create(name='Ilya', balance=1500, age='24')
Buyer.objects.create(name='Terminator2000', balance=42.15, age='52')
Buyer.objects.create(name='Ubivator432', balance=0.5, age='16')

# Добавляем игры в каталог
from task1.models import *
Game.objects.create(title='Cyberpunk 2077', cost=31, size=46.2, description='Game of the year', age_limited=True)
Game.objects.create(title='Mario', cost=55, size=0.5, description='Old game', age_limited=False)
Game.objects.create(title='Hitman', cost=12, size=36.6, description='Who kills Mark?', age_limited=True)

# Продаем игры с учетом возраста покупателей
from task1.models import *
first_buyer = Buyer.objects.get(age__lt=18)
second_buyer, third_buyer = Buyer.objects.filter(age__gt=18)
Game.objects.get(id=1).buyer.set((second_buyer, third_buyer))
Game.objects.get(id=2).buyer.set([third_buyer])
Game.objects.get(id=3).buyer.set((second_buyer, first_buyer, third_buyer))

# Выводим список покупателей
from task1.models import *
buyer = Buyer.objects.all()
print(buyer)

# Выводим список игр
from task1.models import *
game = Game.objects.all()
print(game)

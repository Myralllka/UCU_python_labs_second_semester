from modules.streets import *
from modules.character import *
from modules.items import *
import random
import copy

"""
game classes and characters and items initialization.
"""
stryiska = Street('Стрийська вулиця',
                  'Відома вулиця біля УКУ, нічого цікавого')
kozelnytska = Street('Козельницька вулиця',
                     'Вулиця, на якій знаходиться УКУ')
franka = Street('Вулиця Івана Франка',
                'Якщо по ній йти, можна потрапити в інший корпус УКУ. або '
                'знайти щось цікаве...')
saharova = Street('вулиця академіка Сахарова',
                  'по цій вулиці знаходиться багато приємного: Нова пошта, '
                  'Фуршет...')
boi = Street('вулиця Бой-Желенського',
             'прождовження вулиці Героїв Майдану')
heroes = Street('вулиця Героїв Майдану',
                'складний шлях до мети..')
vitovsky = Street("вулиця Дмитра Вітовського",
                  'саме те, що треба.')

kozelnytska.link_street(franka, 'east')
kozelnytska.link_street(stryiska, 'west')
stryiska.link_street(kozelnytska, 'east')
stryiska.link_street(saharova, 'south_west')
stryiska.link_street(heroes, 'west')
stryiska.link_street(vitovsky, 'north_west')
franka.link_street(vitovsky, 'north_west')
franka.link_street(kozelnytska, 'south_west')
heroes.link_street(boi, 'west')
heroes.link_street(stryiska, 'east')
boi.link_street(heroes, 'east')
boi.link_street(saharova, 'west')
saharova.link_street(boi, 'east')
saharova.link_street(stryiska, 'south_east')
saharova.link_street(vitovsky, 'north')
vitovsky.link_street(saharova, 'east')
vitovsky.link_street(franka, 'east_north')
vitovsky.link_street(franka, 'east_south')

cipok = Item('cipok',
             'Ціпок, палиця, якою легко бити негідників',
             2)
water = Item('water',
             'Пляшка води, може врятувати у скрутну хвилину',
             0)
batig = Item('batig',
             'Батіг, прикріплена до держака мотузка, якою можна '
             'зловити чи набити грабіжника',
             2)
slovo = Item('slovo',
             'Словом іноді можна сильніше більше, ніж предметом (закляття)',
             5)
tetiana = Character('tetiana',
                    'friend',
                    'Тетяна, прекрасна дама серця, яку необхідно знайти',
                    None,
                    None,
                    'врятуй мене, о прекрасний принц! [safe]')
lotr = Character('lotr',
                 'enemy',
                 'Лотр, негідник, грабіжник',
                 batig,
                 2,
                 'віддавай мені всі свої речі!')
djigun = Character('djigun',
                   'enemy',
                   'Джиґун, самовдоволений франт',
                   cipok,
                   2,
                   'ти ніхто проти мене! здавайся й віддавай мені свою '
                   'принцесу!!')
batiar = Character('batiar',
                   'enemy',
                   'Батяр, гульвіса, п\'яничка, популярний у жінок',
                   cipok,
                   4,
                   'Пффф.... маєш горло просушити? [give]')
witch = Character('witch',
                  'enemy',
                  'Зла відьма, Босс',
                  slovo,
                  10,
                  'ТИ НЕ ПРОЙДЕШ')
streets = [kozelnytska, stryiska, boi, franka, saharova, heroes, vitovsky]
items = [cipok, water, batig]
characters = [batiar, lotr, djigun]
vitovsky.add_character(tetiana)
[i.add_item(slovo) for i in [saharova, boi]]
for each in streets:
    for i in range(random.randint(1, 3)):
        each.add_character(copy.deepcopy(random.choice(characters)))
for each in streets:
    for i in range(random.randint(1, 3)):
        each.add_item(copy.deepcopy(random.choice(items)))

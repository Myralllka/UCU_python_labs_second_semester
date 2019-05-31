#!/bin/env python

from modules import *

current_street = kozelnytska
backpack = items


def description(info: list):
    for tmp in info:
        tmp.describe()


dead = False
to_kill = 10
if __name__ == '__main__':

    while dead == False:
        try:
            print("\n(Команда [help] щоб побачити більше команд. "
                  "кількість життя: {})"
                  .format(Character.hero_health))
            current_street.get_details()
            inhabitants = current_street.get_characters()
            items = current_street.get_items()
            if inhabitants:
                print('на цій вулиці такі персонажі:')
                description(inhabitants)
            if items is not None:
                print('також такі штуки:')
                description(items)
            command = input("> ")
            if command in ["north", "south", "east", "west", "south_west",
                           "north_west", "south_east", "east_north",
                           "east_south"]:
                # Move in the given direction
                current_street = current_street.ch_street(command)
            elif command == 'give' and batiar in inhabitants:
                backpack.remove(water)
                for each in inhabitants:
                    if each == batiar and each.status == 'enemy':
                        each.status = 'friend'
                        to_kill -= 1
                        break
            elif command == 'safe' and tetiana in inhabitants:
                Character.saved = True
                inhabitants.remove(tetiana)
                kozelnytska.add_character(witch)
                print('І кожен фініш - це, по-суті, старт!')
            elif command == 'help':
                print('Можливі команди:\n\ttalk\n\tfight\n\ttake\n\tbackpack')
            elif command == 'backpack':
                print(', '.join([i.name for i in backpack]))
            elif command == "talk":
                # Talk to the inhabitant - check whether there is one!
                if inhabitants is not None:
                    character = eval(
                            input('З ким хочеш поговорити? \n > '))
                    character = inhabitants[inhabitants.index(character)]
                    character.talk()
            elif command == "fight":
                if inhabitants is not None:
                    try:
                        tmp = [i.name for i in inhabitants if
                               i.status == 'enemy']
                        msg = 'Кого бити вздумав? \n {} > ' \
                            .format(", ".join(tmp))
                        character = eval(input(msg))
                        character = inhabitants[inhabitants.index(character)]
                        if character not in inhabitants:
                            print("Трясця! тут порожньо.")
                            continue
                        # Fight with the inhabitant, if there is one
                        tmp = [i.name for i in backpack]
                        msg = "Чим би його лупанути...?\n {} > " \
                            .format(', '.join(tmp))
                        fight_with = eval(input(msg))
                        if fight_with not in backpack:
                            print("Та ні, ТАКОГО тут точно немає")
                            continue
                    except SyntaxError:
                        print('Давай ще раз!')
                        continue
                    # Do I have this item?
                    if fight_with in backpack:
                        backpack.remove(fight_with)
                        if character.fight(fight_with) == 'hurt':
                            character.health -= fight_with.power
                            if character.health == 0:
                                print("Ну нарешті ти його прибив!")
                                inhabitants.remove(character)
                                to_kill -= 1
                            else:
                                print("Такс, ти йому вліпив")
                        elif character.fight(fight_with) == 'miss':
                            Character.hero_health -= 1
                            print("Нє, не вишло!")
                            if Character.hero_health <= 0:
                                # What happens if you lose?
                                print("Ой, здається, ти програв.")
                                print("То кінець гри.")

                    else:
                        print("В тебе немає " + fight_with)
                else:
                    print("Ти не можеш бити його з допомогою ")
            elif command == "take":
                if items is not None:
                    print("ти поклав "
                          + ', '.join([i.name for i in items])
                          + " до свого наплічника")
                    backpack.extend(items)
                    current_street.items = None
                else:
                    print("Тут порожньо, біг ме!")
            else:
                print("Щось тут не то. не вмію " + command)
            if current_street == kozelnytska:
                if to_kill <= 0 and Character.saved \
                        and witch not in kozelnytska.characters:
                    print("Єєєєй! ти виграв.")
                    dead = True
                elif to_kill >= 0:
                    print(' !> ти врятував Тетяну? {}\n'
                          ' !> ти вбив відьму? {}\n'
                          ' !> тобі лишилося вбити ще {} ворогів\n'
                          .format(Character.saved,
                                  witch in kozelnytska.characters,
                                  to_kill))
                else:
                    print(' !> ти врятував Тетяну? {}\n'
                          ' !> ти вбив відьму? {}\n'
                          .format(Character.saved,
                                  witch in kozelnytska.characters))
        except NameError:
            print("Перевір команду ще раз!")
            continue
        except KeyError:
            print('Неможливий напрям!')
        except ValueError:
            print('цього не було у списку!')

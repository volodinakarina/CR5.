from classes.arena.arena import Arena
from classes.hero.heroes import Heroes
from classes.equipments.equipments import Equipments
from classes.skills.skills import Skills

skills = Skills()
units = Heroes(skills.get_skills())
equipment = Equipments()

arena = Arena()
heroes = {
    "player": None,
    "enemy": None
}

result_choice_hero = {
    'header': 'Выберите героя',
    'classes': list(units.get_heroes().keys()),
    'weapons': equipment.get_weapons_names(),
    'armors': equipment.get_armors_names(),
}

result_choice_enemy = {
    'header': 'Выберите врага',
    'classes': list(units.get_heroes().keys()),
    'weapons': equipment.get_weapons_names(),
    'armors': equipment.get_armors_names(),
}
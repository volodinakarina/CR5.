from dataclasses import dataclass

from classes.skills.skill import Skill


@dataclass
class Hero:
    """
    Датакласс героя для игры
    """
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill
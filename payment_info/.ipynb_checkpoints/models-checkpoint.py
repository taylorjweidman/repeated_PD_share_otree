from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1
    
class Subsession(BaseSubsession):
    
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    
    payment_part_num = models.IntegerField()
    payment_cycle = models.IntegerField()
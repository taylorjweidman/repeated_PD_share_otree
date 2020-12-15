from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = """
This is a repeated Prisoner's Dilemma. A group of players are randomly matched each cycle. Within each cycle the
  players play an indefinitely repeated prisoners dilemma with a continuation probability.
"""

class Constants(BaseConstants):
    name_in_url = 'part_1'
    players_per_group = 2
    num_rounds = 40

    instructions_template = 'type_2_p1/Instructions.html'
    
    # Payoff Values
    high_reward = c(29/5)
    low_reward = c(11/5)
    effort_cost = c(9/5)

    # payoff if 1 player defects and the other cooperates
    betray_payoff = high_reward
    betrayed_payoff = low_reward - effort_cost

    # payoff if both players cooperate or both defect
    cooperate_payoff = high_reward - effort_cost
    defect_payoff = low_reward

    # DIE ROLL WAS DETERMINED USING
    die = die_rolls = [[22, 6, 58, 88, 75, 92, 85, 82, 46, 88, 1, 55, 52, 65, 89, 33, 46, 62, 69, 75, 21, 47, 2, 24, 68, 71, 39, 41, 63, 6],
       [31, 33, 67, 85, 26, 90, 100, 99, 50, 88, 20, 6, 66, 32, 31, 77, 94, 24, 26, 9, 98, 32, 100, 39, 39, 59, 31, 18, 38, 4],
       [83, 90, 68, 56, 57, 41, 64, 64, 19, 37, 58, 57, 1, 26, 65, 53, 78, 42, 33, 98, 11, 15, 81, 34, 58, 68, 61, 47, 18, 79],
       [92, 26, 7, 50, 9, 99, 99, 51, 41, 24, 44, 27, 23, 48, 16, 63, 34, 87, 28, 60, 2, 91, 65, 76, 2, 2, 53, 48, 7, 32],
       [70, 29, 0, 4, 34, 75, 95, 23, 90, 17, 16, 73, 60, 17, 58, 0, 15, 3, 41, 94, 18, 92, 75, 56, 61, 47, 19, 12, 74, 90],
       [27, 80, 56, 92, 97, 15, 89, 81, 81, 39, 79, 29, 25, 66, 35, 63, 86, 11, 34, 100, 7, 92, 24, 76, 17, 50, 25, 43, 16, 71],
       [67, 59, 5, 79, 47, 89, 68, 67, 94, 65, 48, 80, 65, 72, 75, 22, 12, 26, 90, 64, 91, 23, 72, 85, 2, 55, 46, 0, 28, 20],
       [91, 42, 88, 69, 7, 52, 98, 73, 93, 49, 12, 51, 91, 19, 7, 56, 49, 88, 14, 79, 13, 3, 72, 93, 85, 62, 21, 85, 35, 42],
       [18, 75, 27, 6, 23, 54, 62, 89, 73, 37, 99, 27, 6, 76, 29, 35, 55, 27, 56, 13, 16, 29, 3, 75, 90, 44, 76, 29, 84, 30],
       [64, 32, 69, 25, 32, 100, 5, 32, 56, 51, 8, 4, 44, 18, 30, 77, 96, 12, 89, 25, 0, 1, 88, 22, 67, 33, 99, 11, 8, 24],
       [20, 71, 52, 41, 48, 87, 10, 74, 63, 26, 11, 43, 41, 10, 92, 73, 26, 7, 50, 17, 9, 44, 81, 95, 33, 45, 58, 8, 6, 79],
       [39, 25, 12, 9, 1, 10, 19, 62, 16, 30, 48, 35, 8, 36, 89, 40, 57, 75, 85, 94, 56, 93, 40, 11, 30, 86, 37, 34, 28, 33],
       [3, 61, 62, 65, 62, 19, 58, 2, 39, 50, 14, 93, 60, 18, 71, 48, 20, 93, 59, 84, 27, 76, 79, 61, 76, 62, 61, 17, 30, 18],
       [30, 3, 43, 33, 1, 92, 61, 70, 65, 67, 55, 56, 64, 19, 45, 61, 43, 4, 8, 59, 72, 52, 19, 22, 70, 74, 50, 91, 12, 80],
       [85, 50, 5, 54, 66, 57, 43, 22, 52, 55, 61, 75, 0, 44, 98, 80, 17, 33, 44, 73, 48, 74, 77, 70, 32, 48, 40, 11, 38, 70],
       [4, 65, 2, 46, 100, 57, 3, 88, 19, 14, 65, 41, 81, 32, 91, 56, 70, 65, 12, 42, 64, 75, 14, 42, 13, 43, 6, 46, 32, 12],
       [76, 79, 44, 78, 17, 83, 17, 99, 83, 66, 76, 83, 70, 83, 55, 28, 58, 79, 94, 83, 35, 75, 46, 9, 46, 56, 17, 57, 51, 58],
       [27, 86, 3, 43, 39, 9, 4, 18, 40, 24, 1, 17, 63, 43, 82, 59, 87, 12, 38, 17, 49, 67, 47, 100, 58, 34, 30, 74, 47, 46],
       [85, 17, 50, 4, 3, 4, 22, 52, 71, 39, 35, 98, 47, 2, 52, 77, 55, 59, 62, 65, 58, 42, 59, 78, 59, 100, 41, 90, 40, 92],
       [74, 73, 64, 9, 92, 54, 34, 21, 18, 66, 21, 74, 61, 94, 26, 34, 2, 86, 19, 37, 61, 0, 6, 42, 21, 76, 91, 22, 88, 56],
       [6, 92, 57, 7, 66, 30, 44, 63, 53, 1, 23, 12, 70, 84, 15, 54, 1, 44, 33, 67, 78, 69, 74, 57, 12, 35, 71, 73, 43, 29],
       [89, 2, 99, 56, 36, 42, 55, 33, 16, 39, 88, 10, 72, 25, 62, 90, 90, 30, 28, 50, 28, 76, 21, 12, 74, 52, 19, 54, 47, 55],
       [60, 85, 37, 85, 7, 38, 24, 67, 40, 79, 96, 85, 19, 20, 96, 82, 27, 19, 30, 8, 12, 61, 3, 43, 77, 43, 42, 89, 72, 72],
       [98, 14, 16, 57, 52, 68, 48, 41, 100, 19, 43, 36, 15, 96, 39, 4, 84, 70, 43, 48, 5, 95, 25, 58, 7, 55, 26, 31, 98, 98],
       [18, 83, 85, 2, 44, 34, 4, 90, 19, 63, 68, 95, 26, 47, 43, 9, 26, 9, 13, 1, 48, 25, 16, 57, 68, 43, 84, 59, 14, 54],
       [92, 16, 55, 47, 25, 65, 1, 47, 59, 8, 60, 95, 22, 2, 34, 79, 72, 58, 61, 75, 24, 61, 68, 12, 66, 54, 41, 1, 88, 59],
       [28, 67, 34, 37, 31, 85, 15, 23, 6, 22, 80, 43, 71, 29, 82, 98, 98, 97, 20, 55, 4, 49, 18, 34, 73, 32, 4, 97, 84, 70],
       [10, 44, 1, 64, 49, 16, 40, 58, 11, 99, 24, 72, 39, 69, 53, 8, 67, 51, 15, 19, 6, 79, 95, 16, 88, 60, 40, 78, 5, 19],
       [48, 47, 92, 49, 13, 82, 74, 24, 11, 5, 15, 43, 56, 75, 86, 33, 74, 32, 78, 82, 16, 69, 73, 64, 97, 51, 16, 76, 62, 46],
       [11, 3, 59, 82, 24, 36, 22, 27, 50, 49, 70, 39, 64, 73, 58, 31, 48, 45, 56, 2, 3, 13, 20, 37, 66, 69, 81, 81, 60, 71]]
    
    groups_by_cycle_dict = {2: [],
                            4: [[[4, 1], [2, 3]],
                                [[3, 4], [2, 1]],
                                [[3, 1], [4, 2]],
                                [[3, 4], [2, 1]],
                                [[3, 1], [2, 4]],
                                [[4, 3], [1, 2]],
                                [[1, 3], [2, 4]],
                                [[4, 3], [2, 1]],
                                [[2, 3], [1, 4]],
                                [[3, 2], [4, 1]],
                                [[1, 3], [2, 4]],
                                [[1, 2], [4, 3]],
                                [[2, 1], [4, 3]],
                                [[3, 2], [1, 4]],
                                [[3, 1], [2, 4]],
                                [[3, 4], [2, 1]],
                                [[1, 2], [3, 4]],
                                [[4, 2], [3, 1]],
                                [[1, 2], [4, 3]],
                                [[2, 3], [4, 1]]]}

    # GROUPS BY CYCLE IS GENERATED USING
    # n = total number of players in session
    # numbers = random.sample(range(1, n + 1), n)
    # groups_by_cycle = []
    # for cycle in range(20):
    #     random.shuffle(numbers)
    #     groups_by_cycle.append([numbers[i:i+2] for i in range(0, len(numbers), group_size)])
    number_of_subjects = 4
    groups_by_cycle = groups_by_cycle_dict[number_of_subjects]

    Cycle_Condition_1 = 75 # Die roll is greater than
    Cycle_Condition_2 = 1 # Round number is greater than

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.session.get_participants():
            p.vars['round'] = 0
            p.vars['cycle'] = 1

    def set_groups(self):
        groups = Constants.groups_by_cycle[self.session.get_participants()[0].vars['cycle']]
        print(groups)
        self.set_group_matrix(groups)

class Group(BaseGroup):
    cycle = models.IntegerField(initial=1)

class Player(BasePlayer):
    cycle = models.IntegerField(initial=1)
    round = models.IntegerField(initial=1)
    decision = models.StringField(
        choices=['A', 'B'],
        doc="""This player's decision""",
        widget=widgets.RadioSelect
    )
    other_decision = models.StringField()
    die_roll = models.IntegerField()

    def new_cycle(self):
        self.round = 1
        self.cycle = self.participant.vars['cycle'] + 1
        self.participant.vars['cycle'] = self.cycle

    def new_round(self):
        self.round = self.participant.vars['round'] + 1
        self.participant.vars['round'] = self.round
        self.cycle = self.participant.vars['cycle']

    def set_payoff(self):
        payoff_matrix = {
            'A':{'A': Constants.cooperate_payoff,
                 'B': Constants.betrayed_payoff},
            'B':{'A': Constants.betray_payoff,
                 'B': Constants.defect_payoff}
        }
        self.payoff = payoff_matrix[self.decision][self.get_others_in_group()[0].decision]
        self.other_decision = self.get_others_in_group()[0].decision
        self.die_roll = Constants.die[self.cycle-1][self.participant.vars['round']-1]

    def store_vars(self):
        self.cycle = self.participant.vars['cycle'] + 1
        self.participant.vars['cycle'] = self.cycle
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Between_Rounds(WaitPage):

    wait_for_all_groups = True

    # ASSIGN GROUPS
    # UPDATE ROUND VARIABLES
    # GIVEN CONDITIONS:
    #     GENERATE A NEW CYCLE
    # PRINT

    def after_all_players_arrive(self):

        for p in self.subsession.get_players():                                                                 # Update Variables This Round
            print('Updating')
            p.new_round() 

        P = self.subsession.get_players()[0]                                                                    # REPRESENTATIVE PLAYER
        max_cycle_roll = max(Constants.die[P.participant.vars['cycle']-1][:P.participant.vars['round']])        # Maximum Die Roll This Cycle
        reveal_round = P.participant.vars['round']                                                              # This Round
        print(max_cycle_roll,reveal_round)

        if (max_cycle_roll > Constants.Cycle_Condition_1) & (reveal_round > Constants.Cycle_Condition_2):       # Given Cycle Conditions
            for p in self.subsession.get_players():                                                             # Generate New Cycle
                p.new_cycle()

        groups = Constants.groups_by_cycle[self.session.get_participants()[0].vars['cycle']]
        self.subsession.set_group_matrix(groups)

        print(' ')
        print('Round Number: ',P.round_number)
        print(' Groups:', groups)
        print(' Round: ',P.round)
        print(' Cycle: ',P.cycle)
        print(' Roll: ',P.die_roll)
        print(' Group 1: ',P.subsession.get_groups()[0].get_players())
        print(' Group 2: ', P.subsession.get_groups()[1].get_players())

class Introduction(Page):

    def is_displayed(self):
        P = self.subsession.get_players()[0]
        print('Cycle:',P.participant.vars['cycle'])
        print('Round:',P.participant.vars['round'])
        return (P.participant.vars['cycle'] == 1) & (P.participant.vars['round'] == 1)

class Decision(Page):
    form_model = 'player'
    form_fields = ['decision']

    def vars_for_template(self):
        round_number = self.player.round
        player_in_all_rounds = self.player.in_all_rounds()[-round_number:-1]
        opponent_in_all_rounds = self.player.get_others_in_group()[0].in_all_rounds()[-round_number:-1]
        return {'player_in_all_rounds': player_in_all_rounds,
                'opponent_in_all_rounds': opponent_in_all_rounds,
                'cycle':self.player.cycle,
                'round':round_number}

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()

class Results(Page):

    def vars_for_template(self):
        round_number = self.player.round
        player_in_all_rounds = self.player.in_all_rounds()[-round_number:]
        opponent_in_all_rounds = self.player.get_others_in_group()[0].in_all_rounds()[-round_number:]
        player_decision = self.player.decision
        opponent_decision = self.player.other_decision
        die_roll = self.player.die_roll
        
        def bindes(x):
            if x == 'A':
                return 1
            if x == 'B':
                return 2
        
        return {'player_in_all_rounds': player_in_all_rounds,
                'opponent_in_all_rounds': opponent_in_all_rounds,
                'player_decision':player_decision,
                'opponent_decision':opponent_decision,
                'cycle':self.player.cycle,
                'round':round_number,
                'die_roll':die_roll,
                'bin_own':bindes(str(player_decision)),
                'bin_other':bindes(str(opponent_decision))}

class Summary(Page):

    def is_displayed(self):
        p = self.subsession.get_players()[0]
        max_cycle_roll = max(Constants.die[p.participant.vars['cycle']-1][:p.participant.vars['round']])
        reveal_round = p.participant.vars['round']

        return (max_cycle_roll > 75) & (reveal_round > 2)

    def vars_for_template(self):
        round_number = self.player.round
        player_in_all_rounds = self.player.in_all_rounds()[-round_number:]
        opponent_in_all_rounds = self.player.get_others_in_group()[0].in_all_rounds()[-round_number:]
        player_decision = self.player.decision
        opponent_decision = self.player.other_decision
        die_roll = self.player.die_roll
        return {'player_in_all_rounds': player_in_all_rounds,
                'opponent_in_all_rounds': opponent_in_all_rounds,
                'player_decision':player_decision,
                'opponent_decision':opponent_decision,
                'cycle':self.player.cycle,
                'round':round_number,
                'die_roll':die_roll}

page_sequence = [
    Between_Rounds,
    Introduction,
    Decision,
    ResultsWaitPage,
    Results,
    Summary,
]

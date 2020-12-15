from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random

class PaymentInfo(Page):

    def vars_for_template(self):

        p = self.participant
        
        payment_part_num = p.vars['payment_part_num']
        payment_cycle = p.vars['payment_cycle']
        
        self.player.payment_part_num = payment_part_num
        self.player.payment_cycle = payment_cycle

        payment_part = ['p1_payment','p2_payment'][payment_part_num-1]
        part_round = ['p1_payment_round','p2_payment_round'][payment_part_num-1]
        cycle_round = p.vars[part_round][payment_cycle-1]

        participation_fee = c(6)
        payoff = p.vars[payment_part][payment_cycle-1]

        p.payoff = payoff + participation_fee
        
        return {
            'payment_part': payment_part_num,
            'payment_cycle': payment_cycle,
            'cycle_round': cycle_round,
            'payoff': self.participant.payoff - c(6),
            'total_payoff': self.participant.payoff,
            'redemption_code': self.participant.label,
        }
    
class ThankYou(Page):
    def vars_for_template(self):

        return {
            'redemption_code': self.participant.label,
        }

page_sequence = [PaymentInfo,
                ThankYou]

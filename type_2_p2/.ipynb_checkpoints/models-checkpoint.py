from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = """
This is a repeated Prisoner's Dilemma. A group of players are randomly matched each cycle. Within each cycle the
  players play an indefinitely repeated prisoners dilemma with a continuation probability.
"""

class Constants(BaseConstants):
    name_in_url = 't2p2'
    players_per_group = 4
    num_rounds = 70
    
    session_number = 1 # 1,2,3

    instructions_template = 'type_2_p1/Instructions.html'
    
    # Payoff Values
    high_reward = c(29)
    low_reward = c(11)
    effort_cost = c(9)

    # Payoff if 1 player defects and the other cooperates
    betray_payoff = high_reward
    betrayed_payoff = low_reward - effort_cost

    # Payoff if both players cooperate or both defect
    cooperate_payoff = high_reward - effort_cost
    defect_payoff = low_reward

    # DIE ROLL WAS DETERMINED USING
    # [random.sample(range(1,101),30) for x in range(30)]
    die_dict = {
        1:[[53, 45, 68, 80, 36, 91, 67, 29, 43, 96, 4, 26, 14, 71, 81, 64, 48, 69, 17, 5, 85, 30, 78, 35, 58, 83, 19, 70, 31, 61],
           [18, 62, 20, 60, 41, 97, 65, 76, 49, 11, 90, 46, 25, 23, 21, 30, 4, 27, 51, 59, 24, 61, 9, 36, 17, 34, 40, 54, 79, 22],
           [22, 15, 90, 8, 96, 10, 4, 20, 92, 57, 50, 35, 1, 53, 18, 73, 91, 61, 6, 41, 69, 64, 83, 86, 94, 32, 81, 77, 68, 60], 
           [93, 76, 54, 32, 14, 66, 69, 2, 30, 90, 43, 29, 70, 60, 18, 55, 35, 6, 78, 17, 53, 52, 83, 50, 41, 99, 8, 48, 59, 37], 
           [63, 13, 8, 36, 78, 84, 7, 60, 26, 17, 29, 82, 31, 28, 56, 50, 64, 86, 43, 89, 40, 67, 72, 45, 79, 77, 41, 61, 6, 83], 
           [19, 84, 54, 49, 65, 7, 37, 20, 2, 16, 24, 41, 38, 57, 71, 21, 1, 9, 56, 82, 3, 34, 81, 70, 52, 61, 50, 45, 1, 18], 
           [63, 80, 86, 79, 41, 83, 84, 93, 33, 92, 32, 38, 68, 66, 96, 26, 98, 37, 16, 64, 59, 18, 25, 70, 71, 67, 51, 65, 45, 36],
           [44, 31, 47, 32, 5, 78, 51, 52, 91, 7, 1, 38, 12, 75, 59, 8, 77, 70, 21, 33, 41, 46, 55, 18, 56, 63, 14, 20, 40, 81], 
           [94, 53, 66, 80, 35, 74, 22, 54, 1, 59, 92, 57, 73, 60, 84, 6, 16, 3, 8, 45, 7, 40, 93, 23, 51, 4, 71, 99, 67, 78], 
           [89, 38, 96, 46, 70, 81, 98, 72, 62, 60, 6, 35, 95, 71, 47, 19, 25, 33, 80, 40, 93, 20, 68, 26, 74, 12, 90, 18, 92, 76],
           [10, 79, 54, 18, 96, 53, 55, 46, 51, 4, 88, 16, 80, 70, 98, 23, 50, 37, 42, 15, 22, 90, 62, 2, 68, 67, 81, 75, 73, 87],
           [80, 28, 99, 31, 79, 52, 34, 43, 27, 75, 69, 20, 93, 95, 23, 77, 63, 83, 73, 16, 8, 82, 25, 61, 6, 11, 32, 55, 66, 85],
           [6, 26, 90, 50, 14, 34, 80, 85, 43, 16, 29, 42, 95, 60, 94, 98, 1, 83, 47, 8, 32, 41, 68, 12, 28, 1, 35, 53, 19, 24],
           [18, 89, 75, 45, 82, 99, 44, 65, 93, 61, 17, 11, 91, 42, 55, 2, 85, 15, 77, 56, 34, 31, 52, 70, 13, 32, 38, 3, 69, 0],
           [99, 39, 8, 42, 79, 7, 35, 51, 9, 34, 85, 1, 54, 27, 23, 53, 41, 38, 20, 81, 58, 64, 88, 75, 91, 97, 57, 78, 70, 11],
           [30, 55, 36, 84, 44, 52, 46, 33, 71, 60, 74, 78, 66, 1, 24, 90, 67, 94, 49, 51, 91, 95, 26, 21, 28, 68, 37, 54, 5, 19],
           [49, 25, 79, 47, 18, 72, 4, 7, 23, 70, 91, 9, 40, 95, 99, 35, 50, 54, 46, 16, 86, 76, 66, 42, 74, 71, 12, 68, 1, 73],
           [76, 69, 29, 80, 65, 36, 85, 7, 46, 81, 41, 75, 15, 5, 55, 72, 37, 52, 78, 38, 99, 89, 97, 94, 47, 4, 32, 26, 74, 48],
           [91, 87, 67, 99, 75, 63, 81, 1, 29, 59, 76, 28, 45, 96, 57, 97, 14, 62, 88, 38, 44, 7, 9, 98, 11, 27, 56, 6, 64, 71],
           [95, 85, 21, 81, 34, 78, 87, 90, 37, 82, 89, 55, 47, 93, 45, 96, 54, 53, 20, 36, 80, 61, 60, 73, 24, 65, 3, 6, 76, 15],
           [86, 11, 66, 85, 53, 35, 46, 22, 84, 57, 87, 97, 23, 67, 41, 77, 50, 76, 2, 73, 1, 78, 1, 92, 99, 6, 68, 34, 47, 62],
           [99, 32, 17, 19, 38, 24, 29, 20, 71, 13, 2, 45, 46, 68, 31, 7, 66, 64, 28, 73, 25, 4, 3, 98, 74, 1, 96, 1, 69, 72],
           [69, 87, 27, 57, 90, 62, 98, 80, 85, 26, 91, 93, 50, 81, 88, 51, 65, 66, 46, 1, 13, 54, 33, 38, 61, 10, 84, 64, 35, 30],
           [36, 86, 52, 23, 59, 90, 65, 88, 30, 21, 55, 31, 78, 82, 1, 11, 51, 19, 8, 27, 80, 75, 43, 71, 93, 44, 12, 85, 25, 77],
           [56, 51, 37, 89, 80, 93, 87, 75, 11, 19, 45, 1, 17, 3, 83, 55, 12, 78, 38, 54, 33, 8, 88, 70, 1, 44, 41, 7, 25, 6],
           [84, 8, 39, 71, 36, 65, 85, 51, 26, 50, 38, 55, 58, 80, 92, 37, 14, 93, 1, 88, 48, 6, 32, 66, 30, 42, 59, 19, 5, 11],
           [71, 11, 5, 94, 43, 34, 9, 98, 35, 47, 89, 91, 40, 50, 68, 36, 2, 67, 24, 59, 86, 55, 80, 8, 32, 72, 1, 20, 28, 3],
           [87, 86, 73, 58, 18, 94, 81, 80, 46, 62, 92, 69, 51, 61, 28, 22, 77, 53, 25, 83, 76, 52, 30, 29, 7, 84, 19, 50, 8, 34],
           [0, 53, 34, 14, 39, 74, 21, 27, 24, 57, 52, 1, 86, 11, 28, 17, 83, 71, 75, 30, 54, 18, 90, 45, 85, 16, 79, 59, 33, 12],
           [93, 99, 74, 73, 85, 68, 22, 38, 36, 97, 2, 59, 13, 89, 58, 41, 21, 79, 72, 24, 20, 40, 81, 57, 55, 95, 8, 25, 86, 4]],
        2:[[53, 45, 68, 80, 36, 91, 67, 29, 43, 96, 4, 26, 14, 71, 81, 64, 48, 69, 17, 5, 85, 30, 78, 35, 58, 83, 19, 70, 31, 61],
           [18, 62, 20, 60, 41, 97, 65, 76, 49, 11, 90, 46, 25, 23, 21, 30, 4, 27, 51, 59, 24, 61, 9, 36, 17, 34, 40, 54, 79, 22],
           [22, 15, 90, 8, 96, 10, 4, 20, 92, 57, 50, 35, 1, 53, 18, 73, 91, 61, 6, 41, 69, 64, 83, 86, 94, 32, 81, 77, 68, 60], 
           [93, 76, 54, 32, 14, 66, 69, 2, 30, 90, 43, 29, 70, 60, 18, 55, 35, 6, 78, 17, 53, 52, 83, 50, 41, 99, 8, 48, 59, 37], 
           [63, 13, 8, 36, 78, 84, 7, 60, 26, 17, 29, 82, 31, 28, 56, 50, 64, 86, 43, 89, 40, 67, 72, 45, 79, 77, 41, 61, 6, 83], 
           [19, 84, 54, 49, 65, 7, 37, 20, 2, 16, 24, 41, 38, 57, 71, 21, 1, 9, 56, 82, 3, 34, 81, 70, 52, 61, 50, 45, 1, 18], 
           [63, 80, 86, 79, 41, 83, 84, 93, 33, 92, 32, 38, 68, 66, 96, 26, 98, 37, 16, 64, 59, 18, 25, 70, 71, 67, 51, 65, 45, 36],
           [44, 31, 47, 32, 5, 78, 51, 52, 91, 7, 1, 38, 12, 75, 59, 8, 77, 70, 21, 33, 41, 46, 55, 18, 56, 63, 14, 20, 40, 81], 
           [94, 53, 66, 80, 35, 74, 22, 54, 1, 59, 92, 57, 73, 60, 84, 6, 16, 3, 8, 45, 7, 40, 93, 23, 51, 4, 71, 99, 67, 78], 
           [89, 38, 96, 46, 70, 81, 98, 72, 62, 60, 6, 35, 95, 71, 47, 19, 25, 33, 80, 40, 93, 20, 68, 26, 74, 12, 90, 18, 92, 76],
           [10, 79, 54, 18, 96, 53, 55, 46, 51, 4, 88, 16, 80, 70, 98, 23, 50, 37, 42, 15, 22, 90, 62, 2, 68, 67, 81, 75, 73, 87],
           [80, 28, 99, 31, 79, 52, 34, 43, 27, 75, 69, 20, 93, 95, 23, 77, 63, 83, 73, 16, 8, 82, 25, 61, 6, 11, 32, 55, 66, 85],
           [6, 26, 90, 50, 14, 34, 80, 85, 43, 16, 29, 42, 95, 60, 94, 98, 1, 83, 47, 8, 32, 41, 68, 12, 28, 1, 35, 53, 19, 24],
           [18, 89, 75, 45, 82, 99, 44, 65, 93, 61, 17, 11, 91, 42, 55, 2, 85, 15, 77, 56, 34, 31, 52, 70, 13, 32, 38, 3, 69, 0],
           [99, 39, 8, 42, 79, 7, 35, 51, 9, 34, 85, 1, 54, 27, 23, 53, 41, 38, 20, 81, 58, 64, 88, 75, 91, 97, 57, 78, 70, 11],
           [30, 55, 36, 84, 44, 52, 46, 33, 71, 60, 74, 78, 66, 1, 24, 90, 67, 94, 49, 51, 91, 95, 26, 21, 28, 68, 37, 54, 5, 19],
           [49, 25, 79, 47, 18, 72, 4, 7, 23, 70, 91, 9, 40, 95, 99, 35, 50, 54, 46, 16, 86, 76, 66, 42, 74, 71, 12, 68, 1, 73],
           [76, 69, 29, 80, 65, 36, 85, 7, 46, 81, 41, 75, 15, 5, 55, 72, 37, 52, 78, 38, 99, 89, 97, 94, 47, 4, 32, 26, 74, 48],
           [91, 87, 67, 99, 75, 63, 81, 1, 29, 59, 76, 28, 45, 96, 57, 97, 14, 62, 88, 38, 44, 7, 9, 98, 11, 27, 56, 6, 64, 71],
           [95, 85, 21, 81, 34, 78, 87, 90, 37, 82, 89, 55, 47, 93, 45, 96, 54, 53, 20, 36, 80, 61, 60, 73, 24, 65, 3, 6, 76, 15],
           [86, 11, 66, 85, 53, 35, 46, 22, 84, 57, 87, 97, 23, 67, 41, 77, 50, 76, 2, 73, 1, 78, 1, 92, 99, 6, 68, 34, 47, 62],
           [99, 32, 17, 19, 38, 24, 29, 20, 71, 13, 2, 45, 46, 68, 31, 7, 66, 64, 28, 73, 25, 4, 3, 98, 74, 1, 96, 1, 69, 72],
           [69, 87, 27, 57, 90, 62, 98, 80, 85, 26, 91, 93, 50, 81, 88, 51, 65, 66, 46, 1, 13, 54, 33, 38, 61, 10, 84, 64, 35, 30],
           [36, 86, 52, 23, 59, 90, 65, 88, 30, 21, 55, 31, 78, 82, 1, 11, 51, 19, 8, 27, 80, 75, 43, 71, 93, 44, 12, 85, 25, 77],
           [56, 51, 37, 89, 80, 93, 87, 75, 11, 19, 45, 1, 17, 3, 83, 55, 12, 78, 38, 54, 33, 8, 88, 70, 1, 44, 41, 7, 25, 6],
           [84, 8, 39, 71, 36, 65, 85, 51, 26, 50, 38, 55, 58, 80, 92, 37, 14, 93, 1, 88, 48, 6, 32, 66, 30, 42, 59, 19, 5, 11],
           [71, 11, 5, 94, 43, 34, 9, 98, 35, 47, 89, 91, 40, 50, 68, 36, 2, 67, 24, 59, 86, 55, 80, 8, 32, 72, 1, 20, 28, 3],
           [87, 86, 73, 58, 18, 94, 81, 80, 46, 62, 92, 69, 51, 61, 28, 22, 77, 53, 25, 83, 76, 52, 30, 29, 7, 84, 19, 50, 8, 34],
           [0, 53, 34, 14, 39, 74, 21, 27, 24, 57, 52, 1, 86, 11, 28, 17, 83, 71, 75, 30, 54, 18, 90, 45, 85, 16, 79, 59, 33, 12],
           [93, 99, 74, 73, 85, 68, 22, 38, 36, 97, 2, 59, 13, 89, 58, 41, 21, 79, 72, 24, 20, 40, 81, 57, 55, 95, 8, 25, 86, 4]],
        3:[[46, 75, 58, 19, 5, 39, 97, 88, 43, 98, 68, 7, 38, 24, 15, 45, 52, 71, 9, 78, 26, 13, 22, 62, 35, 30, 36, 51, 33, 49],
           [41, 8, 81, 20, 17, 79, 50, 34, 84, 94, 39, 10, 70, 7, 56, 31, 73, 80, 26, 32, 48, 51, 69, 46, 22, 71, 57, 37, 21, 85],
           [73, 38, 63, 53, 82, 8, 26, 20, 87, 77, 44, 80, 13, 70, 79, 47, 1, 27, 98, 69, 93, 50, 52, 58, 29, 7, 64, 83, 17, 66],
           [36, 90, 4, 5, 9, 53, 19, 98, 74, 13, 70, 28, 11, 91, 86, 59, 34, 96, 50, 84, 72, 38, 76, 33, 71, 8, 62, 21, 58, 27],
           [74, 14, 72, 10, 65, 80, 56, 99, 54, 41, 55, 57, 36, 82, 13, 92, 30, 95, 35, 77, 91, 1, 76, 52, 32, 48, 53, 21, 58, 2],
           [28, 43, 2, 30, 55, 59, 51, 44, 19, 89, 4, 41, 21, 14, 12, 49, 15, 67, 9, 3, 87, 62, 37, 39, 83, 47, 61, 31, 86, 34],
           [75, 68, 70, 5, 88, 10, 29, 89, 84, 40, 36, 22, 97, 65, 93, 74, 48, 1, 94, 31, 72, 11, 49, 92, 3, 6, 4, 12, 47, 7],
           [59, 33, 76, 88, 7, 24, 39, 29, 67, 14, 65, 51, 66, 75, 62, 68, 85, 48, 71, 61, 22, 1, 25, 49, 10, 60, 55, 57, 74, 27],
           [7, 42, 22, 18, 80, 90, 56, 5, 49, 11, 19, 2, 4, 81, 3, 37, 14, 52, 32, 17, 38, 75, 82, 35, 21, 69, 93, 79, 47, 83],
           [76, 11, 52, 73, 93, 49, 27, 40, 60, 72, 58, 66, 77, 26, 84, 17, 12, 1, 82, 46, 29, 4, 33, 48, 54, 51, 97, 30, 14, 25],
           [52, 91, 65, 8, 92, 81, 45, 37, 64, 60, 18, 6, 63, 47, 99, 66, 51, 73, 98, 53, 89, 78, 61, 36, 87, 21, 20, 16, 83, 30],
           [79, 97, 28, 49, 38, 56, 24, 88, 9, 65, 72, 32, 84, 41, 51, 50, 67, 3, 1, 73, 93, 23, 82, 95, 18, 91, 81, 78, 66, 47],
           [56, 1, 10, 4, 34, 59, 73, 96, 12, 28, 15, 51, 57, 99, 42, 87, 11, 82, 9, 33, 97, 17, 54, 25, 26, 1, 5, 47, 18, 89],
           [45, 37, 71, 4, 9, 12, 13, 39, 69, 81, 50, 38, 65, 78, 97, 53, 86, 63, 22, 44, 3, 76, 43, 74, 66, 46, 85, 2, 47, 79],
           [54, 39, 49, 14, 84, 2, 90, 18, 59, 53, 80, 79, 56, 70, 27, 51, 64, 26, 42, 36, 16, 83, 88, 19, 57, 74, 61, 85, 96, 43],
           [75, 60, 42, 20, 71, 63, 94, 95, 39, 37, 67, 48, 7, 34, 56, 91, 93, 76, 97, 24, 54, 55, 30, 68, 61, 70, 3, 86, 64, 26],
           [43, 44, 90, 11, 22, 19, 78, 37, 45, 56, 85, 47, 41, 77, 94, 21, 63, 23, 79, 66, 91, 38, 73, 71, 48, 1, 18, 32, 50, 24],
           [70, 22, 6, 61, 37, 31, 67, 50, 52, 45, 39, 79, 4, 86, 27, 73, 44, 55, 71, 7, 30, 66, 1, 13, 99, 24, 18, 81, 19, 56],
           [33, 7, 14, 29, 58, 98, 66, 38, 73, 63, 85, 24, 81, 28, 52, 71, 31, 22, 48, 16, 25, 6, 72, 3, 86, 59, 20, 34, 62, 51],
           [65, 16, 78, 44, 36, 80, 20, 15, 27, 12, 43, 55, 99, 10, 74, 81, 32, 35, 90, 66, 85, 26, 60, 72, 37, 30, 82, 63, 22, 33],
           [3, 28, 88, 39, 76, 87, 51, 91, 35, 99, 7, 29, 1, 81, 46, 16, 61, 38, 78, 74, 75, 36, 77, 4, 93, 72, 9, 10, 82, 66],
           [80, 60, 2, 5, 98, 32, 33, 99, 65, 51, 56, 87, 84, 76, 74, 38, 29, 1, 82, 3, 4, 25, 71, 23, 40, 11, 16, 27, 81, 70],
           [92, 90, 41, 70, 35, 12, 29, 65, 98, 57, 45, 88, 38, 7, 49, 52, 61, 63, 67, 89, 42, 5, 81, 85, 30, 15, 71, 26, 20, 9],
           [50, 31, 60, 74, 98, 66, 34, 97, 47, 21, 1, 40, 90, 54, 62, 18, 67, 8, 59, 44, 14, 92, 99, 13, 85, 38, 4, 65, 32, 91],
           [68, 44, 85, 58, 76, 10, 96, 84, 52, 50, 1, 95, 93, 3, 86, 22, 79, 49, 62, 66, 89, 1, 5, 60, 11, 56, 13, 48, 61, 87],
           [46, 48, 21, 65, 44, 49, 24, 7, 5, 6, 25, 78, 62, 39, 82, 67, 45, 87, 23, 53, 37, 16, 2, 33, 83, 19, 22, 8, 50, 84],
           [62, 12, 34, 13, 65, 80, 54, 94, 28, 33, 99, 42, 38, 37, 2, 3, 52, 83, 73, 26, 45, 8, 97, 29, 90, 81, 31, 14, 49, 11],
           [88, 82, 26, 76, 27, 89, 86, 87, 75, 68, 14, 63, 67, 98, 73, 92, 53, 22, 6, 29, 20, 5, 65, 1, 94, 58, 66, 1, 62, 48],
           [71, 59, 92, 52, 53, 72, 56, 66, 84, 81, 95, 80, 48, 60, 88, 20, 49, 77, 24, 61, 11, 14, 93, 16, 57, 7, 46, 99, 50, 15],
           [51, 81, 4, 29, 23, 78, 28, 24, 60, 21, 15, 9, 11, 26, 38, 3, 91, 70, 8, 16, 17, 62, 87, 14, 39, 86, 1, 63, 46, 68]]
    }
    die = die_dict[session_number]

    # GROUPS BY CYCLE IS GENERATED USING
    #def groupcycle(n,g):
    #    groups_by_cycle = []
    #    numbers = random.sample(range(1,n+1),n)
    #    for c in range(11):
    #        random.shuffle(numbers)
    #        groups_by_cycle.append([numbers[i:i+g] for i in range(0,len(numbers),g)])
    #    return groups_by_cycle
    
    groups_by_cycle_dict = {4: [[[3, 2, 1, 4]], 
                                [[1, 2, 4, 3]], 
                                [[2, 4, 3, 1]], 
                                [[4, 2, 1, 3]], 
                                [[3, 2, 4, 1]], 
                                [[2, 3, 4, 1]], 
                                [[4, 1, 2, 3]], 
                                [[1, 4, 3, 2]], 
                                [[1, 2, 4, 3]], 
                                [[1, 3, 2, 4]],
                                [[3, 2, 1, 4]]],
                            16: [[[1, 11, 5, 12], [7, 8, 13, 16], [15, 10, 3, 14], [6, 9, 4, 2]], 
                                 [[1, 13, 12, 3], [15, 11, 4, 8], [14, 10, 7, 2], [9, 16, 6, 5]], 
                                 [[6, 3, 14, 8], [13, 5, 7, 12], [10, 9, 4, 2], [15, 11, 1, 16]], 
                                 [[6, 12, 1, 8], [3, 15, 14, 9], [5, 13, 11, 4], [7, 16, 10, 2]], 
                                 [[3, 2, 15, 10], [9, 12, 14, 13], [16, 4, 11, 5], [8, 6, 1, 7]], 
                                 [[13, 12, 10, 1], [7, 11, 15, 16], [6, 8, 3, 2], [5, 14, 9, 4]], 
                                 [[6, 5, 15, 12], [16, 9, 3, 4], [13, 10, 14, 7], [1, 11, 8, 2]], 
                                 [[8, 7, 9, 14], [11, 6, 2, 16], [4, 15, 12, 5], [10, 1, 13, 3]], 
                                 [[2, 1, 9, 8], [15, 4, 14, 10], [16, 5, 6, 7], [11, 12, 13, 3]], 
                                 [[12, 3, 4, 8], [1, 15, 16, 2], [5, 6, 10, 13], [7, 9, 11, 14]],
                                 [[1, 11, 5, 12], [7, 8, 13, 16], [15, 10, 3, 14], [6, 9, 4, 2]]],
                            20: [[[7, 4, 14, 13], [1, 11, 6, 8], [10, 17, 2, 20], [15, 19, 12, 3], [5, 9, 18, 16]],
                                 [[3, 7, 20, 18], [4, 14, 1, 12], [5, 10, 8, 13], [17, 6, 16, 19], [9, 2, 11, 15]],
                                 [[7, 14, 16, 15], [17, 20, 11, 2], [10, 13, 9, 12], [4, 1, 18, 5], [3, 6, 19, 8]],
                                 [[9, 20, 19, 15], [13, 7, 10, 14], [6, 1, 12, 3], [2, 5, 4, 16], [18, 8, 17, 11]],
                                 [[13, 20, 1, 4], [15, 11, 9, 8], [3, 5, 14, 12], [19, 17, 6, 2], [18, 16, 10, 7]],
                                 [[12, 10, 18, 17], [1, 2, 11, 15], [5, 16, 4, 8], [7, 6, 3, 13], [19, 14, 20, 9]],
                                 [[1, 7, 3, 17], [16, 20, 10, 15], [12, 5, 4, 6], [19, 8, 9, 18], [11, 2, 13, 14]],
                                 [[13, 12, 8, 20], [3, 4, 10, 2], [16, 9, 19, 18], [14, 15, 6, 5], [17, 7, 11, 1]],
                                 [[8, 16, 9, 1], [19, 15, 20, 6], [3, 2, 10, 17], [5, 7, 12, 11], [14, 18, 13, 4]],
                                 [[9, 3, 12, 13], [2, 10, 11, 6], [15, 14, 4, 5], [8, 18, 7, 17], [1, 16, 20, 19]],
                                 [[7, 4, 14, 13], [1, 11, 6, 8], [10, 17, 2, 20], [15, 19, 12, 3], [5, 9, 18, 16]]],
                           24: [[[8, 17, 9, 3], [23, 22, 16, 10], [6, 13, 7, 11], [19, 5, 20, 14], [1, 4, 2, 18], [12, 15, 24, 21]], 
                                [[3, 5, 19, 12], [16, 24, 18, 15], [4, 21, 1, 9], [22, 14, 23, 6], [20, 8, 7, 13], [2, 11, 17, 10]], 
                                [[16, 15, 8, 10], [24, 1, 23, 5], [13, 20, 14, 17], [12, 9, 11, 6], [7, 22, 2, 19], [21, 18, 4, 3]], 
                                [[18, 7, 22, 21], [15, 10, 19, 13], [23, 14, 24, 11], [2, 5, 1, 8], [17, 9, 6, 20], [12, 4, 16, 3]], 
                                [[20, 23, 17, 5], [22, 2, 13, 1], [11, 10, 4, 9], [19, 12, 14, 21], [8, 16, 15, 3], [6, 24, 7, 18]], 
                                [[4, 14, 21, 13], [8, 7, 20, 16], [19, 17, 22, 6], [12, 2, 1, 15], [11, 18, 5, 24], [3, 9, 10, 23]], 
                                [[5, 22, 4, 20], [2, 1, 11, 13], [23, 7, 9, 18], [3, 6, 24, 10], [14, 15, 21, 8], [17, 12, 19, 16]], 
                                [[14, 24, 23, 3], [15, 10, 22, 1], [12, 19, 5, 13], [16, 2, 18, 7], [17, 4, 21, 11], [9, 20, 6, 8]], 
                                [[23, 20, 11, 24], [16, 3, 22, 2], [6, 18, 12, 15], [21, 1, 4, 14], [13, 17, 7, 9], [8, 19, 10, 5]], 
                                [[1, 23, 12, 9], [7, 8, 16, 2], [15, 21, 18, 10], [14, 3, 13, 22], [11, 17, 19, 6], [20, 24, 5, 4]],
                                [[8, 17, 9, 3], [23, 22, 16, 10], [6, 13, 7, 11], [19, 5, 20, 14], [1, 4, 2, 18], [12, 15, 24, 21]]]}
    
    number_of_subjects = 4
    groups_by_cycle = groups_by_cycle_dict[number_of_subjects]

    Cycle_Condition_1 = 75 # Die roll is greater than
    Cycle_Condition_2 = 5  # Round number is greater than
    Cycle_Condition_3 = 10 # Number of cycles

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.session.get_participants():
            p.vars['p2_round'] = 0
            p.vars['p2_cycle'] = 1
            p.vars['p2_payment_round'] = list([])
            p.vars['p2_payment'] = list([])

class Group(BaseGroup):
    p2_cycle = models.IntegerField(initial=1)

class Player(BasePlayer):
    p2_cycle = models.IntegerField(initial=1)
    p2_round = models.IntegerField(initial=1)
    decision = models.StringField()
    group_decision = models.StringField()
    die_roll = models.IntegerField()

    def new_cycle(self):
        self.p2_round = 1
        self.participant.vars['p2_round'] = self.p2_round
        self.p2_cycle = self.participant.vars['p2_cycle'] + 1
        self.participant.vars['p2_cycle'] = self.p2_cycle

    def new_round(self):
        self.p2_round = self.participant.vars['p2_round'] + 1
        self.participant.vars['p2_round'] = self.p2_round
        self.p2_cycle = self.participant.vars['p2_cycle']

    def set_payoff(self):
        payoff_matrix = {
            'Green':{'All 3 Green': Constants.cooperate_payoff,
                 'Any of 3 Red': Constants.betrayed_payoff},
            'Red':{'All 3 Green': Constants.betray_payoff,
                 'Any of 3 Red': Constants.defect_payoff}
        }
        self.payoff = payoff_matrix[self.decision][self.group_decision]
        self.die_roll = Constants.die[self.p2_cycle-1][self.participant.vars['p2_round']-1]

    def store_vars(self):
        self.p2_cycle = self.participant.vars['p2_cycle'] + 1
        self.participant.vars['p2_cycle'] = self.p2_cycle

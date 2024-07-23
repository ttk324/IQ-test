
from otree.api import *
c = cu

doc = ''
class Constants(BaseConstants):
    name_in_url = 'Tiffany_Raven_Kamei'
    players_per_group = None
    num_rounds = 1
    Q1_A = 5
    Q2_A = 3
    Q3_A = 5
    Q4_A = 3
    Q5_A = 1
    Q6_A = 4
    Q7_A = 3
    Q8_A = 1
    Q9_A = 6
    Q10_A = 4
    Q11_A = 2
    Q12_A = 4
    Q13_A = 1
    Q14_A = 5
    Q15_A = 7
    CA_EXCHANGERATE = 10
    WA_EXCHANGERATE = 2
class Subsession(BaseSubsession):
    pass
def set_payoffs(subsession: Subsession):
    session = subsession.session
    for p in subsession.get_players():
        set_payoff(p)
    
    
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    Q1 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q2 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q3 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q4 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q5 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q6 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q7 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q8 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q9 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q10 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q11 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q12 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q13 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q14 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    Q15 = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8']], initial=-1, label=' あなたの答え', widget=widgets.RadioSelectHorizontal)
    numberofcorrectanswers = models.IntegerField(initial=0)
    numberofwronganswer = models.IntegerField()
    payofftoshow = models.IntegerField()
def set_payoff(player: Player):
    if player.Q1==Constants.Q1_A:
        ans1=1
    else:
        ans1=0
    if player.Q2==Constants.Q2_A:
        ans2=1
    else:
        ans2=0    
    if player.Q3==Constants.Q3_A:
        ans3=1
    else:
        ans3=0
    if player.Q4==Constants.Q4_A:
        ans4=1
    else:
        ans4=0    
    if player.Q5==Constants.Q5_A:
        ans5=1
    else:
        ans5=0
    if player.Q6==Constants.Q6_A:
        ans6=1
    else:
        ans6=0        
    if player.Q7==Constants.Q7_A:
        ans7=1
    else:
        ans7=0 
    if player.Q8==Constants.Q8_A:
        ans8=1
    else:
        ans8=0
    if player.Q9==Constants.Q9_A:
        ans9=1
    else:
        ans9=0 
    if player.Q10==Constants.Q10_A:
        ans10=1
    else:
        ans10=0
    if player.Q11==Constants.Q11_A:
        ans11=1
    else:
        ans11=0
    if player.Q12==Constants.Q12_A:
        ans12=1
    else:
        ans12=0
    if player.Q13==Constants.Q13_A:
        ans13=1
    else:
        ans13=0
    if player.Q14==Constants.Q14_A:
        ans14=1
    else:
        ans14=0
    if player.Q15==Constants.Q15_A:
        ans15=1
    else:
        ans15=0

    player.numberofcorrectanswers=ans1+ans2+ans3+ans4+ans5+ans6+ans7+ans8+ans9+ans10+ans11+ans12+ans13+ans14+ans15
    player.numberofwronganswer=15-player.numberofcorrectanswers
    
    player.payoff=(player.numberofcorrectanswers*Constants.CA_EXCHANGERATE-player.numberofwronganswer*Constants.WA_EXCHANGERATE) #depends on the exchange rate
    
    player.payofftoshow=player.numberofcorrectanswers*Constants.CA_EXCHANGERATE-player.numberofwronganswer*Constants.WA_EXCHANGERATE

    # set payoff as global variable
    participant = player.participant
    participant.vars['IQ_payoff'] = player.payofftoshow

class Instruction(Page):
    form_model = 'player'
class Waitforeveryone(WaitPage):
    wait_for_all_groups = True
class Q1(Page):
    form_model = 'player'
    form_fields = ['Q1']
    timeout_seconds = 60
class Q2(Page):
    form_model = 'player'
    form_fields = ['Q2']
    timeout_seconds = 60
class Q3(Page):
    form_model = 'player'
    form_fields = ['Q3']
    timeout_seconds = 60
class Q4(Page):
    form_model = 'player'
    form_fields = ['Q4']
    timeout_seconds = 60
class Q5(Page):
    form_model = 'player'
    form_fields = ['Q5']
    timeout_seconds = 60
class Q6(Page):
    form_model = 'player'
    form_fields = ['Q6']
    timeout_seconds = 60
class Q7(Page):
    form_model = 'player'
    form_fields = ['Q7']
    timeout_seconds = 60
class Q8(Page):
    form_model = 'player'
    form_fields = ['Q8']
    timeout_seconds = 60
class Q9(Page):
    form_model = 'player'
    form_fields = ['Q9']
    timeout_seconds = 60
class Q10(Page):
    form_model = 'player'
    form_fields = ['Q10']
    timeout_seconds = 60
class Q11(Page):
    form_model = 'player'
    form_fields = ['Q11']
    timeout_seconds = 60
class Q12(Page):
    form_model = 'player'
    form_fields = ['Q12']
    timeout_seconds = 60
class Q13(Page):
    form_model = 'player'
    form_fields = ['Q13']
    timeout_seconds = 60
class Q14(Page):
    form_model = 'player'
    form_fields = ['Q14']
    timeout_seconds = 60
class Q15(Page):
    form_model = 'player'
    form_fields = ['Q15']
    timeout_seconds = 60
class Waitforresult(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = set_payoffs
class Result(Page):
    form_model = 'player'
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            correctanswer=player.numberofcorrectanswers,
            wronganswer=player.numberofwronganswer,
            mypayoff=player.payofftoshow)
page_sequence = [Instruction, Waitforeveryone, Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Waitforresult, Result]
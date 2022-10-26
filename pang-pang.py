import random as rand

class Player():
   def __init__(self, lifes):
      self.lifes = lifes
      self.scores = 0
      self.did_hit = False
      self.is_hitted = False

   def fire(self):
       self.did_hit = True if rand.uniform(0, 1) > 0.4 else False
       self.is_hitted = True if rand.uniform(0, 1) > 0.7 else False

   def inc_scores(self):
       self.scores += 1

   def reduce_lifes(self):
       self.lifes -= 1

a_player = Player(3)       # Initiera en spelare med tre liv
while True:
    input('Tryck Enter för att skjuta')
    a_player.fire()
    if a_player.did_hit:
       print('Träff!')
       a_player.inc_scores() # Antalet poäng ökas med 1
    else:
       print('Miss, sikta bättre')
    if a_player.is_hitted:
       print('Aaaaaah')
       a_player.reduce_lifes() # Antalet liv minskas med 1
    else:
       print('Du klarade dig denna gång!')
       print(a_player.scores)
       print(a_player.lifes)
    if a_player.lifes <= 0:
       break


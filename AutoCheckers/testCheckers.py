'''
Created on Jul 22, 2011

@author: Davide Aversa
'''

from CheckersBrain import CheckersBrain

weights1 = {'PIECE':400,
          'KING':1200,
          'BACK':10,
          'KBACK':10,
          'CENTER':30,
          'KCENTER':30,
          'FRONT':60,
          'KFRONT':60,
          'MOB':0}

weights2 = {'PIECE':400,
          'KING':800,
          'BACK':40,
          'KBACK':40,
          'CENTER':40,
          'KCENTER':40,
          'FRONT':60,
          'KFRONT':60,
          'MOB':0}

# This is an usage example. It's easy!
C = CheckersBrain(weights1, 2, weights2,verbose=True)
#C.reset()
C.run_self()

print("The winner is %s!" % C.winner)

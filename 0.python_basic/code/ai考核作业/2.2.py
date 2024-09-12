#未完成

import random

l=['A','2','3','4','5','6','7','8','9','10','J','Q','K',
   'A','2','3','4','5','6','7','8','9','10','J','Q','K',
   'A','2','3','4','5','6','7','8','9','10','J','Q','K',
   'A','2','3','4','5','6','7','8','9','10','J','Q','K',
   '大王','小王']

random.shuffle(l)

p1=open("player1.txt",'w')
p2=open("player2.txt",'w')
p3=open("player3.txt",'w')
o=open("other.txt",'w')

p1.write(str(l[0:17]))
p2.write(str(l[17:34]))
p3.write(str(l[34:51]))
o.write(str(l[51:54]))

p1.close()
p2.close()
p3.close()
o.close()




每个project都是一等一的逆天，不多说，直接hog开始
## hog（24spring）

看完1.6
### 第一阶段

直接开题目，解锁q00

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
? 4
-- OK! --

>>> test_dice() # Second call
? 1
-- OK! --

>>> test_dice() # Third call
? 2
-- OK! --

>>> test_dice() # Fourth call
? 4
-- OK! --

---------------------------------------------------------------------
Question 0 > Suite 2 > Case 1
(cases remaining: 1)

Q: Which of the following is the correct way to "roll" a fair, six-sided die?
Choose the number of the correct choice:
0) six_sided
1) six_sided()
2) six_sided(6)
3) six_sided(1)
4) make_test_dice(6)
5) make_fair_dice(6)
? 5
-- Not quite. Try again! --

Choose the number of the correct choice:
0) six_sided
1) six_sided()
2) six_sided(6)
3) six_sided(1)
4) make_test_dice(6)
5) make_fair_dice(6)
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 0 unlocked.

Cannot backup when running ok with --local.
```

这里理解错了，应该是six_sided调用make_fair_dice函数生成6个色子，make_fair_dice应该是内部封装好的

继续q1

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 1
(cases remaining: 59)

>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
? 4
-- Not quite. Try again! --

? 6
-- Not quite. Try again! --

? 1
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 2
(cases remaining: 58)

>>> from hog import *
>>> roll_dice(3, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 3
(cases remaining: 57)

>>> from hog import *
>>> roll_dice(4, make_test_dice(2, 2, 3))
? 9
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 4
(cases remaining: 56)

>>> from hog import *
>>> a = roll_dice(4, make_test_dice(1, 2, 3))
>>> a # check that the value is being returned, not printed
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 5
(cases remaining: 55)

>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
? 1
-- OK! --

>>> # Make sure you call dice exactly num_rolls times!
>>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
>>> # Note that a return statement within a loop ends the loop
>>> roll_dice(1, counted_dice)
? 6
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 6
(cases remaining: 54)

>>> from hog import *
>>> roll_dice(9, make_test_dice(6))
? 30
-- Not quite. Try again! --

? 54
-- OK! --

>>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 1
(cases remaining: 53)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 2
(cases remaining: 52)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 3
(cases remaining: 51)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 1
(cases remaining: 50)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 2
(cases remaining: 49)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 3
(cases remaining: 48)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 4
(cases remaining: 47)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 5
(cases remaining: 46)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 6
(cases remaining: 45)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 7
(cases remaining: 44)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 8
(cases remaining: 43)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 9
(cases remaining: 42)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 10
(cases remaining: 41)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 11
(cases remaining: 40)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 12
(cases remaining: 39)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 13
(cases remaining: 38)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 14
(cases remaining: 37)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 15
(cases remaining: 36)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 16
(cases remaining: 35)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 17
(cases remaining: 34)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 18
(cases remaining: 33)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 19
(cases remaining: 32)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 20
(cases remaining: 31)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 21
(cases remaining: 30)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 22
(cases remaining: 29)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 23
(cases remaining: 28)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 24
(cases remaining: 27)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 25
(cases remaining: 26)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 26
(cases remaining: 25)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 27
(cases remaining: 24)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 28
(cases remaining: 23)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 29
(cases remaining: 22)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 30
(cases remaining: 21)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 31
(cases remaining: 20)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 32
(cases remaining: 19)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 33
(cases remaining: 18)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 34
(cases remaining: 17)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 35
(cases remaining: 16)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 36
(cases remaining: 15)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 37
(cases remaining: 14)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 38
(cases remaining: 13)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 39
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 40
(cases remaining: 11)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 41
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 42
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 43
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 44
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 45
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 46
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 47
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 48
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 49
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 3 > Case 50
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 1 unlocked.

Cannot backup when running ok with --local.
```

中间傻瓜了几次，一次是最下面那个，把9×6看成了5×6，还有就是刚开始的时候一下没理解意思，这里返回的应该是总和。

接下来开代码：

```
def roll_dice(num_rolls, dice=six_sided):  
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of  
    the outcomes unless any of the outcomes is 1. In that case, return 1.  
    num_rolls:  The number of dice rolls that will be made.    dice:       A function that simulates a single dice roll outcome.    """    # These assert statements ensure that num_rolls is a positive integer.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls > 0, 'Must roll at least once.'  
    # BEGIN PROBLEM 1  
    i,sum=1,0  
    tip=True  
    while i<=num_rolls:  
        a=dice()  
        if a==1:  
            tip=False  
        i,sum=i+1,sum+a  
    if tip:  
        return sum  
    else:  
        return 1  
    # END PROBLEM 1
```

需要注意的是，题目里有说，必须要保证循环次数为num_rolls，不能碰到1就返回1

还有就是不要反复调用dice，每调用一次dice，dice的值就会更新

开q02

这里遇到了点小问题，我用的fall2022的网页写的这个，所以规则不对，结果发现我现在做的版本spring2024官网得要伯努利账号，然后试了一下fall2022，spring2022，fall2020的备份，都不行，但是，简单搜索了一下，发现了2024spring的备份，爽了！

贴一个2024spring的备份：https://cs61a.org/proj/hog/

不过我好像发现这个没更新完（）所以后面肯定又会遇到问题，唉

继续：

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 1
(cases remaining: 14)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(21, 46)
? 6
-- Not quite. Try again! --

? 27
-- Not quite. Try again! --

? 9
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 2
(cases remaining: 13)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(52, 79)
? 15
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 3
(cases remaining: 12)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(0, 0)
? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 4
(cases remaining: 11)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(0, 5)
? 0
-- Not quite. Try again! --

? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 5
(cases remaining: 10)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(2, 5)
? 6
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 6
(cases remaining: 9)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(7, 2)
? 21
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 7
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 8
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 9
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 10
(cases remaining: 5)

>>> from hog import *
>>> import tests.construct_check as test
>>> boar_brawl(72, 29)
? 15
-- Not quite. Try again! --

? 1
-- OK! --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 11
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 12
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 13
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 2 > Suite 1 > Case 14
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 2 unlocked.
```

错的有点多，继续代码实现：

```
def boar_brawl(player_score, opponent_score):  
    """Return the points scored by rolling 0 dice according to Boar Brawl.  
  
    player_score:     The total score of the current player.    opponent_score:   The total score of the other player.  
    """    # BEGIN PROBLEM 2    a=player_score  
    b=opponent_score  
    return max(1,abs(a%10-b%100//10)*3)  
    # END PROBLEM 2
```

一样，也是要注意不要重复调用的问题

继续q3，要进行一轮的实现了

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 1
(cases remaining: 12)

>>> from hog import *
>>> take_turn(2, 7, 27, make_test_dice(4, 5, 1))
? 9
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 2
(cases remaining: 11)

>>> from hog import *
>>> take_turn(3, 15, 9, make_test_dice(4, 6, 1))
? 1
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 3
(cases remaining: 10)

>>> from hog import *
>>> take_turn(0, 12, 41) # what happens when you roll 0 dice?
? 6
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 4
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 5
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 6
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 7
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 8
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 9
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 10
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 11
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 3 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 3 unlocked.
```

解锁如上，代码如下：

```
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the points scored on a turn rolling NUM_ROLLS dice when the  
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.  
    num_rolls:       The number of dice rolls that will be made.    player_score:    The total score of the current player.    opponent_score:  The total score of the other player.    dice:            A function that simulates a single dice roll outcome.    """    # Leave these assert statements here; they help check for errors.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'  
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'  
    # BEGIN PROBLEM 3  
    if num_rolls==0:  
        return boar_brawl(player_score,opponent_score)  
    else:  
        return roll_dice(num_rolls,dice)  
    # END PROBLEM 3
```

两行代码解决，继续q4

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 1
(cases remaining: 27)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(1)
? 1
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 2
(cases remaining: 26)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 3
(cases remaining: 25)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(3)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 4
(cases remaining: 24)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(9)
? 3
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 5
(cases remaining: 23)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(28)
? 6
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 6
(cases remaining: 22)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(64)
? 11
-- Not quite. Try again! --

? 7
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 7
(cases remaining: 21)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 8
(cases remaining: 20)

>>> from hog import *
>>> import tests.construct_check as test
>>> num_factors(97)
? 2
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 9
(cases remaining: 19)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 10
(cases remaining: 18)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(1)
? 1
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 11
(cases remaining: 17)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(21)
? 23
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 12
(cases remaining: 16)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 13
(cases remaining: 15)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(62)
? 67
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 14
(cases remaining: 14)

>>> from hog import *
>>> import tests.construct_check as test
>>> sus_points(64)
? 64
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 15
(cases remaining: 13)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 16
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 17
(cases remaining: 11)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 18
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 19
(cases remaining: 9)

>>> from hog import *
>>> import tests.construct_check as test
>>> simple_update(2, 5, 7, make_test_dice(2, 4))
? 11
-- OK! --

>>> sus_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a sus number?
? 11
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 20
(cases remaining: 8)

>>> from hog import *
>>> import tests.construct_check as test
>>> simple_update(0, 15, 37) # what happens when you roll 0 dice?
? 4
-- Not quite. Try again! --

? 19
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 17
-- Not quite. Try again! --

? 21
-- OK! --

>>> sus_update(0, 15, 37) # is 21 a sus number?
? 23
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 21
(cases remaining: 7)

>>> from hog import *
>>> import tests.construct_check as test
>>> simple_update(2, 2, 3, make_test_dice(4))
? 20
-- Not quite. Try again! --

? 10
-- OK! --

>>> sus_update(2, 2, 3, make_test_dice(4)) # is 10 a sus number?
? 11
-- OK! --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 22
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 23
(cases remaining: 5)

-- Already unlocked --

Question 4 > Suite 1 > Case 24
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 25
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 26
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 4 > Suite 1 > Case 27
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 4 unlocked.
```

代码：

```
def num_factors(n):  
    """Return the number of factors of N, including 1 and N itself."""  
    # BEGIN PROBLEM 4    i,s=1,0  
    while i<=n:  
        if n%i==0:  
            s+=1  
        i+=1  
    return s  
    # END PROBLEM 4  
  
def sus_points(score):  
    """Return the new score of a player taking into account the Sus Fuss rule."""  
    # BEGIN PROBLEM 4    s=score  
    if num_factors(s)==3 or num_factors(s)==4:  
        while not is_prime(s):  
            s+=1  
    return s  
    # END PROBLEM 4  
  
def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the total score of a player who starts their turn with  
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.    """    # BEGIN PROBLEM 4    s=simple_update(num_rolls,player_score,opponent_score,dice)  
    return sus_points(s)  
    # END PROBLEM 4
```


q5

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 1
(cases remaining: 104)

Q: The variables score0 and score1 are the scores for Player 0
and Player 1, respectively. Under what conditions should the
game continue?
Choose the number of the correct choice:
0) While score0 is less than goal
1) While score0 and score1 are both less than goal
2) While at least one of score0 or score1 is less than goal
3) While score1 is less than goal
? 1
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 2
(cases remaining: 103)

Q: What is a strategy in the context of this game?
Choose the number of the correct choice:
0) The number of dice a player will roll
1) A function that returns the number of dice a player will roll
2) A player's desired turn outcome
? 1
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 3
(cases remaining: 102)

Q: If strategy1 is Player 1's strategy function, score0 is
Player 0's current score, and score1 is Player 1's current
score, then which of the following demonstrates correct
usage of strategy1?
Choose the number of the correct choice:
0) strategy1(score1, score0)
1) strategy1(score1)
2) strategy1(score0)
3) strategy1(score0, score1)
? 0
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 1 > Case 4
(cases remaining: 101)

Q: Player 0 has a score of 55, Player 1 has a score of 22,
and Player 0's strategy is given by lambda x, y: ((y % 10) * (x % 10)) % 10.
How many dice will Player 0 roll on their turn?
Choose the number of the correct choice:
0) 1
1) 0
2) 10
3) 5
? 1
-- OK! --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 1
(cases remaining: 100)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 2
(cases remaining: 99)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 3
(cases remaining: 98)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 4
(cases remaining: 97)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 5
(cases remaining: 96)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 6
(cases remaining: 95)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 7
(cases remaining: 94)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 8
(cases remaining: 93)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 9
(cases remaining: 92)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 10
(cases remaining: 91)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 11
(cases remaining: 90)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 12
(cases remaining: 89)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 13
(cases remaining: 88)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 14
(cases remaining: 87)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 15
(cases remaining: 86)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 16
(cases remaining: 85)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 17
(cases remaining: 84)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 18
(cases remaining: 83)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 19
(cases remaining: 82)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 20
(cases remaining: 81)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 21
(cases remaining: 80)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 22
(cases remaining: 79)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 23
(cases remaining: 78)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 24
(cases remaining: 77)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 25
(cases remaining: 76)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 26
(cases remaining: 75)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 27
(cases remaining: 74)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 28
(cases remaining: 73)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 29
(cases remaining: 72)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 30
(cases remaining: 71)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 31
(cases remaining: 70)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 32
(cases remaining: 69)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 33
(cases remaining: 68)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 34
(cases remaining: 67)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 35
(cases remaining: 66)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 36
(cases remaining: 65)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 37
(cases remaining: 64)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 38
(cases remaining: 63)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 39
(cases remaining: 62)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 40
(cases remaining: 61)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 41
(cases remaining: 60)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 42
(cases remaining: 59)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 43
(cases remaining: 58)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 44
(cases remaining: 57)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 45
(cases remaining: 56)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 46
(cases remaining: 55)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 47
(cases remaining: 54)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 48
(cases remaining: 53)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 49
(cases remaining: 52)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 50
(cases remaining: 51)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 51
(cases remaining: 50)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 52
(cases remaining: 49)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 53
(cases remaining: 48)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 54
(cases remaining: 47)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 55
(cases remaining: 46)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 56
(cases remaining: 45)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 57
(cases remaining: 44)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 58
(cases remaining: 43)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 59
(cases remaining: 42)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 60
(cases remaining: 41)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 61
(cases remaining: 40)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 62
(cases remaining: 39)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 63
(cases remaining: 38)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 64
(cases remaining: 37)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 65
(cases remaining: 36)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 66
(cases remaining: 35)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 67
(cases remaining: 34)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 68
(cases remaining: 33)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 69
(cases remaining: 32)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 70
(cases remaining: 31)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 71
(cases remaining: 30)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 72
(cases remaining: 29)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 73
(cases remaining: 28)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 74
(cases remaining: 27)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 75
(cases remaining: 26)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 76
(cases remaining: 25)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 77
(cases remaining: 24)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 78
(cases remaining: 23)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 79
(cases remaining: 22)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 80
(cases remaining: 21)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 81
(cases remaining: 20)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 82
(cases remaining: 19)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 83
(cases remaining: 18)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 84
(cases remaining: 17)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 85
(cases remaining: 16)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 86
(cases remaining: 15)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 87
(cases remaining: 14)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 88
(cases remaining: 13)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 89
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 90
(cases remaining: 11)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 91
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 92
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 93
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 94
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 95
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 96
(cases remaining: 5)

-- Already unlocked --

Question 5 > Suite 2 > Case 97
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 98
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 99
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 5 > Suite 2 > Case 100
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 5 unlocked.
```

代码：

```
def play(strategy0, strategy1, update,  
         score0=0, score1=0, dice=six_sided, goal=GOAL):  
    """Simulate a game and return the final scores of both players, with  
    Player 0's score first and Player 1's score second.  
    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in    which both players always choose to roll 5 dice on every turn and the Sus    Fuss rule is in effect.  
    A strategy function, such as always_roll_5, takes the current player's    score and their opponent's score and returns the number of dice the current    player chooses to roll.  
    An update function, such as sus_update or simple_update, takes the number    of dice to roll, the current player's score, the opponent's score, and the    dice function used to simulate rolling dice. It returns the updated score    of the current player after they take their turn.  
    strategy0: The strategy for player0.    strategy1: The strategy for player1.    update:    The update function (used for both players).    score0:    Starting score for Player 0    score1:    Starting score for Player 1    dice:      A function of zero arguments that simulates a dice roll.    goal:      The game ends and someone wins when this score is reached.    """    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)  
    # BEGIN PROBLEM 5    while True:  
        if who==0:  
            strategy=strategy0(score0,score1)  
            score0=update(strategy,score0,score1,dice)  
        else:  
            strategy=strategy1(score1,score0)  
            score1=update(strategy,score1,score0,dice)  
        if score0>=goal or score1>=goal:  
            break  
        who=1-who  
    # END PROBLEM 5  
    return score0, score1
```

芜湖！第一阶段hog结束！

总的第一阶段代码如下：

```
"""The Game of Hog."""  
  
from dice import six_sided, make_test_dice  
from ucb import main, trace, interact  
  
GOAL = 100  # The goal of Hog is to score 100 points.  
  
######################  
# Phase 1: Simulator #  
######################  
  
  
def roll_dice(num_rolls, dice=six_sided):  
    # These assert statements ensure that num_rolls is a positive integer.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls > 0, 'Must roll at least once.'  
    # BEGIN PROBLEM 1  
    i,sum=1,0  
    tip=True  
    while i<=num_rolls:  
        a=dice()  
        if a==1:  
            tip=False  
        i,sum=i+1,sum+a  
    if tip:  
        return sum  
    else:  
        return 1  
    # END PROBLEM 1  
  
  
def boar_brawl(player_score, opponent_score):  
    # BEGIN PROBLEM 2    
    a=player_score  
    b=opponent_score  
    return max(1,abs(a%10-b%100//10)*3)  
    # END PROBLEM 2  
  
  
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):  
    # Leave these assert statements here; they help check for errors.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'  
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'  
    # BEGIN PROBLEM 3  
    if num_rolls==0:  
        return boar_brawl(player_score,opponent_score)  
    else:  
        return roll_dice(num_rolls,dice)  
    # END PROBLEM 3  
  
  
def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the total score of a player who starts their turn with  
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.    """    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)  
    return score  
  
def is_prime(n):  
    """Return whether N is prime."""  
    if n == 1:  
        return False  
    k = 2  
    while k < n:  
        if n % k == 0:  
            return False  
        k += 1  
    return True  
  
def num_factors(n):  
    """Return the number of factors of N, including 1 and N itself."""  
    # BEGIN PROBLEM 4    i,s=1,0  
    while i<=n:  
        if n%i==0:  
            s+=1  
        i+=1  
    return s  
    # END PROBLEM 4  
  
def sus_points(score):  
    """Return the new score of a player taking into account the Sus Fuss rule."""  
    # BEGIN PROBLEM 4    s=score  
    if num_factors(s)==3 or num_factors(s)==4:  
        while not is_prime(s):  
            s+=1  
    return s  
    # END PROBLEM 4  
  
def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the total score of a player who starts their turn with  
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.    """    # BEGIN PROBLEM 4    s=simple_update(num_rolls,player_score,opponent_score,dice)  
    return sus_points(s)  
    # END PROBLEM 4  
  
  
def always_roll_5(score, opponent_score):  
	return 5  
  
  
def play(strategy0, strategy1, update,  
         score0=0, score1=0, dice=six_sided, goal=GOAL):  
	who = 0  # Who is about to take a turn, 0 (first) or 1 (second)  
    # BEGIN PROBLEM 5    
    while True:  
        if who==0:  
            strategy=strategy0(score0,score1)  
            score0=update(strategy,score0,score1,dice)  
        else:  
            strategy=strategy1(score1,score0)  
            score1=update(strategy,score1,score0,dice)  
        if score0>=goal or score1>=goal:  
            break  
        who=1-who  
    # END PROBLEM 5  
    return score0, score1
```

今天先到这里！

爽了爽了，上号一会儿

回来写一下感想，其实不难，需要注意的就是每道题目一环扣一环，联系地很紧密所以推荐找个时间一起写掉。
### 第二阶段：

unlock6

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> always_roll(3)(10, 20)
? 3
-- OK! --

---------------------------------------------------------------------
Question 6 > Suite 1 > Case 2
(cases remaining: 1)

>>> from hog import *
>>> always_roll(0)(99, 99)
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 6 unlocked.
```

代码：

```
def always_roll(n):  
    assert n >= 0 and n <= 10  
    # BEGIN PROBLEM 6  
    def strategy(x,y):  
        return n  
    return strategy  
    # END PROBLEM 6
```

继续第七问：

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 7 > Suite 1 > Case 1
(cases remaining: 9)

>>> from hog import *
>>> is_always_roll(always_roll_5)
? True
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 1 > Case 2
(cases remaining: 8)

>>> from hog import *
>>> is_always_roll(always_roll(3))
? True
-- OK! --

---------------------------------------------------------------------
Question 7 > Suite 1 > Case 3
(cases remaining: 7)

>>> from hog import *
>>> is_always_roll(catch_up)
? False
-- OK! --
```

代码：

```
def is_always_roll(strategy, goal=GOAL):  
    # BEGIN PROBLEM 7    
    i=0  
    while i<=goal:  
        j=0  
        while j <goal:  
            if strategy(i,j)!=strategy(i,j+1):  
                return False  
            j+=1  
        i+=1  
    return True  
    # END PROBLEM 7
```

遍历二维数组

继续


q8

这里是先介绍了一个新的语法，就是*，`*arg`可以代指不止一个东西，使用`*arg`语法来写第八问

首先来看看第八问到底是干啥的？

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 1
(cases remaining: 7)

Q: What is one reason that make_averaged is a higher order function?
Choose the number of the correct choice:
0) It calls a function that is not itself
1) It uses the *args keyword
2) It contains a nested function
3) It takes in a function as an argument
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) It calls a function that is not itself
1) It uses the *args keyword
2) It contains a nested function
3) It takes in a function as an argument
? 3
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 1 > Case 2
(cases remaining: 6)

Choose the number of the correct choice:
0) None
1) An arbitrary amount, which is why we need to use *args to call it
2) Two
? 1
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 1
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_dice = make_averaged(dice, 1000)
>>> # Average of calling dice 1000 times
>>> averaged_dice()
? 3.75
-- OK! --

---------------------------------------------------------------------
Question 8 > Suite 2 > Case 2
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
? 6.0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 8 unlocked.

Cannot backup when running ok with --local.
```

最后一题的时候需要注意，别忘记前面的规则，只要色子有1，那么和就是1，别忘记了。

```
def make_averaged(original_function, samples_count=1000):  
    # BEGIN PROBLEM 8    
    def f(*args):  
        i, sum = 1, 0  
        while i<=samples_count:  
            sum+=original_function(*args)  
            i+=1  
        return sum/samples_count  
    return f  
    # END PROBLEM 8
```

有点艰难，但是还是看出来题目是啥意思了

q9

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 9 > Suite 1 > Case 1
(cases remaining: 10)

Q: If multiple num_rolls are tied for the highest scoring
average, which should you return?
Choose the number of the correct choice:
0) A random num_rolls
1) The highest num_rolls
2) The lowest num_rolls
? 2
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 1
(cases remaining: 9)

>>> from hog import *
>>> dice = make_test_dice(3)   # dice always returns 3
>>> max_scoring_num_rolls(dice, samples_count=1000)
? 1
-- Not quite. Try again! --

? 0
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 1.0
-- Not quite. Try again! --

?
-- Not quite. Try again! --

? 3
-- Not quite. Try again! --

? 4
-- Not quite. Try again! --

? 5
-- Not quite. Try again! --

? 6
-- Not quite. Try again! --

? 7
-- Not quite. Try again! --

? 8
-- Not quite. Try again! --

? 9
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 2
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 3
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 1
(cases remaining: 6)

>>> from hog import *
>>> dice = make_test_dice(2)     # dice always rolls 2
>>> max_scoring_num_rolls(dice, samples_count=1000)
? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 2
(cases remaining: 5)

>>> from hog import *
>>> dice = make_test_dice(1)     # dice always rolls 1
>>> max_scoring_num_rolls(dice, samples_count=1000)
? 1
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 3
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
>>> max_scoring_num_rolls(dice, samples_count=1000)
? 1
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 4
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 5
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 6
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 9 unlocked.

Cannot backup when running ok with --local.
```

中间有个东西没反应过来，色子是累计和的，其实是对上一个函数的不了解

```
def max_scoring_num_rolls(dice=six_sided, samples_count=1000):  
	# BEGIN PROBLEM 9    
	_average_dice=make_averaged(roll_dice,samples_count)  
    i=2  
    max_i= 1  
    max_value=_average_dice(1,dice)  
    while i<=10:  
        temp=_average_dice(i,dice)  
        if max_value<temp:  
            max_value=temp  
            max_i=i  
        i+=1  
    return max_i
```

q10

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 1
(cases remaining: 10)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=7, num_rolls=2)
? num_rolls
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 2
(cases remaining: 9)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=15, num_rolls=7)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 3
(cases remaining: 8)

>>> from hog import *
>>> boar_strategy(40, 51, threshold=16, num_rolls=7)
? num_rolls
-- Not quite. Try again! --

? 7
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 4
(cases remaining: 7)

>>> from hog import *
>>> boar_strategy(44, 53, threshold=3, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 5
(cases remaining: 6)

>>> from hog import *
>>> boar_strategy(44, 53, threshold=4, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 6
(cases remaining: 5)

>>> from hog import *
>>> boar_strategy(40, 31, threshold=9, num_rolls=5)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 7
(cases remaining: 4)

>>> from hog import *
>>> boar_strategy(40, 31, threshold=10, num_rolls=5)
? 5
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 8
(cases remaining: 3)

>>> from hog import *
>>> boar_strategy(40, 52, threshold=15, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 9
(cases remaining: 2)

>>> from hog import *
>>> boar_strategy(40, 52, threshold=16, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 10 > Suite 1 > Case 10
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 10 unlocked.

Cannot backup when running ok with --local.
```

代码：

```
def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):  
    # BEGIN PROBLEM 10    
    if boar_brawl(score,opponent_score)>=threshold:  
        return 0  
    return num_rolls  
    # END PROBLEM 10
```

q11

```
=====================================================================
Assignment: Project 1: Hog
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 1
(cases remaining: 8)

>>> from hog import *
>>> sus_strategy(31, 21, threshold=10, num_rolls=2)
? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 2
(cases remaining: 7)

>>> from hog import *
>>> sus_strategy(30, 41, threshold=10, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 3
(cases remaining: 6)

>>> from hog import *
>>> sus_strategy(53, 60, threshold=14, num_rolls=2)
? 2
-- Not quite. Try again! --

? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 4
(cases remaining: 5)

>>> from hog import *
>>> sus_strategy(53, 60, threshold=15, num_rolls=2)
? 0
-- Not quite. Try again! --

? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 5
(cases remaining: 4)

>>> from hog import *
>>> sus_strategy(23, 54, threshold=4, num_rolls=2)
? 0
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 6
(cases remaining: 3)

>>> from hog import *
>>> sus_strategy(14, 21, threshold=8, num_rolls=2)
? 0
-- Not quite. Try again! --

? 2
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 7
(cases remaining: 2)

>>> from hog import *
>>> sus_strategy(14, 21, threshold=12, num_rolls=5)
? 5
-- OK! --

---------------------------------------------------------------------
Question 11 > Suite 1 > Case 8
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 11 unlocked.

Cannot backup when running ok with --local.
```

代码：

```
def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):    
    # BEGIN PROBLEM 11    
    if sus_points(score+boar_brawl(score,opponent_score))-score>=threshold:  
        return 0  
    return num_rolls  
    # END PROBLEM 11
```

就这上面几行代码花了我感觉块40分钟的时间，网页提示跟我说的使用sus_update，我竟然没有及时反应过来。

sus_update是基于simple_update实现的，这里我们不知道dice是啥，根本没办法得出有效结果。

这也解释了为什么我在运行过程中的结果不确定，有时候通过有时候不通过，原因就在默认的dice就是普通的色子

这很难受啊，思路是对的，但是网页提示给错了，有可能是我没get到网页提示的意思就是了

q12

可选的作业

就不写了。

所有代码如下：

```
"""The Game of Hog."""  
from random import shuffle  
  
from dice import six_sided, make_test_dice  
from ucb import main, trace, interact  
  
GOAL = 100  # The goal of Hog is to score 100 points.  
  
######################  
# Phase 1: Simulator #  
######################  
  
  
def roll_dice(num_rolls, dice=six_sided):  
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of  
    the outcomes unless any of the outcomes is 1. In that case, return 1.  
    num_rolls:  The number of dice rolls that will be made.    dice:       A function that simulates a single dice roll outcome.    """    # These assert statements ensure that num_rolls is a positive integer.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls > 0, 'Must roll at least once.'  
    # BEGIN PROBLEM 1  
    i,sum=1,0  
    tip=True  
    while i<=num_rolls:  
        a=dice()  
        if a==1:  
            tip=False  
        i,sum=i+1,sum+a  
    if tip:  
        return sum  
    else:  
        return 1  
    # END PROBLEM 1  
  
  
def boar_brawl(player_score, opponent_score):  
    """Return the points scored by rolling 0 dice according to Boar Brawl.  
  
    player_score:     The total score of the current player.    opponent_score:   The total score of the other player.  
    """    # BEGIN PROBLEM 2    a=player_score  
    b=opponent_score  
    return max(1,abs(a%10-b%100//10)*3)  
    # END PROBLEM 2  
  
  
def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the points scored on a turn rolling NUM_ROLLS dice when the  
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.  
    num_rolls:       The number of dice rolls that will be made.    player_score:    The total score of the current player.    opponent_score:  The total score of the other player.    dice:            A function that simulates a single dice roll outcome.    """    # Leave these assert statements here; they help check for errors.    assert type(num_rolls) == int, 'num_rolls must be an integer.'  
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'  
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'  
    # BEGIN PROBLEM 3  
    if num_rolls==0:  
        return boar_brawl(player_score,opponent_score)  
    else:  
        return roll_dice(num_rolls,dice)  
    # END PROBLEM 3  
  
  
def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the total score of a player who starts their turn with  
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.    """    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)  
    return score  
  
def is_prime(n):  
    """Return whether N is prime."""  
    if n == 1:  
        return False  
    k = 2  
    while k < n:  
        if n % k == 0:  
            return False  
        k += 1  
    return True  
  
def num_factors(n):  
    """Return the number of factors of N, including 1 and N itself."""  
    # BEGIN PROBLEM 4    i,s=1,0  
    while i<=n:  
        if n%i==0:  
            s+=1  
        i+=1  
    return s  
    # END PROBLEM 4  
  
def sus_points(score):  
    """Return the new score of a player taking into account the Sus Fuss rule."""  
    # BEGIN PROBLEM 4    s=score  
    if num_factors(s)==3 or num_factors(s)==4:  
        while not is_prime(s):  
            s+=1  
    return s  
    # END PROBLEM 4  
  
def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):  
    """Return the total score of a player who starts their turn with  
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.    """    # BEGIN PROBLEM 4    s=simple_update(num_rolls,player_score,opponent_score,dice)  
    return sus_points(s)  
    # END PROBLEM 4  
  
  
def always_roll_5(score, opponent_score):  
    """A strategy of always rolling 5 dice, regardless of the player's score or  
    the opponent's score.    """    return 5  
  
  
def play(strategy0, strategy1, update,  
         score0=0, score1=0, dice=six_sided, goal=GOAL):  
    """Simulate a game and return the final scores of both players, with  
    Player 0's score first and Player 1's score second.  
    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in    which both players always choose to roll 5 dice on every turn and the Sus    Fuss rule is in effect.  
    A strategy function, such as always_roll_5, takes the current player's    score and their opponent's score and returns the number of dice the current    player chooses to roll.  
    An update function, such as sus_update or simple_update, takes the number    of dice to roll, the current player's score, the opponent's score, and the    dice function used to simulate rolling dice. It returns the updated score    of the current player after they take their turn.  
    strategy0: The strategy for player0.    strategy1: The strategy for player1.    update:    The update function (used for both players).    score0:    Starting score for Player 0    score1:    Starting score for Player 1    dice:      A function of zero arguments that simulates a dice roll.    goal:      The game ends and someone wins when this score is reached.    """    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)  
    # BEGIN PROBLEM 5    while True:  
        if who==0:  
            strategy=strategy0(score0,score1)  
            score0=update(strategy,score0,score1,dice)  
        else:  
            strategy=strategy1(score1,score0)  
            score1=update(strategy,score1,score0,dice)  
        if score0>=goal or score1>=goal:  
            break  
        who=1-who  
    # END PROBLEM 5  
    return score0, score1  
  
  
#######################  
# Phase 2: Strategies #  
#######################  
  
  
def always_roll(n):  
    """Return a player strategy that always rolls N dice.  
  
    A player strategy is a function that takes two total scores as arguments    (the current player's score, and the opponent's score), and returns a    number of dice that the current player will roll this turn.  
    >>> strategy = always_roll(3)    >>> strategy(0, 0)    3    >>> strategy(99, 99)    3    """    assert n >= 0 and n <= 10  
    # BEGIN PROBLEM 6  
    def strategy(x,y):  
        return n  
    return strategy  
    # END PROBLEM 6  
  
  
def catch_up(score, opponent_score):  
    """A player strategy that always rolls 5 dice unless the opponent  
    has a higher score, in which case 6 dice are rolled.  
    >>> catch_up(9, 4)    5    >>> strategy(17, 18)    6    """    if score < opponent_score:  
        return 6  # Roll one more to catch up  
    else:  
        return 5  
  
  
def is_always_roll(strategy, goal=GOAL):  
    """Return whether STRATEGY always chooses the same number of dice to roll  
    given a game that goes to GOAL points.  
    >>> is_always_roll(always_roll_5)    True    >>> is_always_roll(always_roll(3))    True    >>> is_always_roll(catch_up)    False    """    # BEGIN PROBLEM 7    i=0  
    while i<=goal:  
        j=0  
        while j <goal:  
            if strategy(i,j)!=strategy(i,j+1):  
                return False  
            j+=1  
        i+=1  
    return True  
    # END PROBLEM 7  
  
  
def make_averaged(original_function, samples_count=1000):  
    """Return a function that returns the average value of ORIGINAL_FUNCTION  
    called SAMPLES_COUNT times.  
    To implement this function, you will have to use *args syntax.  
    >>> dice = make_test_dice(4, 2, 5, 1)    >>> averaged_dice = make_averaged(roll_dice, 40)    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's    3.0    """    # BEGIN PROBLEM 8    def f(*args):  
        i, sum = 1, 0  
        while i<=samples_count:  
            sum+=original_function(*args)  
            i+=1  
        return sum/samples_count  
    return f  
    # END PROBLEM 8  
  
  
def max_scoring_num_rolls(dice=six_sided, samples_count=1000):  
    """Return the number of dice (1 to 10) that gives the highest average turn score  
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.    Assume that the dice always return positive outcomes.  
    >>> dice = make_test_dice(1, 6)    >>> max_scoring_num_rolls(dice)    1    """    # BEGIN PROBLEM 9    _average_dice=make_averaged(roll_dice,samples_count)  
    i=2  
    max_i= 1  
    max_value=_average_dice(1,dice)  
    while i<=10:  
        temp=_average_dice(i,dice)  
        if max_value<temp:  
            max_value=temp  
            max_i=i  
        i+=1  
    return max_i  
  
  
    # END PROBLEM 9  
  
  
def winner(strategy0, strategy1):  
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""  
    score0, score1 = play(strategy0, strategy1, sus_update)  
    if score0 > score1:  
        return 0  
    else:  
        return 1  
  
  
def average_win_rate(strategy, baseline=always_roll(6)):  
    """Return the average win rate of STRATEGY against BASELINE. Averages the  
    winrate when starting the game as player 0 and as player 1.    """    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)  
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)  
  
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2  
  
  
def run_experiments():  
    """Run a series of strategy experiments and report results."""  
    six_sided_max = max_scoring_num_rolls(six_sided)  
    print('Max scoring num rolls for six-sided dice:', six_sided_max)  
  
    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5  
    print('catch_up win rate:', average_win_rate(catch_up))  
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))  
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))  
  
    print('boar_strategy win rate:', average_win_rate(boar_strategy))  
    print('sus_strategy win rate:', average_win_rate(sus_strategy))  
    print('final_strategy win rate:', average_win_rate(final_strategy))  
    "*** You may add additional experiments as you wish ***"  
  
  
  
  
def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):  
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD  
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.    """    # BEGIN PROBLEM 10    if boar_brawl(score,opponent_score)>=threshold:  
        return 0  
    return num_rolls  
    # END PROBLEM 10  
  
  
def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):  
    """This strategy returns 0 dice when your score would increase by at least threshold."""  
    # BEGIN PROBLEM 11    if sus_points(score+boar_brawl(score,opponent_score))-score>=threshold:  
        return 0  
    return num_rolls  
    # END PROBLEM 11  
  
  
def final_strategy(score, opponent_score):  
    """Write a brief description of your final strategy.  
  
    *** YOUR DESCRIPTION HERE ***    """    # BEGIN PROBLEM 12    return 6  # Remove this line once implemented.  
    # END PROBLEM 12  
  
##########################  
# Command Line Interface #  
##########################  
  
# NOTE: The function in this section does not need to be changed. It uses  
# features of Python not yet covered in the course.  
  
@main  
def run(*args):  
    """Read in the command-line argument and calls corresponding functions."""  
    import argparse  
    parser = argparse.ArgumentParser(description="Play Hog")  
    parser.add_argument('--run_experiments', '-r', action='store_true',  
                        help='Runs strategy experiments')  
  
    args = parser.parse_args()  
  
    if args.run_experiments:  
        run_experiments()
```

hog正式结束？

说实话写的很不爽，感觉有力气无处使的感觉



## cats(23spring)

#### q1

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import pick
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> pick(ps, s, 0) # remember to put quotes ('') around strings!
? 'short'
-- OK! --

>>> pick(ps, s, 1)
? 'tiny'
-- OK! --

>>> pick(ps, s, 2)
? ''
-- OK! --

---------------------------------------------------------------------
```

实现：

```
def pick(paragraphs, select, k):  
    # BEGIN PROBLEM 1    
    i,j=0,0  
    for i in range(len(paragraphs)):  
        if select(paragraphs[i]):  
            if j==k:  
                return paragraphs[i]  
            j+=1  
    return ''  
    # END PROBLEM 1
```

#### q2

先看看utils.py里面的函数到底有哪些，分别是什么作用：

```
def remove_punctuation(s):  
    punctuation_remover = str.maketrans('', '', string.punctuation)  
    return s.strip().translate(punctuation_remover)
```

字面意思，去除一个句子里的标点符号，之类的东西

```
def lower(s):  
    return s.lower()
```

将一个字符串的所有字母变成小写

```
def split(s):  
    return s.split()
```

将一个字符串按照空格分割成列表

题目要求：

实现 `about` 函数，该函数接收一个主题词列表 `subject`，返回一个函数，该函数接受一个段落，并返回一个布尔值，表示该段落是否包含 `subject` 中的任何词。

一旦我们实现了 `about`，我们将能够将返回的函数作为 `select` 参数传递给 `pick`，这在我们继续实现打字测试时会很有用。

为了能够准确地进行比较，你需要忽略大小写（也就是说，不区分大写和小写字母）和段落中的标点符号。此外，只检查 `subject` 中单词在段落中的精确匹配，而不是子字符串。例如，“dogs” 不应被视为单词 “dog” 的匹配。

q

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import about
>>> from cats import pick
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
? False
-- OK! --

>>> dogs('A paragraph about dogs.')
? True
-- OK! --

>>> dogs('Release the Hounds!')
? True
-- OK! --

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
? True
-- OK! --

>>> dogs('Do gs and ho unds don\'t count')
? False
-- OK! --

>>> dogs("AdogsParagraph")
? False
-- OK! --
```

代码：

```
def about(subject):  
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'  
    # BEGIN PROBLEM 2  
    def help(l):  
        l=split(remove_punctuation(lower(l)))  
        for word in subject:  
            for ch in l:  
                if ch==word:  
                    return True  
        return False    
    return help  
  
    # END PROBLEM 2
```

一个二维遍历

#### q3

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import accuracy
>>> accuracy("12345", "12345") # This should return 100.0 (not the integer 100!)
? 100.0
-- OK! --

>>> accuracy("a b c", "a b c")
? 100.0
-- OK! --

>>> accuracy("a  b  c  d", "b  a  c  d")
? 50.0
-- OK! --

>>> accuracy("a b", "c d e")
? 0.0
-- OK! --

>>> accuracy("Cat", "cat") # the function is case-sensitive
? 0.0
-- OK! --

>>> accuracy("a b c d", "a d")
? 50.0
-- Not quite. Try again! --

? 25.0
-- OK! --

>>> accuracy("abc", " ")
? 0.0
-- OK! --

>>> accuracy("a b \tc" , "a b c") # Tabs don't count as words
? 100.0
-- OK! --

>>> accuracy("abc", "")
? 0.0
-- OK! --

>>> accuracy("", "abc")
? 0.0
-- OK! --

>>> accuracy("a b c d", "b c d")
? 0.0
-- OK! --

>>> accuracy("cats.", "cats") # punctuation counts
? 50.0
-- Not quite. Try again! --

? 0.0
-- OK! --

>>> accuracy("", "") # Returns 100.0
? 100.0
-- OK! --
```

代码：

```
def accuracy(typed, source):  
    typed_words = split(typed)  
    source_words = split(source)  
    # BEGIN PROBLEM 3  
    len_typed=len(typed_words)  
    len_source=len(source_words)  
  
    if len_typed==0 and len_source==0:  
        return 100.0  
    if len_typed==0 or len_source==0:  
        return 0.0  
  
    len_min=min(len_typed,len_source)  
    typed_i=0  
  
    for i in range(0,len_min):  
        if typed_words[i]==source_words[i]:  
            typed_i+=1  
  
    return typed_i / len_typed * 100  
    # END PROBLEM 3
```

#### q4

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import wpm
>>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
? 20.0
-- OK! --

>>> wpm("a b c", 20)
? 3.0
-- OK! --

>>> wpm("", 10)
? 0.0
-- OK! --
```

代码：

```
def wpm(typed, elapsed):  
    assert elapsed > 0, 'Elapsed time must be positive'  
    # BEGIN PROBLEM 4  
    return 12*len(typed)/elapsed  
    # END PROBLEM 4
```

一行解决

#### q5

```                                                                              =====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
? cult
-- Not quite. Try again! --

? 'cult'
-- OK! --

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
? 'cul'
-- OK! --

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
? 'car'
-- OK! --

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
? 'word'
-- OK! --

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
? 'idea'
-- Not quite. Try again! --

? 'inside'
-- OK! --

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? 'idea'
-- OK! --

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
? 'outside'
-- OK! --

>>> length_ratio = lambda w1, w2, limit: len(w2) / len(w1) # An asymmetric diff function
>>> autocorrect("aaa", ["a"], length_ratio, 2) # typed_word ("aaa") is passed in as the first argument to a diff function
? 'a'
-- OK! --

>>> autocorrect("cats", ["panthers", "lions"], length_ratio, 2)
? 'lions'
-- OK! --
```

代码：

```
def autocorrect(typed_word, word_list, diff_function, limit):  
    # BEGIN PROBLEM 5    if typed_word in word_list:  
        return typed_word  
    diff_list=[diff_function(typed_word,word,limit) for word in word_list]  
    min_diff=min(diff_list)  
    if min_diff<=limit:  
        return word_list[diff_list.index(min_diff)]  
    else:  
        return typed_word  
    # END PROBLEM 5
```

这里使用了列表推导式，感觉不错

#### q6

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 106)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 2
(cases remaining: 105)

>>> from cats import feline_fixes, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
? 1
-- OK! --

>>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
? 2
-- OK! --

>>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
? 3
-- OK! --

>>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
? 5
-- OK! --

>>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
? 5
-- OK! --
```

只能用递归写，看一眼，感觉像是得用之前那个字底向上的递归。

```
def feline_fixes(typed, source, limit):  
    # BEGIN PROBLEM 6    
    
    if limit<0:  
        return limit+1  
  
    elif len(typed)==0 or len(source)==0:  
        return abs(len(typed)-len(source))  
  
    elif typed[0]!=source[0]:  
        return 1+feline_fixes(typed[1:],source[1:],limit-1)  
  
    else:  
        return feline_fixes(typed[1:],source[1:],limit)  
  
    # END PROBLEM 6
```

其实不用，但是这里我落入了一个坑，可能是没仔细看题目。如果超过limit之后直接返回。

#### q7

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 1
(cases remaining: 106)

>>> from cats import minimum_mewtations, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> minimum_mewtations("wind", "wind", big_limit)
? 0
-- OK! --

>>> minimum_mewtations("wird", "wiry", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("wird", "bird", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("wird", "wir", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("wird", "bwird", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("speling", "spelling", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("used", "use", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("hash", "ash", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("ash", "hash", big_limit)
? 1
-- OK! --

>>> minimum_mewtations("roses", "arose", big_limit)     # roses -> aroses -> arose
? 2
-- OK! --

>>> minimum_mewtations("tesng", "testing", big_limit)   # tesng -> testng -> testing
? 3
-- Not quite. Try again! --

? 2
-- OK! --

>>> minimum_mewtations("rlogcul", "logical", big_limit) # rlogcul -> logcul -> logicul -> logical
? 3
-- OK! --

>>> minimum_mewtations("", "", big_limit) # nothing to nothing needs no edits
? 0
-- OK! --
```

代码：

```
def minimum_mewtations(typed, source, limit):  
    if limit<0:  
        return limit+1  
  
    if typed==source:  
        return 0  
  
    if len(typed)==0 or len(source)==0:  
        # 加法操作  
        if len(typed)<len(source):  
            return minimum_mewtations(source[0]+typed,source,limit-1)+1  
  
        # 减法操作  
        if len(typed)>len(source):  
            return minimum_mewtations(typed[1:],source,limit-1)+1  
  
    if typed[0]==source[0]:  
        return minimum_mewtations(typed[1:],source[1:],limit)  
  
    # 加法操作  
    add=minimum_mewtations(source[0]+typed,source,limit-1)+1  
  
    # 减法操作  
    remove=minimum_mewtations(typed[1:],source,limit-1)+1  
  
    #替换操作  
    substitute=minimum_mewtations(source[0]+typed[1:],source,limit-1)+1  
  
    return min(add,remove,substitute)
```


感觉有点难度的，后面那个min有想出来，但是一下子没想出来怎么min，后来突然发现模板。

然后上面的代码在前面的部分有冗余，可以再修改一下。

#### q8

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> typed = ['I', 'have', 'begun']
>>> prompt = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
? 'ID: 1 Progress: 0.6'
-- Not quite. Try again! --

? ID: 1 Progress: 0.6
-- OK! --

>>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
(line 1)? ID: 1 Progress: 0.6
(line 2)? 0.6
-- OK! --

>>> report_progress(['I', 'begun'], prompt, 2, print_progress)
(line 1)? ID: 1 Progress: 0.2
-- Not quite. Try again! --

(line 1)? ID: 2 Progress: 0.2
(line 2)? 0.2
-- OK! --

>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
(line 1)? ID: 3 Progress: 0.2
(line 2)? 0.2
-- OK! --
```

代码：

```
def report_progress(typed, prompt, user_id, upload):  
    # BEGIN PROBLEM 8    same=0  
    for t,p in zip(typed,prompt):  
        if t==p:  
            same+=1  
        else:  
            break  
    dic={  
        'id': user_id,  
        'progress': same/len(prompt)  
    }  
    upload(dic)  
    return dic['progress']  
    # END PROBLEM 8
```

#### q9

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import *
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> match = time_per_word(words, p)
>>> get_all_words(match)
? ['This', 'is', 'fun']
-- OK! --

>>> get_all_times(match)
? [[3,2,1],[4,2,3]]
-- OK! --

>>> p = [[0, 2, 3], [2, 4, 7]]
>>> match = time_per_word(['hello', 'world'], p)
>>> get_word(match, word_index=1)
? 'hello'
-- Not quite. Try again! --

? 'world'
-- OK! --

>>> get_all_times(match)
? [[2,1],[2,3]]
-- OK! --

>>> time(match, player_num=0, word_index=1)
? [2,1]
-- Not quite. Try again! --

? 1
-- OK! --
```

code:

```
def time_per_word(words, times_per_player):  
    # BEGIN PROBLEM 9    
    times = []  
    for player_times in times_per_player:  
        player_durations = []  
        for i in range(len(player_times) - 1):  
            player_durations.append(player_times[i+1] - player_times[i])  
        times.append(player_durations)  
  
    return match(words, times)  
    # END PROBLEM 9
```

既然都用python了，我感觉上面的代码有点蠢。所以......

```
def time_per_word(words, times_per_player):  
    # BEGIN PROBLEM 9    
    
    times = [  
        [player_times[i + 1] - player_times[i] for i in range(len(player_times) - 1)]  
        for player_times in times_per_player  
    ]  
  
    return match(words, times)  
    # END PROBLEM 9
```

#### q10

```
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import match, fastest_words
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))
? p0
-- Not quite. Try again! --

? p1
-- Not quite. Try again! --

? [['What','luck'],[great]]
-- Not quite. Try again! --

? [['What',],['great','luck']]
-- OK! --

>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
? [['What','luck'],['great']]
-- OK! --

>>> p2 = [4, 3, 1]
>>> fastest_words(match(['What', 'great', 'luck'], [p0, p1, p2]))
? [['What'],['great'],['luck']]
-- OK! --
```

code:

是不难实现的，但是很麻烦，现在不是很想写，先去搞其他事情去了（）就差这步了

```

```
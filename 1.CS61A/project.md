
每个project都是一等一的逆天，不多说，直接hog开始
## hog

采用的是2024spring的版本

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



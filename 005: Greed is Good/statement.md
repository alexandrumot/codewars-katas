# 005: Greed is Good 

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 `Three 1's => 1000 points`<br>
 `Three 6's =>  600 points`<br>
 `Three 5's =>  500 points`<br>
 `Three 4's =>  400 points`<br>
 `Three 3's =>  300 points`<br>
 `Three 2's =>  200 points`<br>
 `One   1   =>  100 points`<br>
 `One   5   =>   50 point`<br>

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.


## Examples:

 `Throw....Score`<br>
 `---------   ------------------`<br>
 `5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)`<br>
 `1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)`<br>
 `2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)`<br>

<br>Link: https://www.codewars.com/kata/5270d0d18625160ada0000e4
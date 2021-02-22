# Readme.11

### Usage

Accepts `?` or `!` or `/` or  ````` as input 

Can call bot with either `roll` or `r`

* Roll 1 die of any type  `/r d20`
* Roll 1 die of any type with a modifier `/r d20+3`
* Roll multiple dice `/r 3d20`
* Roll multiple dice with a modifier `/r 3d6+3`
* Roll with advantage `/r 2d20k1`
* Roll with disadvantage `/r 2d20l1`
* Roll with advantage/disadvantage with mods `/r 2d20k1+4`

### Tests and Output

* Roll 1 die of any type
  * Tests
    * !roll d3
    * !roll d20
    * !roll d100
  * Example output
    * @user D3: 2
    * @user D20: 17
* Roll 1 die of any type with a + or - modifier
  * Tests
    * !roll d3+2
    * !roll d20+1
    * !roll d100+88
    * !roll d3-2
    * !roll d20-1
    * !roll d100-88
  * Example output
    * @user D100+88:  15+88 = 103
    * @user  D20-1: 7-1 = 6   
* Roll multiple dice of any type
  * Tests
    * !roll 2d20
    * !roll 3d100
    * !roll 100d100
  * Example output
    * @user \[5 + 13\] = 18
    * @user \[15 + 39 + 56\] = 110
* Roll Multiple dice of any type with a + or - modifier 
  * Tests
    * !roll 10d6+3
    * !roll 3d10+2
    * !roll 4d3-2
    * !roll 1d20-4
  * Example output
    * @user \[2 + 5 + 1 + 4 + 5 + 3 + 1 + 1 + 1 + 4\] + 3 = 30
    * @user \[3 + 2 + 1 + 3\] - 2 = 7
* Roll with advantage or disadvantage
  * Tests
    * !roll 2d20k1
    * !roll 2d20l1
  * Example output
    * @user Rolled: \[12, 14\]  Kept: \[14\]
    * @user Rolled: \[14, 2\]  Kept: \[2\]
* Roll with advantage or disadvantage with a + or - modifier
  * Tests
    * !roll 2d20k1+3
    * !roll 2d20l1+3
  * Example output
    * @user Rolled: \[4, 5\]  Kept: \[5\]    With modifier:   \[8\]
    * @user Rolled: \[20, 20\]  Kept: \[20\]    With modifier:   \[23\]


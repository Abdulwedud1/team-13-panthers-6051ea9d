*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
http://arcobotics.com/wp-content/uploads/2015/12/sparki-driver-icon.png
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX      StartingY      Direction     EndingX    EndingY 
Move in the middle of the board     0              0          NORTH              0                    1
Move in the edge of the board       0              0          SOUTH              0                    0
Move towards the edge of the board  8              0          EAST               9                    0
Move towrads the edge from top      8              9          EAST               9                    9
Move in the middle of the board     5              5          WEST               4                    5
Move towards the bottom of board    4              1          SOUTH              4                    0
Move towards the edge of the board  0              3          WEST               0                    3
Move in the middle of the board     6              4          NORTH              6                    5


*** Keywords ***
Move character
    [Arguments]    ${StartingX}  ${StartingY}  ${Direction}  ${EndingX}  ${EndingY}
     Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}
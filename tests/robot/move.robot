*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
http://arcobotics.com/wp-content/uploads/2015/12/sparki-driver-icon.png
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX      StartingY      Direction     EndingX    EndingY 
Move in the middle of the board     0              0          NORTH              0                    1
Move in the edge of the board       0              0          SOUTH              0                    0



*** Keywords ***
Move character
    [Arguments]    ${StartingX}  ${StartingY}  ${Direction}  ${EndingX}  ${EndingY}
    Initialize character xposition with ${StartingX}
    Initialize character xposition with ${StartingY}
    Move iun direction           ${Direction}
    Character xpositions should be  ${EndingX}
    Character ypositions should be  ${EndingY}

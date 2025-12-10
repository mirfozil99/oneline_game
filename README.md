# oneline_game
game made in Python command line 
Game Description
A turn-based game in which the player battles a monster. Each participant can perform one of the available actions on their turn. The game continues until one participant’s health reaches zero. The winner is the one who remains with a positive health value.
Game Mechanics
Participants:
Player: the character controlled by the user.
Monster: the character controlled by the system (randomly choosing actions).
Character Actions:
ATTACK: deals a fixed amount of damage to the opponent.
HEAL: restores a certain amount of health, but not above the maximum value.
SKIP: does nothing and passes the turn to the next participant.
Objective:
Defeat the opponent by reducing their health to zero.
Turn Order:
The player goes first, then the monster. Turns alternate.
Gameplay
Game Start:
Two characters are initialized: the player and the monster.
Each character has a name, initial health, and maximum health.
Action Selection:
The player manually selects an action by entering the corresponding choice (e.g., through a text interface or menu).
The monster randomly selects one of the three actions.
Action Processing:
The chosen action is executed and immediately affects the opponent or the acting character.
Order of execution:
The player selects an action → the action is processed.
The monster selects an action → the action is processed.
Game End:
The game ends when one character’s health reaches zero.
The result is displayed: the winner’s name and remaining health.
Functional Requirements
Initialization:
Each character has a name, current health, and maximum health.
The initial parameters for the player and the monster are identical.
Game Loop:
The loop continues until one participant’s health becomes 0.
Within each turn:
The player selects an action through the interface (e.g., entering a number that corresponds to an action).
The monster selects an action randomly.
Action Processing:
ATTACK: decreases the opponent’s health by a fixed amount.
HEAL: restores the character’s health, but not above the maximum value.
SKIP: makes no changes.
Game Result:
After the game ends, a message is displayed announcing the winner.
Non-Functional Requirements
Extensibility:
Easy addition of new character types (for example, player allies or different monsters).
Support for new action types without modifying the core structure.
Modularity:
The code should be divided into logically separate components (characters, actions, game logic).
Usability:
A simple and intuitive interface for selecting actions.
Clear messages about turn outcomes and character status.
Performance:
Game logic should run quickly and not depend on the number of characters or action types.
Success Criteria
The game loop ends correctly (when one participant’s health reaches 0).
All three action types are processed according to the described rules.
The user can easily control the character through the interface.
New characters or actions can be added with minimal effort.

Good luck, everyone gg

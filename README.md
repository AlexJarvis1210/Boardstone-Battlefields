
# Boardstone: Battlefields

Welcome to the nexus of strategy and sorcery, where card meets grid in a clash of tactical prowess and magical might. Boardstone: Battlefields is a hex-grid card battle game that combines the intricate mechanics of card-based strategy with the spatial dynamics of board game play.

In this realm, two players face off in a world where wit equals might, and a well-played card can turn the tide of battle. Each contender wields a deck of carefully chosen cards, representing valiant minions and powerful spells. The objective is clear: obliterate your opponent’s base or outlast them on the battlefield to claim victory.

This game is a tribute to the classics, drawing inspiration from the venerable Hearthstone's intuitive card play and the strategic depth of hex-based board games. It’s a hybrid that challenges players to not only consider the cards in their hand but also the lay of the land, as they maneuver their minions across a dynamic battlefield peppered with obstacles and opportunities alike.

Players must manage their resources wisely, balancing the deployment of minions with the casting of spells, all the while anticipating their opponent’s moves. With a variety of card types, including tanks, healers, DPS, ranged units, and spellcasters, the possibilities for combat and strategy are endless.

Prepare for battle, strategize with precision, and step onto the battlefield of hexes. In Boardstone: Battlefields, only the most cunning will prevail.

---

## Gameplay

### Card Types and Categories

- **Minions**:
  - **Tank**: Minions with high health that can absorb damage.
  - **Healer**: Minions that can restore health to other minions or the player's base.
  - **DPS (Damage Per Second)**: High-damage minions, crucial for offensive strategies.
  - **Ranged**: Minions that can attack from a distance without needing to be adjacent to the target.
  - **Spellcaster**: Minions with abilities that can cast spells or influence the battlefield in various ways.

- **Spells**:
  - Influence the game by being played directly from the hand.
  - Can be buffs, debuffs, direct damage, or healing spells.
  - Mana cost is proportional to their impact level.

### Card Mechanics

- **Battlecry**: A special action that occurs when the minion is played from the hand.
- **Deathrattle**: An effect that takes place when the minion dies.
- **Targeting**: Battlecries can target minions to apply buffs or debuffs.

### Movement Mechanics

- Players have a pool of movement points to allocate for repositioning minions on the board each turn.
- This pool replenishes each turn and can be modified by spell effects or minion abilities.

### Combat Rules

- **Turn-Based Combat**: Minions cannot attack the turn they are played unless they have the 'Rush' ability.
- **Ranged Combat Challenge**: Ranged minions can attack from a distance, but traditionally in games like Hearthstone, they would not receive return damage if the target is not in range to retaliate. We need to deliberate on how to balance this for Boardstone: Battlefields.

### Special Abilities

- **Stealth**: Minions cannot be targeted by attacks or spells while in stealth.
- **Rush**: Allows minions to attack on the same turn they are played.
- **Charge**: Considering implementation. It would let minions attack immediately, disregarding movement restrictions.
- **Taunt**: We aim to reimagine taunt mechanics for tank minions to add a unique tactical layer to the game.

### Base Mechanics

- The player's base starts with 30HP.
- Bases can have abilities triggered for a mana cost, similar to Hearthstone's hero powers.

---

**Challenges and Considerations:**

- **Ranged Combat Resolution**: For ranged attackers, it might be unrealistic for a melee minion to deal return damage if it's struck from a distance. One solution could be to introduce the concept of 'armor' or 'shielding' for melee units to abstractly represent their defensive capabilities against ranged attacks. Alternatively, ranged minions could have reduced health to balance their advantage of range, making them more vulnerable to indirect effects or spells.

- **Taunt Mechanic Redesign**: Traditional taunt mechanics force attacks to be directed towards taunting minions. For a novel approach, we could consider:
  - **Zone Control**: Tank minions could create a zone of control around them, where enemy minions must stop if they enter it, limiting their movement and possibly forcing engagement.
  - **Provocation**: Instead of forcing the attack, taunt could reduce the damage of enemy minions unless they attack the 'taunting' minion, simulating a distraction mechanic.

### Endgame Scenarios

- **Base Destruction**: The primary victory condition is to reduce the opponent's base health to zero.
- **Fatigue**: If a player exhausts their deck, they take increasing fatigue damage each turn, starting at 1 and incrementing by 1 with each subsequent turn without a card to draw.

### Card Draw Mechanics

- Players draw one card at the beginning of their turn.
- Additional card draw mechanics are integrated within battlecry and deathrattle effects, spells, and other special abilities.
- The frequency of card draws will require balancing to ensure players neither consistently have too few nor too many cards.

### Board Layout

- The battlefield is laid out in a hex grid, starting with 3 hex's on line 1 (includng the base), each subsequent row has 1 more hex up to and including row = 9. This is mirrored on each side of the map.
- Random, yet symmetrical tiles are placed to ensure fair play. These could potentially include special tiles that trigger effects when a minion lands on them.

### Development Notes

- **Special Tiles**: Consider adding various tiles that trigger different effects for more dynamic gameplay. This feature would require careful design to maintain game balance.
- **Balancing**: Ongoing testing is needed to fine-tune the frequency and impact of card draw mechanics, special abilities, and the interplay between different minion types.

****************************************************************************************************

Breakdown of tasks:

*****CURRENT STAGE******
1. **Game Setup and Initialization**: This includes setting up the game board, initializing player bases, and shuffling the decks.
   - Define the game board layout and hex grid system.
   - Create player classes with health, mana, and deck initialization.
   - Implement deck shuffling and the draw mechanism.

2. **Card Implementation**: Define the card classes and their properties.
   - Implement different card types (minions and spells) with their attributes.
   - Code the special abilities (battlecry, deathrattle, etc.).

3. **Game Mechanics**: Develop the core gameplay mechanics.
   - Implement the turn-based system.
   - Code the movement mechanics and the allocation of movement points.
   - Develop the combat rules and interactions between cards.

4. **User Interface (UI)**: While this is often parallel to the game mechanics, it's crucial for testing.
   - Develop a basic UI to interact with the game.
   - Display the board, cards, and basic game information.

5. **Gameplay Loop**: Code the main game loop where players take turns until the game ends.
   - Implement the conditions for each phase of a turn.
   - Code the win/loss conditions.

6. **Testing and Balancing**: This is an iterative process where you test game mechanics and balance them.
   - Create test cases for different game scenarios.
   - Adjust card attributes and mechanics based on testing feedback.

7. **Polishing and Refinement**: Finalize the game by adding additional features and polishing existing ones.
   - Implement advanced UI/UX features.
   - Refine the game mechanics based on extensive playtesting.

8. **Documentation and Cleanup**: Ensure that the code is well-documented and clean.
   - Add comments and documentation.
   - Refactor code for efficiency and readability.




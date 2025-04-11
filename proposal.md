# Desktop Flower Farm

## Repository
https://github.com/AshleySimo/utd-angm2305-25s-final-AshleySimo.git

## Description
This program will open a small window with a simple desktop farming game. In the game, you will be able to plant flowers, water them, harvest them, sell the yield, and buy seeds. It is relevant by being a form of entertainment or relaxation utilizing a simplified version of the popular farming simulator genre.

## Features
- Animated Movements
  - The player will be able to move their character using the Vector2 movement system supplied within PyGame. As the player moves, their "status" will be updated, corresponding to a list containing image files of these small animations. With these animated movements, the player will be able to see their character walk, till the ground, and water their plants. 
- Planting
  - When the player hits "C" on their keyboard, they will be able to plant a flower on one of the set plantable tiles in the game. This will be done using a collisions detector within PyGame; when the player hitbox is colliding with a soil hitbox and the player presses "C", a flower is planted.
- Growing & Harvesting
  - Every flower will have a grow rate that is dependent on delta time; As the flower age increases, the flower sprite is updated to make it appear that the flower is growing. When the flower has reached its max age, it can be harvested by the player simply by walking over it using collisions. When the flower is harvested, a flower item will be added to the players inventory.
- Inventory
  - The inventory will be a simple dictionary. The items (keys) the player can have in their inventory is coins, flower seeds, and flowers. The player will start with 100 coins, 5 seeds, and 0 flowers. The values of these keys will increase or decrease as the player preforms specific actions.
- Buy/Sell
  - The player will be able to open a shop menu by pressing "E" on their keyboard. In this shop, their coins, flower seeds, and flowers will be listed with their value pairs (amount of each). By clicking the flower seeds, they will be able to buy one at a time, decreasing their coin value by 20 each time. By clicking the flowers, they will be able to sell one at a time, increasing their coin value by 35 each time. 

## Challenges
- Will need to learn how to create animated movements as the player moves the character. This includes the direction the sprite faces changing depending on the direction the player is moving. 
- Will need to learn how to properly use collisions to allow the player to plant and harvest the flowers. 
- Will need to learn how to display the inventory key/value pairs in a shop menu and use mouse collisions to allow the player to buy/sell in that menu. 

## Outcomes
Ideal Outcome:
- The ideal outcome is all of the above features being implemented in a way that consistently works and allows for an endless game loop for the player. The actions above should be able to execute over and over again; the game has no effective "end."

Minimal Viable Outcome:
- Some of the features listed above are implemented and consistently working. The minimum features include the player having control of the characters movements, the related animations update and display on the screen, and the player should be able to plant and harvest crops.

## Milestones
- Week 1 (4/13-4/19)
  1. Implement the game window, including the tile grass background and the placement of the soil patches where flowers can be grown.
  2. Implement the character and the characters animations. This can be done with temporary image files at this point.
  3. Begin work on the character sprites. This will include an idle sprite for the up, down, left, and right directions, as well as walking sprites for those directions. This will also include a sprite for planting a flower in every direction.

- Week 2 (4/20-4/26)
  1. Implement the players inventory, flower planting, flower growth, and harvesting.
  2. Complete flower sprites for each growth state (seedling, sprout, budding, flowering).

- Week 3 (4/27-5/3)
  1. Implement the shop menu and buy/sell actions.

- Week 4 (5/4-5/10)
  1. Complete any features that have not yet been completed.
  2. Complete the demo video of the game and upload to YouTube.
  3. Final Project Completion: 5/12, 11:59PM

# DESKTOP FLOWER FARM
This is my final project for ANGM 2305: Programming for Digital Arts!

## Demo
Demo Video: https://youtu.be/46bTjFzOChQ

## GitHub Repository
GitHub Repo: https://github.com/AshleySimo/utd-angm2305-25s-final-AshleySimo.git

## Description
Desktop Flower Farm is a small, desktop farm simulator meant to run alongside you while you go about your day on your computer. The name is the game: farm flowers on your desktop! You play as a cute farmdog who loves planting poppies. Watch them grow, harvest them, and come back to plant more whenever you need a break from life! 

The style of Desktop Flower Farm is meant to be simple and reminiscent of the popular farming game, Stardew Valley, which is where I got my initial inspiration from. It features a pixel art style with bright colors and small animations for idling, planting, and walking. Due to no character customization, rather than creating a human sprite, you play as a more malleable and relatable farm dog! Call them whatever you like, or call them by your name! In this 640x480 window, the world is what you make of it. Rather, it's a peaceful field ripe for poppy planting. You can plant flowers in any tile on the screen, giving full creative liberty to the player! They grow in five stages: seedling, sprout, fledgling, budding, and bloomed! Once they're full grown, you can leave them, harvest them, or plant more! The only thing you need to keep track of is the number of flowers you've planted--if you want to check the counter in the top left corner, of course.

- Files Provided
  - project.py: This is the python file containing the game itself! Here, you can simply run the file in the terminal, and Desktop Flower Farm will open on your desktop!
  - support.py: This is a custom support file which houses one custom function and one class. This file allows the assets to be loaded into the game and the planting animation to not run forever! Does not need to be opened, tampered with, or ran in the terminal; this file only needs to exist in the same directory as project.py. 
  - assets: This is the directory where the magic happens! Metaphorically. This folder contains subfolders that contain all of the images needed to make Desktop Flower Farm appear as beautifully as it does on your screen. That includes the grass, the flowers growth stages, and the many images needed to create the animations of the farm dog player! This folder needs to exist in the same directory as project.py.
As given in the GitHub repo, it should be sufficient for the player to download the "src" folder with everything in it, and all of the necessary files will be in the right place for Desktop Flower Farm to run smoothly!

- Future Areas of Improvement
  - The hitbox for the player tends to overlap with multiple grass tiles at once, which sometimes causes two flowers to be planted at once. With more hitbox and collision work, the planting mechanism could be improved to stop this from happening and allow the player to plant a flower on the tile over from wherever they are facing.
  - The harvesting mechanic experiences some bugs currently which may cause multiple flowers to be harvested at once across the screen or none to be harvested at all when you collide with a fully grown flower. 
  - In the future, this game could be expanded to include tilling soil, watering plants, having an inventory and coins, and being able to sell flowers and buy seeds. It could even be improved to include multiple different types of flowers, allowing the player to get more creative with their flower assortments.

## Tutorials/References
https://youtu.be/T4IX36sP_0c?si=kugHLDFCf1bOIlNG
https://youtu.be/BHr9jxKithk?si=AJyZrDZPMN10SFTX

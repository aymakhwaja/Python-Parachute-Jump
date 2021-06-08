#Ayma Khwaja
#ak6xbg

#This is a parachute game where the player has to avoid hitting the red and black bombs in order
#to survive. There is a health bar, collectible hearts which increase health, and 3 levels in which
#the game gets faster every level.


import pygame
import gamebox
import random



start = False



#camera
camera = gamebox.Camera(700,550)

#grounds are the sides of the camera display screen
ground1 = gamebox.from_color(0,614,"lightblue",9999999999,140)
ground2 = gamebox.from_color(0,-66,"lightblue",999999999,140)
ground3 = gamebox.from_color(-45,0,"lightblue",100,9999999)

grounds = [ground1, ground2]


#cover and instructions
cover = gamebox.from_image(349,275,"cov.png")
cover.scale_by(1.04)

#main character
chara = gamebox.from_image(400,105,"char.png")
chara.scale_by(1)



#clouds
clouds1 =gamebox.from_image(400,300,"cloud.png")
clouds1.scale_by(0.85)
clouds1.left = camera.left

clouds2 =gamebox.from_image(500,0,"cloud.png")
clouds2.scale_by(0.85)
clouds2.left = clouds1.right


def place_background1():
    #this assists in creating a scrolling background
    if clouds1.right < camera.left:
        clouds1.left = clouds2.right
    if clouds2.right < camera.left:
        clouds2.left = clouds1.right

# scrollspeeds depending on the level
scrollspeed = 4
scrollspeed2 = 8
scrollspeed3 = 12
scrollspeed4 = 2


background1 = [clouds1, clouds2,chara]

chara.center = [100,300]


# empty lists that are appended to and variables used in tick function
hazards = []
hazards2 = []
hazards3 = []
hearts = []
counter = 0
score = -1
health = 100

def tick(keys):
    # this is the main function to animate the game
    global start, score, counter, health

    counter += 1
#game is not on (displays cover and instructions) until the player hits the spacebar
    if score == -1:
        camera.draw(cover)
        if pygame.K_SPACE in keys:
            start = True
            score = 0

#else means the game is on
    else:
        # LEVEL 1
        if score < 500:
            camera.clear("lightblue")
            camera.x += scrollspeed
            chara.move(4, 0)
            # animates background
            for object in background1:
                place_background1()
                camera.draw(object)

            # level 1 bombs, this code randomizes the x,y coordinates of bombs
            if counter % 50 == 0:
                numhazards = random.randint(0, 2)
                for i in range(numhazards):
                    hazards.append(gamebox.from_image((1000), random.randint(-20, 550), "bomb.png"))

            for hazard in hazards:
                hazard.x -= 5

                if hazard.touches(ground3):
                    hazard.move(random.randint(1200, 1500), random.randint(-100, 20))

                if hazard.touches(chara):
                    health -= 1
                camera.draw(hazard)

        # LEVEL 2
        if score > 499:
            camera.clear("dodgerblue")
            camera.x += scrollspeed2
            chara.move(8, 0)
            for object in background1:
                place_background1()
                camera.draw(object)

            #level 2 bombs
            if counter % 50 == 0:
                numhazards2 = random.randint(0, 2)
                for i in range(numhazards2):
                    hazards2.append(gamebox.from_image((4800), random.randint(-20, 550), "bomb2.png"))

            for hazard in hazards2:
                hazard.x -= 9

                if hazard.touches(ground3):
                    hazard.move(random.randint(2000, 3000), random.randint(-100, 20))

                if hazard.touches(chara):
                    health -= 1
                camera.draw(hazard)

        # LEVEL 3
        if score > 1000:
            camera.clear("steelblue")
            camera.x += scrollspeed3
            chara.move(12, 0)
            for object in background1:
                place_background1()
                camera.draw(object)
            #level 3 bombs
            if counter % 40 == 0:
                numhazards3 = random.randint(0, 4)
                for i in range(numhazards3):
                    hazards3.append(gamebox.from_image((7500), random.randint(0, 550), "bomb2.png"))
                    hazards3.append(gamebox.from_image((8500), random.randint(-20, 550), "bomb.png"))


            for hazard in hazards3:
                hazard.x -= 13

                if hazard.touches(ground3):
                    hazard.move(random.randint(6700, 8000), random.randint(-100, 20))
                if hazard.touches(chara):
                    health -= 1
                camera.draw(hazard)

        # victory
        if score >1499:
            camera.clear("lightblue")
            camera.x += scrollspeed4
            chara.move(4, 0)
            for object in background1:
                place_background1()
                camera.draw(object)

     #victory text
            win = gamebox.from_text(camera.left + 300, 20, "YOU WON!!! ", 50, 'pink')
            camera.draw(win)
            if score > 1549:

                gamebox.pause()


        scoreboard = gamebox.from_text(camera.left + 55, 20, "Score: " + str(score), 24, 'darkslategray')
        camera.draw(scoreboard)
        camera.draw(ground1)
        camera.draw(ground2)

        score += 1


        camera.draw(ground3)
        ground3.move(4, 0)

# this randomizes the heart collectibles. if health is below 100 they increase health
        if counter % 100 == 0:
            numhearts = random.randint(0, 2)
            for i in range(numhearts):
                hearts.append(gamebox.from_image((1000), random.randint(-100, 600), "heart.png"))
        for heart in hearts:
            heart.x -= 5

            if heart.touches(ground3):
                heart.move(random.randint(1000, 2000), random.randint(-100, 20))
            if heart.touches(chara) and health < 100:
                    health += 1
            camera.draw(heart)



        if score < 1500 and health == 0:
            lost = gamebox.from_text(camera.left +300 , 20, "YOU LOST ", 50, 'pink')
            camera.draw(lost)
            gamebox.pause()

# this makes sure the character doesn't go past the sides of the game and stays within frame
        for item in grounds:
            if chara.touches(item):
                chara.move_to_stop_overlapping(item)
            camera.draw(item)

# this text displays health
        lives = gamebox.from_text(camera.right -100, 20, "Parachute Health: " + str(health), 24, 'navyblue')
        camera.draw(lives)


# user control keys allow them to move up and down to dodge objects
        if pygame.K_DOWN in keys:
            chara.y += 6
        if pygame.K_UP in keys:
            chara.y -= 6


    camera.display()


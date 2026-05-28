def on_button_pressed_a():
    Bird.change(LedSpriteProperty.Y, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Bird.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Bird: game.LedSprite = None
Bird = game.create_sprite(0, 2)
Bird.set(LedSpriteProperty.BLINK, 300)
Obstacles: List[game.LedSprite] = []
emptyObstacleY = randint(0, 4)

def on_forever():
    global emptyObstacleY
    Ticks = 0
    while len(Obstacles) > 0 and Obstacles[0].get(LedSpriteProperty.X) == 0:
        Obstacles.remove_at(0).delete()
    for Obstacle in Obstacles:
        Obstacle.change(LedSpriteProperty.X, -1)
    if Ticks % 3 == 0:
        emptyObstacleY = randint(0, 4)
        for index in range(5):
            if index != emptyObstacleY:
                Obstacles.append(game.create_sprite(4, index))
        basic.pause(1000)
    for Obstacle2 in Obstacles:
        if Obstacle2.get(LedSpriteProperty.X) == Bird.get(LedSpriteProperty.X) and Obstacle2.get(LedSpriteProperty.Y) == Bird.get(LedSpriteProperty.Y):
            game.game_over()
basic.forever(on_forever)

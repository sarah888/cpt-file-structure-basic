keys_pressed = [False for key_code in range(256)]

def setup():
    global player_position
    size(640, 480)
    player_position = PVector(width/2, height/2)


def draw():
    background(0)
    print([i for i, is_pressed in enumerate(keys_pressed)
             if is_pressed])
    
    if keys_pressed[ord('A')]:  # left
        player_position.x += -3
    elif keys_pressed[ord('D')]:  # right
        player_position.x += 3
            
    if keys_pressed[ord('W')]:  # up
        player_position.y += -3
    if keys_pressed[ord('S')]:  # down
        player_position.y += 3
        
    fill(255)
    ellipse(player_position.x, player_position.y, 20, 20)
        

def keyPressed():
    keys_pressed[keyCode] = True

def keyReleased():
    keys_pressed[keyCode] = False

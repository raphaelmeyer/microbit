import microbit
import random
import radio
import music

can_sing = microbit.pin0.is_touched()
radio.on()

def listen():
    for i in range(5):
        answer = radio.receive()
        if answer is not None:
            return answer
        microbit.sleep(100)
    return None

def respond(message):
    if message == 'hello':
        radio.send('how are you')
    elif message == 'can you sing':
        if can_sing:
            radio.send('yes')
            music.play(music.ODE)
        else:
            radio.send('no')

def start_talking():
    radio.send('hello')
    answer = listen()
    if answer == 'how are you':
        radio.send('can you sing')
        answer = listen()
        if answer == 'yes':
            microbit.display.show(microbit.Image.HAPPY)
        elif answer == 'no':
            microbit.display.show(microbit.Image.SAD)
        else:
            microbit.display.show(microbit.Image.CONFUSED)
        microbit.sleep(2000)
        microbit.display.clear()

################################################################

while True:
    if random.random() < 0.05:
        start_talking()
    else:
        message = listen()
        if message is not None:
            respond(message)
    microbit.sleep(100)
    
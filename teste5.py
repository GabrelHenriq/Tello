from djitellopy import Tello

tello = Tello()
i = 0

tello.connect()
tello.takeoff()

while i <= 4:
    tello.move_forward(500)
    i += 1

i = 0

tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(180)
tello.rotate_counter_clockwise(90)

while i <= 4:
    tello.move_forward(500)
    i += 1

tello.land()
tello.end()
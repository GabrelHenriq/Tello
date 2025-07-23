from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(230)
tello.rotate_counter_clockwise(90)
tello.move_forward(90)
tello.rotate_counter_clockwise(90)
tello.move_forward(230)

tello.land()
tello.end()
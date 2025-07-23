from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_forward(500)
tello.move_forward(500)
tello.move_forward(440)
tello.rotate_counter_clockwise(90)
tello.move_forward(150)


tello.land()
tello.end()
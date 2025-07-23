from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.go_xyz_speed(200, 90, -10, 100)

tello.land()
tello.end()
from djitellopy import Tello
from processvid import processar_video

tello = Tello()

tello.connect()
tello.takeoff()

tello.streamon()
processar_video(tello)


tello.land()
tello.end()
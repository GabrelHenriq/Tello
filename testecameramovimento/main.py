import threading
import cv2
from djitellopy import Tello

video_pronto = threading.Event()

def voo(tello):
    video_pronto.wait()

    tello.takeoff()
    tello.move_forward(50)
    confirmar = input('Digite S para continuar')
    if confirmar == 's' and confirmar == 'S':
        tello.rotate_counter_clockwise(180)
        confirmar2 = input('Digite S para continuar')
        if confirmar2 == 's' and confirmar2 == 'S':
            tello.move_forward(50)
        else: tello.land()
    else: tello.land()    
    tello.land()


def stream_video(tello):
    while True:
        frame = tello.get_frame_read().frame
        cv2.imshow('Tello', frame)
        if not video_pronto.is_set():
            video_pronto.set()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def main():
    tello = Tello()
    tello.connect()
    tello.streamon()

    video_thread = threading.Thread(target=stream_video, args=(tello,))

    video_thread.daemon = True

    video_thread.start()

    voo(tello)

    tello.reboot()


if __name__ == "__main__":
    main()
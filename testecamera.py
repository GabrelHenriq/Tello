import cv2
from djitellopy import Tello

def processar_video(tello):
    while True:
        frame = tello.get_frame_read().frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    tello.end()


def main():

    tello = Tello()

    tello.connect()

    tello.streamon()

    processar_video(tello)

if __name__ == "__main__":
    main()
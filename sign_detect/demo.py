import cv2

server = 'rtsp://192.168.1.8:8080/h264_opus.sdp'
cap = cv2.VideoCapture(server)

while True:
    ret, frame = cap.read()
    if ret:
        print(frame.shape)  # This should print a tuple with width and height
        cv2.imshow("Image", frame)
    else:
        print("Error: Could not capture frame")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
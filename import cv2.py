import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
reconhecimentoFacial = mp.solutions.face_detection
reconhecedorFacial = reconhecimentoFacial.FaceDetection()
desenho = mp.solutions.drawing_utils

if webcam.isOpened():
    while True:
        validar, frame = webcam.read()
        print(frame)
        listaRostos = reconhecedorFacial.process(frame)

        if listaRostos.detections:
            for rosto in listaRostos.detections:
                desenho.draw_detection(frame, rosto)

        cv2.imshow("Reconhecimento Facil", frame)
        if cv2.waitKey(2) == 27:
            break
    cv2.imwrite("Foto.png", frame)

webcam.release()


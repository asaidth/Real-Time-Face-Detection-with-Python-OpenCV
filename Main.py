from pathlib import Path

import cv2


BASE_DIR = Path(__file__).resolve().parent
CASCADE_PATH = BASE_DIR / "Modelos" / "haarcascade_frontalface_default.xml"


def main() -> None:
    face_cascade = cv2.CascadeClassifier(str(CASCADE_PATH))
    if face_cascade.empty():
        raise RuntimeError(
            f"No se pudo cargar el clasificador Haar Cascade: {CASCADE_PATH}"
        )

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError(
            "No se pudo acceder a la cámara. Verifica que esté conectada "
            "y que ninguna otra aplicación la esté usando."
        )

    print("Presiona 'q' para cerrar la ventana.")

    try:
        while True:
            success, frame = camera.read()
            if not success:
                print("No se pudo leer un fotograma de la cámara.")
                break

            grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                grayscale_frame,
                scaleFactor=1.1,
                minNeighbors=5,
            )

            for x, y, width, height in faces:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + width, y + height),
                    (0, 255, 0),
                    2,
                )

            cv2.imshow("Detección facial en tiempo real", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

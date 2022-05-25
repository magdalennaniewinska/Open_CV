import cv2 as cv
import mediapipe as mp
import time


class FaceMesh():
    def __init__(self, max_num_faces=2):
        self.max_num_faces = max_num_faces
        self.mpFaceMesh = mp.solutions.face_mesh
        self.mpDraw = mp.solutions.drawing_utils
        self.face_mesh = self.mpFaceMesh.FaceMesh(max_num_faces=self.max_num_faces)

    def find_mesh(self, img, draw=True):
        # Convert image
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # Use face detection model
        self.results = self.face_mesh.process(imgRGB)

        faces = []
        if self.results.multi_face_landmarks:
            # print(results.multi_face_landmarks)
            for faceLm in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLm, self.mpFaceMesh.FACEMESH_CONTOURS)
                face = []
                for id, lm in enumerate(faceLm.landmark):
                    # Transform landmarks to pixel values
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, cx, cy)
                    face.append([cx, cy])
                faces.append(face)
        return img, faces


def main():
    cap = cv.VideoCapture('FaceVideos/2.mp4')
    pTime = 0
    detector = FaceMesh()

    while True:
        success, img = cap.read()
        img, faces = detector.find_mesh(img)
        # if len(faces):
        #    print(len(faces))

        # Measure FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display img
        cv.putText(img, f"FPS:{(int(fps))}", (100, 100), cv.FONT_HERSHEY_COMPLEX_SMALL, 7, (255, 0, 0), 2)
        cv.imshow("Image", img)
        # The 'q' button is set as the quiting button
        if cv.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()

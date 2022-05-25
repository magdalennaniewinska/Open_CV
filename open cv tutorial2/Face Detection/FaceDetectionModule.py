import cv2 as cv
import mediapipe as mp
import time


class FaceDetection():
    def __init__(self, detection_confidence=0.5):
        self.detection_confidence = detection_confidence
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.face_detection = self.mpFaceDetection.FaceDetection(self.detection_confidence)

    def find_face(self, img, draw=True):
        # Convert image
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # Use face detection model
        self.results = self.face_detection.process(imgRGB)

        bboxs = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                h, w, c = img.shape
                bbox_from_class = detection.location_data.relative_bounding_box
                bbox = int(bbox_from_class.xmin * w), int(bbox_from_class.ymin * h), \
                       int(bbox_from_class.width * w), int(bbox_from_class.height * h)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    cv.rectangle(img, bbox, (255, 0, 255), 2)
                    cv.putText(img, f"{(int(detection.score[0] * 100))}%", (bbox[0], bbox[1] - 20), cv.FONT_HERSHEY_PLAIN,
                               3, (0, 255, 0), 2)

        return img, bboxs


def main():
    pTime = 0
    detector = FaceDetection(0.5)

    cap = cv.VideoCapture(0)

    while True:
        success, img = cap.read()
        img, bboxs = detector.find_face(img)

        # Measure FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        # Display img
        cv.putText(img, f"FPS:{(int(fps))}", (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
        cv.imshow("Image", img)

        # The 'q' button is set as the quiting button
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()

import cv2
import mediapipe as mp

class handDetector():
    # Khởi tạo thư viện mediapipe
    def __init__(self):

        # gán thuộc tính mpHands bằng mp.solutions.hands (thư viện mediapipe)
        self.mpHands = mp.solutions.hands
        # Khởi tạo bộ phát hiện tay (Hands)
        self.hands = self.mpHands.Hands()
        # Khởi tạo bộ vẽ landmark (drawing_utils)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        # Chuyển từ BGR thành RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Đưa vào thư viện mediapipe
        results = self.hands.process(imgRGB)

        # Khởi tạo list chứa các toạ độ của khớp của các ngón tay
        hand_lms = []

        # Kiểm tra có tìm thấy bàn tay hay không
        if results.multi_hand_landmarks:

            # Vẽ landmark cho các bàn tay
            for handlm in results.multi_hand_landmarks:
                # Vẽ các khớp của các ngón tay
                self.mpDraw.draw_landmarks(img, handlm, self.mpHands.HAND_CONNECTIONS)


            # Trích ra các toạ độ của khớp của các ngón tay
            firstHand = results.multi_hand_landmarks[0]

            h, w, _ = img.shape


            # enumerate: lấy ra index và giá trị của phần tử trong list
            for id, lm in enumerate(firstHand.landmark):
                # lm.x: tọa độ x của khớp tay (ví dụ 0.5) => nhân với chiều rộng để ra tọa độ thực
                # lm.y: tọa độ y của khớp tay (ví dụ 0.5) => nhân với chiều cao để ra tọa độ thực
                # print(id, lm.x, lm.y)
                real_x, real_y = int(lm.x * w), int(lm.y * h)

                hand_lms.append([id, real_x, real_y])

        return img, hand_lms


    def count_finger(self, hand_lms):
        finger_start_index = [4, 8, 12, 16, 20]
        finger_end_index = [3, 6, 10, 14, 18]
        n_fingers = 0

        if len(hand_lms) > 0:
            # kiểm tra ngón cái
            if hand_lms[finger_start_index[0]][1] < hand_lms[finger_end_index[0]][1]:
                n_fingers += 1

            # kiểm tra các ngón còn lại
            for idx in range(1, 5):
                if hand_lms[finger_start_index[idx]][2] < hand_lms[finger_end_index[idx]][2]:
                    n_fingers += 1

            return n_fingers
        else:
            return 0


    # Cách 2
    def count_finger_2(self, hand_lms):
        finger_start_index = [4, 8, 12, 16, 20]
        n_fingers = 0

        if len(hand_lms)>0:
            # Kiểm tra ngón cái
            if hand_lms[finger_start_index[0]][1]< hand_lms[finger_start_index[0]-1][1]:
                n_fingers +=1

            # Kiểm tra 4 ngón còn lại
            for idx in range(1,5):
                if hand_lms[finger_start_index[idx]][2] < hand_lms[finger_start_index[idx]-2][2]:
                    n_fingers +=1

            return n_fingers
        else:
            return -1




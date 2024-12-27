import cv2
import numpy as np
import time

print("Opening camera. Stay out of the frame for 30 frames. To end the session, press 'Esc'.")

cap = cv2.VideoCapture(0)
time.sleep(2)
background = None

for _ in range(30):
    ret, frame = cap.read()
    if not ret:
        print("Error capturing background frame.")
        break
    background = cv2.flip(frame, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error capturing video frame.")
        break

    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound1 = np.array([0, 120, 50])
    upper_bound1 = np.array([10, 255, 255])
    lower_bound2 = np.array([170, 120, 50])
    upper_bound2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv_frame, lower_bound1, upper_bound1)
    mask2 = cv2.inRange(hsv_frame, lower_bound2, upper_bound2)

    combined_mask = cv2.bitwise_or(mask1, mask2)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    mask_inverse = cv2.bitwise_not(combined_mask)
    background_segment = cv2.bitwise_and(background, background, mask=combined_mask)
    current_frame_segment = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    output_frame = cv2.addWeighted(background_segment, 1, current_frame_segment, 1, 0)
    cv2.imshow('Magic O.O', output_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

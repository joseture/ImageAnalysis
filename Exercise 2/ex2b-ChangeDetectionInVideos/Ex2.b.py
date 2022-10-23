import time
import cv2
import numpy as np


def show_in_moved_window(win_name, img, x, y):
    """
    Show an image in a window, where the position of the window can be given
    """
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, x, y)
    cv2.imshow(win_name,img)


def capture_from_camera_and_show_images(alpha):
    print("Starting image capture")

    print("Opening connection to camera")
    url = 0
    use_droid_cam = False
    if use_droid_cam:
        url = "http://10.2.10.116:4747/http://10.2.10.116:4747/video"
    cap = cv2.VideoCapture(url)
    # cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    print("Starting camera loop")
    # Get first image
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame")
        exit()

    # Transform image to gray scale and then to float, so we can do some processing
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

    # To keep track of frames per second
    start_time = time.time()
    n_frames = 0
    stop = False
    while not stop:
        ret, new_frame = cap.read()
        if not ret:
            print("Can't receive frame. Exiting ...")
            break

        # i. Transform image to gray scale and then to float, so we can do some processing
        new_frame_gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY).astype(np.float32)

        # ii. Compute difference image
        dif_img = np.abs(new_frame_gray - frame_gray)
        
        # iii. Creates a binary image by applying a threshold, T, to the difference image.
        ret, thres = cv2.threshold(dif_img, 100, 255, cv2.THRESH_BINARY)  
        
        # iv. Computes the total number of foreground, F, pixels in the foreground image.
        F = np.sum(thres == 0)
        
        # v. Compute the percentage of foreground pixels compared to the total number of pixels in the image (F).
        per = F/(480*640)
        
        # if (per != 1.0):
        #     print( "Foreground:", F, "Percentage:", per)

        # vi. Decides if an alarm should be raised if F is larger than an alert value, A.
        if (per < 0.9995):
            str_out2 = f"Change detected!"
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(thres, str_out2, (150, 100), font, 1, 255, 1)
               
        # vii. Shows the input image, the backround image, the difference image, and the binary image. The binary image should be scaled by 255.

        str_out3 = f"Foreground pixels: {480*640 - F}"
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(thres, str_out3, (200, 200), font, 0.5, 255, 1)
        
        
        # Keep track of frames-per-second (FPS)
        n_frames = n_frames + 1
        elapsed_time = time.time() - start_time
        fps = int(n_frames / elapsed_time)

        # Put the FPS on the new_frame
        str_out = f"fps: {fps}"
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(new_frame, str_out, (100, 100), font, 1, 255, 1)

        # Display the resulting frame
        show_in_moved_window('Input', new_frame, 0, 10)
        # show_in_moved_window('Input gray', new_frame_gray.astype(np.uint8), 600, 10)
        show_in_moved_window('Binary', (thres).astype(np.uint8), 600, 10)
        show_in_moved_window('Difference image', dif_img.astype(np.uint8), 1200, 10)

        # Old frame is updated
        #frame_gray = new_frame_gray
        frame_gray = alpha*frame_gray+(1-alpha)*new_frame_gray
        
        if cv2.waitKey(1) == ord('q'):
            stop = True

    print("Stopping image loop")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    
    alpha = 0.95
    capture_from_camera_and_show_images(alpha)
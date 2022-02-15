import cv2

def get_opencv_result(video_to_process, out_background_filename):
    # create VideoCapture object for further video processing
    captured_video = cv2.VideoCapture(video_to_process)
    # check video capture status
    if not captured_video.isOpened:
        print("Unable to open: " + video_to_process)
        exit(0)

    # instantiate background subtraction
    background_subtr_method = cv2.bgsegm.createBackgroundSubtractorGSOC()

    while True:
        # read video frames
        retval, frame = captured_video.read()
        # check whether the frames have been grabbed
        if not retval:
            cv2.imwrite( out_background_filename, background_img )
            break
        # resize video frames
        height, width = frame.shape[:2]
        frame = cv2.resize(frame, (width, height))
        # pass the frame to the background subtractor
        foreground_mask = background_subtr_method.apply(frame)
        # obtain the background without foreground mask
        background_img = background_subtr_method.getBackgroundImage()
        # show the current frame, foreground mask, subtracted result
        cv2.imshow("Initial Frames", frame)
        cv2.imshow("Foreground Masks", foreground_mask)
        cv2.imshow("Subtraction Result", background_img)

        keyboard = cv2.waitKey(10)
        if keyboard == 27:
            cv2.imwrite( out_background_filename, background_img )
            break


if __name__ == "__main__":
    outNameVideo = "CAM_100_14022022_1456.mpeg"
    out_background_filename = "cam100_plaza_armas_guadalajara.jpg"
    # start BS-pipeline
    get_opencv_result(outNameVideo, out_background_filename)
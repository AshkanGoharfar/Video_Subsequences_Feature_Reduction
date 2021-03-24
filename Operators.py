import cv2
import numpy as np
from _plotly_utils.colors.cmocean import amp


def reduce_feature(color_space, cam_or_video, change_col_mode):
    if cam_or_video == 'camera':
        cap = cv2.VideoCapture(0)
    elif cam_or_video == 'video':
        cap = cv2.VideoCapture('Input/v_BodyWeightSquats_g01_c03.avi')
    else:
        print('Wrong console command')
        return 0

    panel = np.zeros([100, 700, 3], np.uint8)
    cv2.namedWindow('panel')

    def nothing(x):
        pass

    cv2.createTrackbar('L to h', 'panel', 0, 179, nothing)  # 0
    cv2.createTrackbar('U to h', 'panel', 179, 179, nothing)  # 179

    cv2.createTrackbar('L to s', 'panel', 0, 255, nothing)  # 7
    cv2.createTrackbar('U to s', 'panel', 255, 255, nothing)  # 255

    cv2.createTrackbar('L to v', 'panel', 0, 255, nothing)  # 30
    cv2.createTrackbar('U to v', 'panel', 255, 255, nothing)  # 255

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    size = (frame_width, frame_height)

    # Below VideoWriter object will create
    # a frame of above defined The output
    result = cv2.VideoWriter(
        'Output/' + 'Output_Video' + '_' + str(color_space) + '_' + str(cam_or_video) + '_' + str(
            change_col_mode) + '.avi',
        cv2.VideoWriter_fourcc(*'MJPG'),
        10, size)
    return background_subtraction(cap, color_space, change_col_mode, cam_or_video, panel, result)


def skeletal_modelling(bg, panel):
    ret, bg = cv2.threshold(bg, 30, 255, 0)
    # Create an empty skeleton
    # size = np.size(bg)
    skel = np.zeros(bg.shape, np.uint8)

    # Get a Cross Shaped Kernel
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    while True:
        try:
            # Open the image
            open = cv2.morphologyEx(bg, cv2.MORPH_OPEN, element)
            # Substract open from the original image
            temp = cv2.subtract(bg, open)
            # Erode the original image and refine the skeleton
            eroded = cv2.erode(bg, element)
            skel = cv2.bitwise_or(skel, temp)
            bg = eroded.copy()
            # If there are no white pixels left ie.. the image has been completely eroded, quit the loop
            if cv2.countNonZero(bg) == 0:
                break
        except:
            break
    # Displaying the final skeleton
    cv2.imshow("Skeleton", skel)
    cv2.imshow('panel', panel)
    k = cv2.waitKey(30) & 0xFF
    return skel, k


def background_subtraction(cap, color_space, change_col_mode, cam_or_video, panel, result):
    all_frames = []
    if color_space == 'skeleton':
        thereshold = np.random.normal(0, 1, 1)
        # thereshold = np.random.random(1)[0]
        if thereshold > 0.5:
            color = cv2.COLOR_BGR2HLS
        else:
            color = cv2.COLOR_BGR2HSV
    while True:
        try:
            _, frame = cap.read()
            if color_space == 'hsv':
                hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            elif color_space == 'hls':
                hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
            elif change_col_mode == 'non-automatic':
                hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
            else:
                try:
                    hls = cv2.cvtColor(frame, color)
                except:
                    break

            if change_col_mode == 'auto' and cam_or_video == 'video':
                lower_green = np.array([0, 0, 35])
                upper_green = np.array([179, 255, 255])
            elif change_col_mode == 'auto' and cam_or_video == 'camera':
                lower_green = np.array([0, 7, 30])
                upper_green = np.array([179, 255, 255])
            elif change_col_mode == 'non-automatic':
                l_h = cv2.getTrackbarPos('L to h', 'panel')
                u_h = cv2.getTrackbarPos('U to h', 'panel')
                l_s = cv2.getTrackbarPos('L to s', 'panel')
                u_s = cv2.getTrackbarPos('U to s', 'panel')
                l_v = cv2.getTrackbarPos('L to v', 'panel')
                u_v = cv2.getTrackbarPos('U to v', 'panel')
                lower_green = np.array([l_h, l_s, l_v])
                upper_green = np.array([u_h, u_s, u_v])
        except:
            print('The video has finished')
            break
        try:
            mask = cv2.inRange(hls, lower_green, upper_green)
            # mask_inv = cv2.bitwise_not(mask)

            bg = cv2.bitwise_and(frame, frame, mask=mask)
            # fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            if color_space != 'skeleton':
                cv2.imshow('bg', bg)
                # cv2.imshow('fg', fg)
                cv2.imshow('panel', panel)
                k = cv2.waitKey(30) & 0xFF
                all_frames.append(bg)
            else:
                bg, k = skeletal_modelling(bg, panel)
                all_frames.append(bg)
            result.write(bg)
            if k == 27:
                break
        except:
            break
    cap.release()
    result.release()
    cv2.destroyAllWindows()
    return all_frames

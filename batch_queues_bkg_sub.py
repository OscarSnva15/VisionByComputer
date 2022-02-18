import os
import cv2
import time


from multiprocessing import Process, Queue, current_process, freeze_support

def recovery_video_files( path="." ):
    videos_to_processs = []
    for x in os.listdir(path):
        if x.endswith(".mpeg") and not os.path.isfile(x.replace("mpeg","png")):
            # Process only video file not previously processed
            videos_to_processs.append(x)

    print("*"*10)
    print("\n".join(videos_to_processs))
    print("*"*10)
    
    return videos_to_processs

#
# Function run by worker processes
#
def worker(input, output):
    for video in iter(input.get, 'STOP'):
        result = compute_video_background(video)
        output.put(result)
        output("  ")

def compute_video_background( video_to_process ):
    size_video =  os.path.getsize(video_to_process)
    print("initializing process {} for video {} with size {}".format(current_process().name, video_to_process,size_video) )

    tic = time.time()
    out_background_filename = video_to_process.replace("mpeg","png")

    # create VideoCapture object for further video processing
    captured_video = cv2.VideoCapture(video_to_process)
    # check video capture status
    if not captured_video.isOpened:
        print("Unable to open: " + video_to_process)
        return "%s says ERROR %s %s on generate %s".format(current_process().name, compute_video_background.__name__, video_to_process, out_background_filename)

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
    
    toc = time.time()

    return "{} finished video {} took %s seconds, size video {}".format(current_process().name,  video_to_process, out_background_filename, toc-tic)


def batch_background_processing( num_process = 4):

    print("batch_background_processing using {} process".format(num_process))

    videos_to_processs = recovery_video_files()

    # IF videos is empty THEN
    #    WAIT 2 horas
    # ELSE

    # Create queues
    task_queue = Queue()
    done_queue = Queue()

    # Submit tasks
    for video in videos_to_processs:
        task_queue.put(video)

    # Start worker processes
    for i in range(num_process):
        Process(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    print('display complete process:')
    for i in range(len(videos_to_processs)):
        print('\t', done_queue.get())

    # Tell child processes to stop
    for i in range(num_process):
        task_queue.put('STOP')

if __name__ == '__main__':
    freeze_support()

    NUMBER_OF_PROCESSES = 8

    batch_background_processing( NUMBER_OF_PROCESSES )

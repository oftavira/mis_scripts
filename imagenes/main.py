import os
import cv2

from natsort import natsorted

def create_video(input_folder, output_file, frame_delay = 0.5):
    
    if not os.path.exists(input_folder):
        print('No existe el directorio especificado')
        return
    
    image_file = [f for f in os.listdir(input_folder)]
    sorted_images = natsorted(image_file)
    first_image = cv2.imread(os.path.join(input_folder, sorted_images[0]))
    height, width, _ = first_image.shape

    video_writer = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 1/frame_delay, (width, height))

    for image_file in sorted_images:
        image_path = os.path.join(input_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)
    
    video_writer.release()
)
import ffmpy
import os

def convert_mp4_to_webm(input_file, output_file):
    ff = ffmpy.FFmpeg(
        inputs={input_file: None},
        outputs={output_file: None}
    )
    
    ff.run()

def convert_all_mp4_in_folder(source_folder, target_folder):
    os.makedirs(target_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        if filename.endswith('.mp4'):
            input_mp4 = os.path.join(source_folder, filename)
            
            output_webm = os.path.join(target_folder, f"{os.path.splitext(filename)[0]}.webm")
            
            convert_mp4_to_webm(input_mp4, output_webm)
            print(f"Конвертирован: {input_mp4} -> {output_webm}")

source_folder = './videos/'
target_folder = './processed_videos/'

convert_all_mp4_in_folder(source_folder, target_folder)
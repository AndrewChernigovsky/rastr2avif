import os 
from PIL import Image
import imageio
import pillow_avif

def convert_image(input_path, index, output_directory):
    index = index + 1
    with Image.open(input_path) as img:
        base_name = "filter-main"
        # base_name = os.path.splitext(os.path.basename(input_path))[0]

        webp_path = os.path.join(output_directory, f"{base_name}{index}@200x200.webp")
        img.save(webp_path, "WEBP")
        print(f"Сохранено: {webp_path}")

        duplicate_webp_path = os.path.join(output_directory, f"{base_name}{index}@1000x1000.webp")
        img.save(duplicate_webp_path)
        print(f"Создан дубликат: {duplicate_webp_path}")

        avif_path = os.path.join(output_directory, f"{base_name}{index}@200x200.avif")
        imageio.imwrite(avif_path, img)
        print(f"Сохранено: {avif_path}")

        duplicate_avif_path = os.path.join(output_directory, f"{base_name}{index}@1000x1000.avif")
        imageio.imwrite(duplicate_avif_path, img)
        print(f"Создан дубликат: {duplicate_avif_path}")


def convert_images_in_directory(directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    for index, filename in enumerate(os.listdir(directory)):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(directory, filename)
            convert_image(input_path, index, output_directory)

input_directory = './images/'
output_directory = './processed_images/'
convert_images_in_directory(input_directory, output_directory)
import os
import shutil
from PIL import Image

download_folder = r'C:/Users/PC/Downloads'

def convert_webp_to_png(file_path):
	image = Image.open(file_path)
	png_file_path = file_path.replace('.webp', '.png')
	image.save(png_file_path, 'PNG')
	os.remove(file_path)

def monitor_downloads():
	while True:
		for file in os.listdir(download_folder):
			file_path = os.path.join(download_folder, file)
			if file.endswith('.webp'):
				convert_webp_to_png(file_path)
				print(f'Converted {file} to PNG')

monitor_downloads()
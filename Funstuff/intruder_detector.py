import cv2
import os
import time
path = '/home/samar/Desktop/Intruder'


def rmrf():
	for the_file in os.listdir(path):
		file_path = os.path.join(path, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path):shutil.rmtree(file_path)
		except Exception as e:
			print(e)


def main():
	cam = cv2.VideoCapture(0)
	while True:
		ret_val, img = cam.read()
		img = cv2.flip(img, 1)
		p,d,f = next(os.walk(path))
		count = len(f)
		if count == 3:
			rmrf()
			count = 0
			break
		img_name =  "Img_"+str(count)+".jpg"
		cv2.imwrite(os.path.join(path , img_name), img)
		print(img_name)
		time.sleep(5)

if __name__ == '__main__':
	main()

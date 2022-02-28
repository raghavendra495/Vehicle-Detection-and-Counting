import os
import subprocess

# Run detections on all files in the inputVideos directory
i=0
for fileName in os.listdir("inputVideos/"):
	i=i+1
	if i!=2:
		continue
	lastDotIndex = fileName.rfind(".")
	# print(fileName[:lastDotIndex])
	# print("python3 yolo_video.py --input inputVideos/" + fileName + " --output outputVideos/" + \
	# 	fileName[:lastDotIndex] + ".avi --yolo yolo-coco --use-gpu 1")
	cmd = "python3 yolo_video.py --input inputVideos/" + fileName + " --output outputVideos/" + \
		fileName[:lastDotIndex] + ".avi --yolo yolo-coco --use-gpu 1"
	print("Running command:\n" + cmd)
	subprocess.run(cmd, shell=True)


# cmd = "python3 yolo_video.py --input inputVideos/" + fileName + " --output outputVideos/" + \
# 		fileName[:lastDotIndex] + ".avi --yolo yolo-coco --use-gpu 1"
# print("Running command:\n" + cmd)
# subprocess.run(cmd, shell=True)
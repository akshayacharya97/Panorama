import imutils
import cv2
import glob

input_path = "/Users/akshayacharya/Desktop/Panorama/Raw Data/riverside/*.jpg"

# input and sort the images
list_images = glob.glob(input_path)
list_sorted = sorted(list_images)
print(list_sorted)

# output path definition
output_path = "/Users/akshayacharya/Desktop/Panorama/Final Panorama/compatpanoexample1.jpg"

# initialize empty list and fill all images
images = []
for image in list_sorted:
    image1 = cv2.imread(image)
    image1 = cv2.resize(image1, (720, 480))
    images.append(image1)

print("Read the images")
# this is the final list to stitch
final = [images[0]]
flag = True
print(len(images))

stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()

i = 0
while(i < len(images)-1):
    (status, stitched) = stitcher.stitch([images[i], images[i+1]])
    if status == 0:
        final.append(images[i+1])
        i = i+1
        print(f"Succesfully can stitch {i} to {i+1}")
        #print(len(final))
        continue
    if status != 0:
        print(f"Succesfully could not stitch {i} to {i + 1}")
        for j in range(i+2, len(images)):
            print(f"now trying {i} to {j}")
            (status, stitchedd) = stitcher.stitch([images[i], images[j]])
            if status == 0:
                print(f"Succesfully managed to stitch {i} to {j}")
                final.append(images[j])
                i=j
                break
            if status != 0:
                print(f"Oops could not stitch {i} to {j}")
                print(f"Will now see compatibility between {i} and {j+1}")

            continue

        i += 1
    continue

print(len(final))
print("Now stitching the final")
(status, stitches) = stitcher.stitch(final)
print(status)

# save it if succesfully stitched
if status == 0:
    # write the output stitched image to disk
    cv2.imwrite(output_path, stitches)
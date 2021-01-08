# Panorama

The compatpano.py is the program where it takes the images and checks comptability between subsequent frames and adds the good frames to a final list and stitches them.

Ex: 10 frames
1-2 -> If good, then adds 1 and 2 to final
2-3-> If good, adds 3 to final. Chucks 3 if not good.



The finalpano.py program checks compatibility between frames and keeps stitching if good.

Ex: 10 frames
1-2 -> If good, stitch and then check that new image with next frame.
(12)-3 -> If good, stitches 12 to 3 to give (123)
(123)-4 -> If good, stitches (123) to 4, if not good, checks (123) with 5 and so on. 

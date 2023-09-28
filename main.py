# # we use the import cv2 statement to bring in a library called "OpenCV" (Open Source Computer Vision Library) into our code.
# # Access to Image and Video Functions: OpenCV provides a wide range of functions and tools to work with images and videos.
# # It allows you to read, write, manipulate, and process images and video streams.

# import cv2
#
# #        cv2.imread used for reading or processing image
# # Reading Images: It reads an image file (such as a JPEG, PNG, or BMP) from your computer's storage into a NumPy array. Once loaded,
# # you can perform various operations on the image using OpenCV functions.
# #
# # Image Processing: After reading an image, you can apply a wide range of image processing operations, such as resizing, cropping, rotating,
# # filtering, and more, to modify the appearance or content of the image.

# image =  cv2.imread("RIDER.png", cv2.IMREAD_UNCHANGED)
#
#
# #  cv2.imshow -- Displaying Images and Video Frames: It shows images and video frames within a graphical window.
# # Real-time Visualization: Useful for displaying live video streams or intermediate results during image processing.
# # Debugging and Testing: Helps developers inspect and validate computer vision and image processing algorithms visually.

# cv2.imshow("title", image)
#
#
# #  cv2 -- Control Image Display: It sets a delay to control how long an image or video frame is displayed in a window created with cv2.imshow.
# #
# # User Interaction: Allows you to create interactive applications where users can control
# # when to proceed to the next part of the code by pressing specific keys during the wait period.

# cv2.waitKey(0)


# ---------------------------------------------------------------------------------------------------------


# new code for the same project
# have install cv2 package it gives output very smartly in JPEG
import cv2


# configurable parameters
source = "RIDER.png"
destination = "newImage.jpeg"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

# persent by which the image is resized

# calculate the 50 percent original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitkey(0)








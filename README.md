# How to use
When you run the application you are asked to fill in 4 variables. Here is an explanation for each one of them
- [Choosing a Template Image](#choosing-a-template-image)
- [Choosing a Brawl VOD](#choosing-a-brawl-vod)
- [Entering the Minimum Accuracy](#entering-the-minimum-accuracy)
- [Entering the Frame Skip Value](#entering-the-frame-skip-value)

<br>

# Choosing a Template Image
This is the most tricky part but don't worry.
## What is a Template Image?
A template image is an image the application will try to fit in each frame of the video. The application will output an accuracy of how well the template image fits into the video frame, and then goes onto the next frame. By providing the template image, you are telling the application what to look for in the video. If i give this image,

![template image 1v1 ranked season 32e](https://github.com/CrossyChainsaw/brawl-template-matcher/assets/74303221/6ae87203-0f0b-4c69-90cc-19ef1b999758)

the application will take a screenshot of every frame it sees with this image inside of it. If you have a bad image, the application will not work properly and output low accuracies.

![image](https://github.com/CrossyChainsaw/brawl-template-matcher/assets/74303221/531a5915-859f-4b96-a45e-1a9cafbc3781)


## How to generate a Template Image?
To generate a Template Image you want to make the application generate frames for you. After, you crop the screenshot to whatever you want to use as a template image. Here is an example.

1. Choose a random template image (doesn't matter we will put minimum accuracy at 0)
2. Choose the .mp4 file which of you want to render frames.
3. Put Minimum Accuracy at 0 (This means the application will try to match the template image and render the frame if the accuracy is at least better than 0.0. But this is always the case since the accuracy can never be lower than 0.0, so it will render all the frames).
4. You can put the frame skip at any value. Safest move is to put it at 1, which will result in all the frames getting rendered. You can also put it at 2 or 3 it it isnt frame perfect or even values like 250.
5. The application will render frames into the results folder. if you see your desired frame you can stop the application and open the image in paint, crop it so you have the template image, and save as .png.

<br>

# Choosing a Brawl VOD
Just choose any .mp4 file with gameplay. Based of the template image you can decide which frames you want to extract.

<br>

# Entering the Minimum Accuracy
The accuracy means how well the template image fits in the video frame. If you have a good template image you can put this at 0.95. If you don't have a good image you can try 0.85. If you don't seem to get any values above 0.6 accuracy, your template image is most likely bad. Read [Choosing a Template Image]() to generate a good template image.

<br>

# Entering the Frame Skip Value
When this is set to 1, the application will check each frame of the video and try to match the template image in the video, outputting an accuracy based of how well the template image fits in the video frame. Usually (If you are extracting matchmaking frames from ranked gameplay) you want to put this value around 250. Having a value of 250 makes sure you won't get duplicate frames of the same matchmaking frame / same opponent. 

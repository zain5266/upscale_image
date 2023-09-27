# upscale_image

To run it on colab:
open the colab
1)  run "!git clone https://github.com/zain5266/upscale_image.git"
2)  run "!apt-get install libnvidia-gl-525" 
3)  run "!sudo apt install -y vulkan-tools"
4)  Change the current working directory:
    import os
    os.chdir("/content/upscale_image") 
5)  Import upscale_image function:
    from image_upscale import upscale_image 
6)  call the functions with required parameters:
    parameters are : 
    img_path: input image path ("/content/example.jpg")
    output_path: output image path ("/content/ouput.jpg")
    model_name: name of the models -> choose from available models (e.g "RealESRGAN_General_WDN_x4_v3")
    scale: select a scale like 1 to 4 
Example run:
img_path="/content/example.jpg"
output_path="/content/ouput.jpg"
model_name: "RealESRGAN_General_WDN_x4_v3"
scale: 4
upscale_image(img_path,output_path,model_name,scale)

import subprocess

def process_upscale(input_path, output_path, model, scale=4):
    # Path to the realesrgan-ncnn-vulkan executable (update this to the correct path)
    realesrgan_executable = '/bin/linux-amd64'

    # Build the command to upscale the image(s)
    upscale_command = [
        realesrgan_executable,
        '-i', input_path,
        '-o', output_path,
        '-s', str(scale),
        '-m', 'models',  # Update this with the path to your model folder
        '-n', model,
        '-g', '0', 
        '-f', 'png',  # Replace with your desired output format
        '-x',  # Enable tta mode if needed
        '-v',   # Verbose output
    ]

    # Run the upscale command
    try:
        subprocess.run(upscale_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error upscaling image: {e.stderr.decode('utf-8')}")
        return None
    return output_path

def upscale_image(img_path,output_path,model_name,scale):
    # Provide the input image path, output image path, model, and scale
    scale = 4  # Adjust the scale as needed
    result_path = process_upscale(img_path, output_path, model_name, scale)
    if result_path:
        print(f"Upscaled image saved at: {result_path}")
        return result_path
    return None
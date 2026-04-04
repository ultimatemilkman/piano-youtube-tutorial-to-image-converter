from PIL import Image
import os

# -------------------------------
# Settings
# -------------------------------
gif_file = "CHANGE_THIS_YOUR_GIF_FILE_NAME_GOES_HERE.gif"  # path to your 1-pixel-tall GIF
max_height = 9000           # max height per output image

# -------------------------------
# Open GIF
# -------------------------------
gif = Image.open(gif_file)
frames = []
image_count = 1 # YOU MIGHT NEED TO CHANGE THIS OCCASIONALLY TO AVOID MULTIPLE IMAGE FILES WITH THE SAME FILE NAME IN THE SAME FOLDER

try:
    while True:
        frame = gif.convert("RGBA")  # ensure consistent format
        frames.append(frame)

        # Check if current stack exceeds max_height
        if len(frames) >= max_height:
            # Flip frames vertically before stacking
            frames.reverse()

            tall_image = Image.new("RGBA", (frame.width, len(frames)))
            for i, f in enumerate(frames):
                tall_image.paste(f, (0, i))
            output_file = f"piano_scroll_{image_count}.png"
            tall_image.save(output_file)
            print(f"Saved {output_file} (height {tall_image.height})")
            image_count += 1
            frames = []

        gif.seek(gif.tell() + 1)

except EOFError:
    # End of GIF
    if frames:
        frames.reverse()  # flip vertically
        tall_image = Image.new("RGBA", (frame.width, len(frames)))
        for i, f in enumerate(frames):
            tall_image.paste(f, (0, i))
        output_file = f"piano_scroll_{image_count}.png"
        tall_image.save(output_file)
        print(f"Saved {output_file} (height {tall_image.height})")

print("Done!")
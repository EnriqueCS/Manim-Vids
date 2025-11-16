import os
import subprocess
import re
import shutil

SCENE_DIR = "./"
DST_PATH = "./currentVideo.mp4"

# Regex to match files like _<#vid><name>_<rest>.py
pattern = re.compile(r'^_(\d+)([a-z_]+)\.py$')

# Get all matching files with their vid number
files = []
for f in os.listdir(SCENE_DIR):
    match = pattern.match(f)
    if match:
        vid_number = int(match.group(1))  # supports 0
        files.append((vid_number, f))

if not files:
    print("No matching files found.")
    exit()

# Sort by vid number
files.sort(key=lambda x: x[0])
sorted_files = [f for _, f in files]

# Show options
print("Select a file to run (0-based), or 's' to stitch all videos via Manim:")
for i, f in enumerate(sorted_files):
    print(f"{i}: {f}")
print("s: Stitch all videos together")

choice = input(f"Enter a number (0-{len(sorted_files)-1}) or 's': ")

def get_class_name(filename):
    fname_no_py = filename.replace(".py", "")
    name_part_raw = re.sub(r'^_\d+', '', fname_no_py)
    return ''.join(part.capitalize() for part in name_part_raw.split('_')), fname_no_py

if choice.lower() == "s":
    video_files = []

    for f in sorted_files:
        class_name, fname_no_py = get_class_name(f)
        manim_cmd = ["manim", "-ql", f, class_name]
        print(f"Running: {' '.join(manim_cmd)}")
        subprocess.run(manim_cmd, check=True)

        # Path of the generated video
        video_path = f"./media/videos/{fname_no_py}/480p15/{class_name}.mp4"
        if not os.path.exists(video_path):
            print(f"Video not found at {video_path}, skipping.")
            continue
        video_files.append(video_path)

    if not video_files:
        print("No videos were generated, nothing to stitch.")
        exit()

    # Create a temporary text file for FFmpeg concatenation
    list_file = "videos_to_concat.txt"
    with open(list_file, "w") as f:
        for vf in video_files:
            f.write(f"file '{os.path.abspath(vf)}'\n")

    # Use FFmpeg to concatenate
    ffmpeg_cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", DST_PATH]
    print(f"Stitching videos into {DST_PATH}")
    subprocess.run(ffmpeg_cmd, check=True)

    os.remove(list_file)
    print(f"Stitched video saved to {DST_PATH}")

else:
    try:
        index = int(choice)
        if not (0 <= index < len(sorted_files)):
            raise ValueError
    except ValueError:
        print("Invalid choice.")
        exit()

    selected_file = sorted_files[index]
    class_name, fname_no_py = get_class_name(selected_file)

    manim_cmd = ["manim", "-ql", selected_file, class_name]
    print(f"Running: {' '.join(manim_cmd)}")
    subprocess.run(manim_cmd, check=True)

    src_path = f"./media/videos/{fname_no_py}/480p15/{class_name}.mp4"

    if os.path.exists(src_path):
        shutil.copy(src_path, DST_PATH)
        print(f"Video copied to {DST_PATH}")
    else:
        print(f"Video not found at {src_path}")

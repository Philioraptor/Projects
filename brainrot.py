import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips  # Import specific modules from moviepy
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip  # Explicitly import CompositeVideoClip
from moviepy.video.VideoClip import TextClip, ImageClip  # Explicitly import TextClip and ImageClip
from moviepy.video.fx.all import crop, resize # Import specific modules from moviepy.video.fx.all
from moviepy.audio.io.AudioFileClip import AudioFileClip  # Import AudioFileClip for audio handling

# Brainrot folders ka path
VIDEO_FOLDER = "backgrounds/"
AUDIO_FOLDER = "sounds/"
OUTPUT_FOLDER = "output/"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Random background selection
background_videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.avi', '.mov'))]
background_clip = VideoFileClip(os.path.join(VIDEO_FOLDER, random.choice(background_videos)))

# User Input Text
text_content = "Newton ne dekha apple gir raha hai, aur tu physics ke marks girte dekh raha hai. 💀📖"

# Text Overlay
text_clip = TextClip(text_content, fontsize=70, color='white', font="Arial-Bold", stroke_color="black", stroke_width=3)
text_clip = text_clip.set_position(("center", "bottom")).set_duration(background_clip.duration)

# Sound Effects (Vine Boom + Sigma Sound)
sound_effects = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith(('.mp3', '.wav'))]
if sound_effects:
    selected_sound = AudioFileClip(os.path.join(AUDIO_FOLDER, random.choice(sound_effects)))
    background_clip = background_clip.set_audio(selected_sound)

# Final Compilation
final_clip = CompositeVideoClip([background_clip, text_clip])
output_path = os.path.join(OUTPUT_FOLDER, "brainrot_output.mp4")
final_clip.write_videofile(output_path, codec="libx264", fps=30)

print(f"✅ Brainrot video saved at: {output_path}")
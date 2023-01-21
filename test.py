from moviepy.editor import *
# clip1 = VideoFileClip("1-15.mp4")
clip2 = VideoFileClip("1-16.mp4")
# clip3 = VideoFileClip("1-17.mp4")
clip4 = VideoFileClip("1-18.mp4")
clip5 = VideoFileClip("1-20.mp4")

final_clip = concatenate_videoclips([clip2,clip4,clip5])

final_clip.write_videofile("Montage.mp4")

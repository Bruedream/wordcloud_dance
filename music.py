import moviepy.editor as mpy
from moviepy.audio.io.AudioFileClip import AudioFileClip

# 读取词云视频
my_clip = mpy.VideoFileClip('E:/PycharmProjects/Dance/result.mp4')
# 截取背景音乐
# audio_backgroung = mpy.AudioFileClip('song.mp4').subclip(17, 44)
# audio_backgroung.write_audiofile('YesOK.mp3')
# 视频中插入音频
audio_clip = AudioFileClip('E:/PycharmProjects/Dance/YesOK.mp3')
final_clip = my_clip.set_audio(audio_clip)
# 保存为最终的视频
final_clip.write_videofile('E:/PycharmProjects/Dance/final_video.mp4')
from moviepy.editor import VideoFileClip,AudioFileClip
# 1. 读取视频文件
video = VideoFileClip('视频.mp4')

# 2. 读取音频文件
audio = AudioFileClip('音频.mp3')

# 3. 将音频设置给视频（这会覆盖原视频的声音）
final_video = video.set_audio(audio)

# 4. 保存合成后的新视频
final_video.write_videofile('完整视频.mp4')  #123
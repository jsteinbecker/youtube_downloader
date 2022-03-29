from pytube import YouTube
import os

doc_todo = open ('links.txt','r').readlines()
doc_done = open ('completed','r').readlines()

for lk in doc_todo:
   if lk in doc_done:
      pass
   else:
      yt = YouTube (lk)
      writenl = open ('completed','a').writelines("\n")
      video = yt.streams.filter(only_audio=True).first()

      out_file = video.download(output_path="Output")

      base, ext = os.path.splitext(out_file)
      new_file = base + '.mp3'
      os.rename(out_file, new_file)
      write_done = open ('completed','a').writelines(lk)
      
      
print("SCRIPT COMPLETE")

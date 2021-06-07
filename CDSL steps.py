from scene_detective import scene_detective
from subber import srt2sub, id_prop, submarine, cutbyid, id_ital, sublist_flatten
from timecoder import get_fr
from CDSL_A import cdsl_a
import time
import winsound

video_path = 'C:/Users/lucaj/Desktop/Chairap/Initials SG/Video/Initials SG Ref 2019_09_30.mp4'
scene_path = 'C:/Users/lucaj/Desktop/Chairap/Initials SG/SRT Final/01 ISG-takebytake.srt'
dialogue_path = 'C:/Users/lucaj/Desktop/Chairap/Initials SG/SRT Final/02 ISG-dialogosCnombre-final.srt'
caption_path = 'C:/Users/lucaj/Desktop/Chairap/Initials SG/SRT Final/03 ISG-captions.srt'
title_path = 'C:/Users/lucaj/Desktop/Chairap/Initials SG/SRT Final/04 Initials SG English Full Subtitles.srt'

print('Building awesome excel, please wait...')
scene_det = scene_detective(video_path, duration=10)
fr = get_fr(scene_det)

sclist = srt2sub(scene_path)
dialogue_list = srt2sub(dialogue_path)
caption_list = srt2sub(caption_path)
title_list = srt2sub(title_path)

dialogue_list = id_prop(dialogue_list, 'dialogue')
caption_list = id_prop(caption_list, 'caption')
title_list = id_prop(title_list, 'title')

sublist = submarine(dialogue_list, caption_list, title_list)
sublist = cutbyid(sublist, ['dialogue', 50], ['caption', 50], ['title', 50])
sublist = sublist_flatten(sublist)
sublist = id_ital(sublist)

start = time.time()
cdsl_a(sclist, sublist, fr, 'Initials S.G.')
end = time.time()
print('Done!')
print('It took ' + str(round(end-start))+'s!')
winsound.PlaySound('MC_Fanfare_Item.wav', winsound.SND_FILENAME)

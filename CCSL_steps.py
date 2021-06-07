from scene_detective import scene_detective
from subber import srt2sub, id_prop, submarine, cutbyid, id_ital, sublist_flatten
from timecoder import get_fr
from CCSL_A import ccsl_a
import time
import winsound

video_path = 'C:/Users/lucaj/Desktop/Chairap/_Works/My Boyfriends Meds/_raw/MBFM SC New Edit para SUBT @24 .mp4'
scene_path = 'C:/Users/lucaj/Desktop/Chairap/_Works/My Boyfriends Meds/SRT Finales/MBM-continuity-final20dic.srt'
sub_path = 'C:/Users/lucaj/Desktop/Chairap/_Works/My Boyfriends Meds/SRT Finales/MBM-subsEN-rollocontinuo-rev20dic.srt'

print('Processing video...')
scene_det = scene_detective(video_path, duration=10)
fr = get_fr(scene_det)

print('Processing subtitles...')
sc_list = srt2sub(scene_path)
sub_list = srt2sub(sub_path)

sc_list = id_prop(sc_list, 'scene')
sub_list = id_prop(sub_list, 'sub')

sublist = submarine(sc_list, sub_list)
sublist = cutbyid(sublist, ['scene', 45], ['sub', 50])
sublist = sublist_flatten(sublist)
sublist = id_ital(sublist)

print('Building awesome excel, please wait...')
start = time.time()
ccsl_a(sublist, fr, "My Boyfriend's Meds")
end = time.time()
tm = round((end-start) / 60)
ts = round((end-start) % 60)
print('Done!')
print('It took ' + str(tm)+'m and ' + str(ts) + 's!')
winsound.PlaySound('MC_Fanfare_Item.wav', winsound.SND_FILENAME)

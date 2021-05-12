#!/usr/bin/env python

id_file = 'id.txt'
in_file  = 'test.txt'
out_file = 'text.txt'

txt_dict = dict()
with open(in_file, 'r') as fi:
    for line in fi:
        txt_id, txt = line.strip().split('|')
        txt_dict[txt_id] = txt

#emo_dict = {"10":"中性", "21":"惊讶", "22":"高兴", "23":"悲伤", "24":"愤怒", "25":"厌恶", "26":"恐惧"}
emo_dict = {"21":"惊讶", "22":"高兴", "23":"悲伤", "24":"愤怒", "25":"厌恶", "26":"恐惧"}
with open(id_file, 'r') as fi, \
     open(out_file, 'w') as fo:
    for line in fi:
        txt_id = line.strip()
        for i in emo_dict:
            fo.write("{}-{}|({}){}\n".format(txt_id, i, emo_dict[i], txt_dict[txt_id]))

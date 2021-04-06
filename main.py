from tqdm import tqdm
import os
import audio
import saveOutput as sv
import STT


def STT4all(cfile='config.txt', sfolder='source', efolder='export'):
    STT_file = STT.STT(cfile)
    for file in tqdm(os.listdir(sfolder), unit='file'):
        filepath = sfolder + '/' + file
        au = audio.Audio(filepath, STT_file.buffer)

        if not au.audio: continue  # If file does not supported, pass them
        f1, f2 = au.splitList()
        sv_file = sv.SaveSTT(file, efolder=efolder)

        for i in tqdm(range(au.splitSize), leave=False, unit='part'):
            t1, t2 = f1[i], f2[i]
            au.svTemp(t1, t2)
            message = STT_file.STT_message('.temp.wav')
            sv_file.save(message)
            au.rmTemp()

if __name__ == '__main__':
    STT4all()
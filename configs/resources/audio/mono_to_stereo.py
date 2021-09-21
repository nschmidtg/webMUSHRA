import torchaudio
import torch
import os

files = []
for path, subdirs, files in os.walk('.'): 
    for name in files:
        if '.wav' in name:
            file_name = os.path.join(path, name)
            print(file_name)
            x, sf = torchaudio.load(file_name)
            if x.shape[0] == 1:
                x = torch.cat([x, x])
                torchaudio.save(file_name, x, sample_rate=sf)
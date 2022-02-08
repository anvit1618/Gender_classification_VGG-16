import os
import random
import glob
import shutil

for c in random.sample(glob.glob('????0*'), 1):
    shutil.move(c, 'train/male' )

for c in random.sample(glob.glob('????1*'), 1):
    shutil.move(c, 'train/female' )

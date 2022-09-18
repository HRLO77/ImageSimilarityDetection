import glob
import os

for i in glob.glob('./test/*.npz'):
    os.remove(i)
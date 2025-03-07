
import os
def cp(fp):
    print("Read access:", os.access(fp, os.R_OK))
    print("Write access:", os.access(fp, os.W_OK))
cp("text.txt")
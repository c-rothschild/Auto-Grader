import subprocess
import os
import glob

directory = 'Day_1_Submissions'

def run_file(f):
    print(f + " is running")
    subprocess.run(["python", f])

for filename in sorted(glob.iglob(f'{directory}/*')):
    run_file(filename)

import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import glob
import time

"""
this code automates the grading process for only the sample files included in the sample_assignments directory
simulated inputs can only be changed by editing the code directly
"""

directory = 'sample_assignments'

def run_file(f, userin):
    print(f[f.index("/") + 1:] + " is running")
    proc = subprocess.Popen(
        ["python", f], stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True
    )
    grep_stdout = proc.communicate(input=userin)[0]
    print('\n'.join(grep_stdout.splitlines()))

def main():
    for filename in sorted(glob.iglob(f'{directory}/*.py')):
        print()
        if 'windchill' in filename.lower():
            run_file(filename, '27.1\n8')
        elif 'race' in filename.lower():
            run_file(filename, '0.73,0.11\n1.333,2.98\n0,0')
        elif 'overlap' in filename.lower():
            run_file(filename, 'cp115,cp116,cp122,cp222\ncp116,cp222,cp274')
        else:
            print(filename + "did not run")
        input()
main()

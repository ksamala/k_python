import subprocess
proc = subprocess.run(['ls', '-l'])

proc = subprocess.run(
        ['ls', '-lrth'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
 )
import subprocess
proc = subprocess.run(['ls', '-l'])

proc = subprocess.run(
        ['ls', '-l'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
 )
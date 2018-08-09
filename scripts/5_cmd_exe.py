Execute a command on a shell remotely

import subprocess
proc = subprocess.run(['ssh', 'root@10.0.0.190'])

proc = subprocess.run(
        ['ls', '-lrth'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
 )

import subprocess

def my_ping(arg):
  process = subprocess.Popen(['ping','-c','5',arg],
                       stdout = subprocess.PIPE,
                       stderr = subprocess.PIPE)

  (stdoutdata, stderrdata) = process.communicate()
  return (stdoutdata, stderrdata)

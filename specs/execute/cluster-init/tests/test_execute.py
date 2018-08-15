import unittest
import subprocess

    
class TestExecute(unittest.TestCase):

    def test_simple(self):
        p = subprocess.Popen(['/opt/pbs/bin/qstat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        
        self.assertEqual(0, p.returncode, msg="Call to qstat failed with Stderr: %s\nStdout%s"
                         % (stderr, stdout))
        

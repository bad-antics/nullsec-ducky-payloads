import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_ducky_payloads.core import DuckyScriptBuilder,PayloadLibrary

class TestDucky(unittest.TestCase):
    def test_build(self):
        d=DuckyScriptBuilder()
        s=d.build_script(["STRING hello","ENTER"])
        self.assertIn("STRING hello",s)
    def test_reverse(self):
        d=DuckyScriptBuilder()
        s=d.reverse_shell_payload("linux","10.0.0.1",4444)
        self.assertIn("10.0.0.1",s)

class TestLibrary(unittest.TestCase):
    def test_list(self):
        l=PayloadLibrary()
        self.assertIn("recon",l.list_payloads())
    def test_count(self):
        l=PayloadLibrary()
        self.assertGreater(l.count(),10)

if __name__=="__main__": unittest.main()

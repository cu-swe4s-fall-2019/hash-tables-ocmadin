import unittest
import hash_tables as ht
import hash_functions as hf

class TestLinearProbe(unittest.TestCase):
    def test_input_params(self):
        self.assertRaises(TypeError,ht.LinearProbe,None,hf.h_ascii)
        self.assertRaises(TypeError,ht.LinearProbe,10,None)
        self.assertRaises(TypeError,ht.LinearProbe,10.0,hf.h_ascii)
        self.assertRaises(TypeError,ht.LinearProbe,[1,1,1],hf.h_ascii)
        self.assertRaises(TypeError,ht.LinearProbe,'tct',hf.h_ascii)
        
    def test_add_function(self):
        test = ht.LinearProbe(50,hf.h_ascii)
        test.add('text','value')
        self.assertEqual(test.T[3][1],'value')

    def test_search_function(self):
        test = ht.LinearProbe(50,hf.h_ascii)
        test.add('text','value')
        self.assertEqual(test.search('text'),'value')
        
    def test_no_overwrite(self):
        test = ht.LinearProbe(50,hf.h_ascii)
        test.add('text','value')
        test.add('text','newvalue')
        self.assertEqual(test.T[3][1],'value')

    def test_search_bad_value(self):
        test = ht.LinearProbe(50,hf.h_ascii)
        test.add('text','value')
        self.assertEqual(test.search('nothere'),None)
    
class TestChainedHash(unittest.TestCase):
    def test_input_params(self):
        self.assertRaises(TypeError,ht.ChainedHash,None,hf.h_ascii)
        self.assertRaises(TypeError,ht.ChainedHash,10,None)
        self.assertRaises(TypeError,ht.ChainedHash,10.0,hf.h_ascii)
        self.assertRaises(TypeError,ht.ChainedHash,[1,1,1],hf.h_ascii)
        self.assertRaises(TypeError,ht.ChainedHash,'tct',hf.h_ascii)
        
import unittest
import hash_functions as hf

class testHASCII(unittest.TestCase):
    def test_no_input_key(self):
        self.assertRaises(TypeError,hf.h_ascii,None,100)
    def test_wrong_input_type_key(self):
        self.assertRaises(TypeError,hf.h_ascii,1,100)
        self.assertRaises(TypeError,hf.h_ascii,[10,10,10],100)
        self.assertRaises(TypeError,hf.h_ascii,{},100)
        
    def test_no_input_N(self):
        self.assertRaises(TypeError,hf.h_ascii,'text',None)
    def test_wrong_input_type_N(self):
        self.assertRaises(TypeError,hf.h_ascii,'text','text')
        self.assertRaises(TypeError,hf.h_ascii,'text',['text','text','text'])
        self.assertRaises(TypeError,hf.h_ascii,'text',{})
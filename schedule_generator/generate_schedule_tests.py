#! /usr/local/bin/python3

import unittest
from mock import *
import datetime
import time
from generate_schedule import current_semester

mes = 11

mock_time = Mock()
mock_time.return_value = time.mktime(datetime.datetime(2011, 1, 21).timetuple())

target = datetime.datetime(2009, 1, 1)
with patch.object(datetime, 'datetime', Mock(wraps=datetime.datetime)) as patched:
    patched.now.return_value = target

 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass

    @patch('current_month', 8)
    def test_segundo_semestre(self):
        self.assertEqual( current_semester(), 2)
    
    @patch('current_month', 1)
    def test_primeiro_semestre(self):
        mes = 1
        self.assertEqual( current_semester(), 1)
 
if __name__ == '__main__':
    unittest.main()

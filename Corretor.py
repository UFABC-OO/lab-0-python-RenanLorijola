from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch
import OlaMundo

class Test(TestCase):
    def test_print(self):
        with patch('sys.stdout', new = StringIO()) as fake_out:
            OlaMundo.main()
            self.assertEqual(fake_out.getvalue(), "Sou UFABC!\n")
            
if __name__ == '__main__':
    main()
import unittest
import ecosysteme as e
import animaux as a

class TestAnimal(unittest.TestCase):
    def test_var(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        f = a.Animal(10, 15, eco)
        self.assertEqual(f._max, 20)
        self.assertEqual(f.coords, (10, 15))
        self.assertTrue(f.sante<=20 and f.sante>=10)
        
    def test_type(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        f = a.Animal(10, 15, eco)
        self.assertIsInstance(f, a.Animal)
        
    def test_cage(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        f1 = a.Animal(-10, 15, eco)
        f2 = a.Animal(-10, -15, eco)
        f3 = a.Animal(50, 15, eco)
        f4 = a.Animal(-2, 35, eco)
        self.assertEqual(f1.coords, (0, 15))
        self.assertEqual(f2.coords, (0, 0))
        self.assertEqual(f3.coords, (41, 15))
        self.assertEqual(f4.coords, (0, 24))
        f1.coords = (16, 64)
        self.assertEqual(f1.coords, (16, 24))
        
    def test_coords(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        c = a.Cigale(10, 15, eco)
        f = a.Fourmi(10, 15, eco)
        self.assertEqual(c.coords, f.coords)
        self.assertIsNot(c.coords, f.coords)
        self.assertIs(c.coords, c.coords)
        ac = c.coords
        c.coords = c.coords
        self.assertEqual(c.coords, ac)
        self.assertIsNot(c.coords, ac)
        ac = c._Animal__coords
        c._Animal__coords = ac
        self.assertIs(c._Animal__coords, ac)
       
class TestCigale(unittest.TestCase):
    
    def test_var(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        c = a.Cigale(10, 15, eco)
        self.assertEqual(c._max, 20)
        self.assertEqual(c.coords, (10, 15))
        self.assertTrue(c.sante<=20 and c.sante>=10)
    def test_type(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        c = a.Cigale(10, 15, eco)
        self.assertIsInstance(c, a.Cigale)
        self.assertIsInstance(c, a.Animal)
        an = a.Animal(15,10,eco)
        self.assertNotIsInstance(an, a.Cigale)
        f = a.Fourmi(12,12,eco)
        self.assertNotIsInstance(f, a.Cigale)
    def test_cage(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        c1 = a.Cigale(-10, 15, eco)
        c2 = a.Cigale(-10, -15, eco)
        c3 = a.Cigale(50, 15, eco)
        c4 = a.Cigale(-2, 35, eco)
        self.assertEqual(c1.coords, (0, 15))
        self.assertEqual(c2.coords, (0, 0))
        self.assertEqual(c3.coords, (41, 15))
        self.assertEqual(c4.coords, (0, 24))
        c1.coords = (16, 64)
        self.assertEqual(c1.coords, (16, 24))
   
class TestEcosysteme(unittest.TestCase):
    def test_type(self):
        eco = e.Ecosysteme(0, 1, 42, 25)
        self.assertIsInstance(eco, list)

if __name__ == '__main__':
    unittest.main()

import Laboratorio
import unittest

class TestLaboratorio(unittest.TestCase):

    '''Definimos las pruebas para cada funcion'''

    def test_suma(self): #(-2,7.2)
        resultado = laboratorio.sumacplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (-2,7.2))
        self.assertAlmostEqual(resultado, (8,7.2))
    
    def test_resta(self): #(8,-3.2)
        resultado = laboratorio.restacplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (8,-3.2))
        self.assertAlmostEqual(resultado, (5,6.2))

    def test_multiplicacion(self): #(-25.4,5.6)
        resultado = laboratorio.multcplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (-25.5,10.444443))
        self.assertAlmostEqual(resultado, (-25.4,5.6))

    def test_division(self): #(-2.254901961, -12.54901961)
        resultado = laboratorio.divcplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (-2.254901961, -12.54901961))
        self.assertAlmostEqual(resultado, (-2.2549,-12.5490))

    def test_mod(self):
        resultado = laboratorio.modcplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (8,7.2))
        self.assertAlmostEqual(resultado, (8,7.2))

    def test_conjugado(self): #(3, -2)
        resultado = laboratorio.conjugadocplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (3,-2))
        self.assertAlmostEqual(resultado, (8,7.2))

    def test_conversion(self):
        resultado = laboratorio.conversioncplx((3,2),(-5,5.2))
        self.assertEqual(resultado, (8,7.2))
        self.assertAlmostEqual(resultado, (8,7.2))

    def test_fase(self): #-0.588 rad o -33.69°
        resultado = laboratorio.fasecplx((3,2),(-5,5.2))
        self.assertEqual(resultado, -0.588)
        self.assertAlmostEqual(resultado, -33.69)

    def test_tensor(self):
        resultado = laboratorio.producto_tesnor([[(1,2), (3,4)], [(2,1), (4,3)]])
        self.assertEqual(resultado, (8,7.2))
        self.assertAlmostEqual(resultado, (8,7.2))
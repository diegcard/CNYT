import cal_matrix_cpmx as cal
import unittest
import numpy as np
"""
-------- Archivo de Testeo de pruebas de la libreria -------
"""

class TestLibVecSpace(unittest.TestCase):

    def test_sumvec(self):
        """test 1: Adición de vectores complejos"""
        c1 = [1 + 5j, -4 - 9j]
        c2 = [1 + 5j, 5 + 17j]
        sum_ver = [(2 + 10j), (1 + 8j)]
        sum_doc = cal.sumacpmx(c1, c2)
        self.assertEqual(sum_doc, sum_ver)

    def test_Inverso_cpmx(self):
        """test 2: Inverso (aditivo) de un vector complejos."""
        c1 = [8.9 + 4.8j, 2.9 - 8.4j]
        sum_ver = [(-8.9 - 4.8j), (-2.9 + 8.4j)]
        sum_doc = cal.inversocpmx(c1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mult_esc(self):
        """test 3: Multiplicación de un escalar por un vector complejo."""
        c1 = [8.9 + 4.8j, 2.9 - 8.4j]
        esc = 5
        sum_ver = [(44.5 + 24j), (14.5 - 42j)]
        sum_doc = cal.mult_esca_vect_cpmx(esc, c1)
        self.assertEqual(sum_doc, sum_ver)

    def test_sum_matrix(self):
        """test 4: Adición de matrices complejas."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        mat2 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(2 + 8j), (-2 - 24j), (8 + 14j)], [(-8 + 4j), (90 - 2j), (26 + 14j)],
                   [(4 + 28j), (4 + 18j), (2 + 6j)]]
        sum_doc = cal.suma_mat_complex(mat1, mat2)
        self.assertEqual(sum_doc, sum_ver)

    def test_inversaadi(self):
        """test 5 :Inversa (aditiva) de una matriz compleja."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(-1 - 4j), (1 + 12j), (-4 - 7j)], [(4 - 2j), (-45 + 1j), (-13 - 7j)],
                   [(-2 - 14j), (-2 - 9j), (-1 - 3j)]]
        sum_doc = cal.mat_inv_cpmx(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mat_mult_esc_cpmx(self):
        """test 6: Multiplicación de un escalar por una matriz compleja."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        esca = 5
        sum_ver = [[(5 + 20j), (-5 - 60j), (20 + 35j)], [(-20 + 10j), (225 - 5j), (65 + 35j)],
                   [(10 + 70j), (10 + 45j), (5 + 15j)]]
        sum_doc = cal.mat_mult_esc_cpmx(esca, mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mat_traspone_cpmx(self):
        """test 7: Transpuesta de una matriz/vector."""
        mat = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 + 4j), (-4 + 2j), (2 + 14j)], [(-1 - 12j), (45 - 1j), (2 + 9j)], [(4 + 7j), (13 + 7j), (1 + 3j)]]
        sum_doc = cal.mat_traspone_cpmx(mat)
        self.assertEqual(sum_doc, sum_ver)

    def test_neg_imag_matrix_cpmx(self):
        """test 8: Conjugada de una matriz/vector"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 - 4j), (-1 + 12j), (4 - 7j)], [(-4 - 2j), (45 + 1j), (13 - 7j)], [(2 - 14j), (2 - 9j), (1 - 3j)]]
        sum_doc = cal.neg_imag_matrix_cpmx(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_adjunta_daga_cpmx(self):
        """test 9: Adjunta (daga) de una matriz/vector"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 - 4j), (-4 - 2j), (2 - 14j)], [(-1 + 12j), (45 + 1j), (2 - 9j)], [(4 - 7j), (13 - 7j), (1 - 3j)]]
        sum_doc = cal.adjunta_daga_cpmx(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_product_mat(self):
        """test 10: Producto de dos matrices (de tamaños compatibles)"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        mat2 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(-77 + 124j), (-65 - 505j), (30 - 121j)], [(-262 + 276j), (2015 + 87j), (554 + 328j)],
                   [(-120 + 10j), (240 + 380j), (-135 + 207j)]]
        sum_doc = cal.product_mat(mat1, mat2)
        self.assertEqual(sum_doc, sum_ver)

    def test_accion_mat(self):
        """test 11: Función para calcular la "acción" de una matriz sobre un vector."""
        mat = [[2 + 4j, 3 - 2j], [4 - 8j, 5 + 1j]]
        vec = [1 + 6j, 2 - 9j]
        sum_ver = "[-34.-15.j  71.-27.j]"
        sum_doc = cal.accion_mat(mat,vec)
        self.assertEqual(sum_doc, sum_ver)

    def test_product_int_vec(self):
        """test 12: Producto interno de dos vectores."""
        c1 = [1 + 5j, -4 - 9j]
        c2 = [1 + 5j, 5 + 17j]
        resp_verd = (109 - 103j)
        resp_doct = cal.produc_interno_vec(c1, c2)
        self.assertEqual(resp_doct, resp_verd)

    def test_norm_vec(self):
        """test 13: Norma de un vector."""
        c1 = [1 + 5j, -4 - 9j]
        resp_verd = 11.09
        resp_doct = cal.norma_vector(c1)
        self.assertEqual(resp_doct, resp_verd)

    def test_distance_vect(self):
        """test 14: Distancia entre dos vectores."""
        vec_1 = [7 + 3j]
        vec_2 = [1 - 5j]
        resp_verd = 10.0
        resp_doct = cal.distance_vect(vec_1, vec_2)
        self.assertEqual(resp_doct, resp_verd)

    def test_val_vec_prop_mat(self):
        """test 15. Valores  y vectores propios de una matriz."""
        mat = [[1, 2, -1], [1, 0, 1],[4, -4, 5]]
        resp_verd = """los valores propios para esta matriz o vector son [3. 2. 1.] y los vectores son [[-0.23570226  0.43643578  0.40824829]
 [ 0.23570226 -0.21821789 -0.40824829]
 [ 0.94280904 -0.87287156 -0.81649658]]"""
        resp_doct = cal.val_vec_prop_mat(mat)
        self.assertEqual(resp_doct,resp_verd)

    def test_mat_unita(self):
        """test 16. Revisar si una matriz es unitaria."""
        mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        resp_verd = "Si es matriz unitaria"
        resp_doct = cal.mat_unita(mat)
        self.assertEqual(resp_doct, resp_verd)

    def test_mat_hermitiana(self):
        """test 17. Revisar si una matriz es Hermitiana."""
        mat = [[1, -1 - 12j, 4 + 7j], [-1 + 12j, 45, 13 + 7j], [4 - 7j, 13 - 7j, 1]]
        resp_verd = "Es hermimtiana"
        resp_doct = cal.mat_hermitiana(mat)
        self.assertEqual(resp_doct, resp_verd)

    def test_prod_tense_mat_vec(self):
        """test 18. Producto tensor de dos matrices/vectores."""
        mat1 = [[2, 3], [1, 4]]
        mat2 = [[5, 3, 2], [1, 0, 2], [-2, 5, 6]]
        resp_verd = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8],[1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        resp_doct = cal.prod_tense_mat(mat1, mat2)
        self.assertEqual(resp_doct, resp_verd)


if __name__ == '__main__':
    unittest.main()

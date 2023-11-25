import cal_matrix_cpmx as cal
import numpy as np


def val_vect(observable):
    valores, vectores = np.linalg.eig(observable)
    lista_valores = []
    lista_vectores = []
    for index in range(len(valores)):
        lista_valores += [(valores[index].real, valores[index].imag)]
    for index in range(len(vectores)):
        vector = []
        for index_2 in range(len(vectores[0])):
            vector += [(vectores[index][index_2].real, vectores[index][index_2].imag)]
        lista_vectores += [vector]
    return lista_valores, lista_vectores

def val_prop_mat_numpy(mat):
    valores_propios, vectores_propios = np.linalg.eig(mat)
    return valores_propios#"los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def vec_prop_mat_numpy(mat):
    valores_propios, vectores_propios = np.linalg.eig(mat)
    return vectores_propios#"los valores propios para esta matriz o vector son {} y los vectores son {}".format(valores_propios, vectores_propios)

def varianza(mat1,mat2):
    mat1 = np.matrix(mat1)
    mat2 = np.matrix(mat2)
    landa1 = mat1-mat2
    rest = val_prop_mat_numpy(landa1)
    product = np.dot(rest, rest)
    return product

def transicion(v1,v2):
    b = cal.produc_interno_vec(v2,v1)
    b = b/(cal.normal(v1)*cal.normal(v2))
    prob = cal.module_vector(b)
    return prob

def media(matrix,ket):
    if cal.normal(ket) != 1:
        ket = cal.normalizar_vector(ket)
    resp = cal.mat_hermitiana(matrix)
    if resp == "La madrix no es hermitiana" or resp == "Error, el tamaño de matrix es incorrrecto":
        return resp
    else:
        med = cal.produc_interno_vec(cal.accion_mat(matrix,ket),ket)
        return med.real

def transitar_a_vectores(mat,ket):
    if cal.normalizar_vector(ket) != 1:
        ket = cal.normalizar_vector(ket)
    vectores = vec_prop_mat_numpy(mat)
    valores = val_prop_mat_numpy(mat)
    prob = []
    for i in range(len(vectores)):
        proba = transicion(ket,vectores[i])
        prob.append(proba)
    return prob

if __name__ == '__main__':
    #Exercise 4.3.1
    v1 = [[(1, 0)], [(0, 0)]]
    observable_x = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
    vr = cal.m_action(observable_x, v1)
    valores_x, vectores_x = val_vect(observable_x)
    print(vec_prop_mat_numpy([[0, 1], [1, 0]]))
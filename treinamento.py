import cv2
import os
import numpy as np

eigeface = cv2.face.EigenFaceRecognizer_create(num_components=50)
#fisherface = cv2.face.FisherFaceRecognizer_create()
#lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagensComId():
    caminhos = [os.path.join('fotos',f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        #print(id)
        ids.append(id)
        faces.append(imagemFace)
        #cv2.imshow("Face", imagemFace)
        #cv2.waitKey(10)
    return np.array(ids), faces
ids, faces = getImagensComId()
print("Treinando...")

eigeface.train(faces, ids)
eigeface.write('classificadorEigen.yml')

#fisherface.train(faces, ids)
#fisherface.write('classificadorFisher.yml')

#lbph.train(faces, ids)
#lbph.write('classificadorlbph.yml')

print("Treinamento realizado!")
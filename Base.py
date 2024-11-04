import cv2

# Inicializar Haar Cascade e reconhecedor facial
classific = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read("classificadorEigen.yml")

# Parâmetros de redimensionamento e fonte
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
limite_confianca = 8000  # Limite para considerar o rosto como desconhecido

# Inicializar a câmera e reduzir a resolução para aumentar FPS
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  # Reduzindo a resolução da câmera
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    conectado, imagem = camera.read()

    if not conectado:
        break

    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesdetec = classific.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

    for (x, y, l, a) in facesdetec:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        id, confianca = reconhecedor.predict(imagemFace)

        # Desenhar o retângulo ao redor do rosto
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        if confianca < limite_confianca:
            # Se a confiança for baixa, mostrar o ID do rosto
            cv2.putText(imagem, str(id), (x, y + a + 30), font, 2.0, (0, 0, 255), 2)
        else:
            # Se a confiança for alta, mostrar "Rosto inválido"
            cv2.putText(imagem, "Rosto invalido", (x, y + a + 30), font, 1.0, (0, 0, 255), 2)

    # Mostrar o vídeo com a detecção de faces
    cv2.imshow("Face", imagem)

    # Pressionar 'q' para sair
    if cv2.waitKey(1) == ord('q'):
        break

# Finalizar e liberar os recursos
camera.release()
cv2.destroyAllWindows()

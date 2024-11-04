import cv2

# Inicializa o classificador de face com Haar Cascade
classific = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Inicializa a câmera (ajustando a resolução para melhorar o FPS)
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Reduz a resolução do vídeo
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Variáveis de controle
amostra = 1
numAmostra = 25
id = input("Digite seu identificador: ")
largura, altura = 220, 220
print("Capturando a face...")

while True:
    # Captura o frame atual da câmera
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Detecção de faces com parâmetros otimizados
    facesdetec = classific.detectMultiScale(imagemCinza, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

    # Itera sobre as faces detectadas
    for (x, y, l, a) in facesdetec:
        # Desenha um retângulo em torno do rosto
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

    # Mostra o vídeo com a detecção de faces
    cv2.imshow("Face", imagem)

    # Espera por uma tecla
    key = cv2.waitKey(1) & 0xFF
    
    # Se a tecla 's' for pressionada, captura a imagem
    if key == ord('q'):
        if amostra <= numAmostra:
            imagemface = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
            cv2.imwrite(f"fotos/pessoas.{id}.{amostra}.jpg", imagemface)
            print(f"[foto {amostra} capturada com sucesso]")
            amostra += 1
        else:
            print("Número máximo de amostras já capturado.")

    # Se a tecla 'q' for pressionada, sai do loop
    if key == ord('s'):
        break

# Libera os recursos
print("Captura encerrada.")
camera.release()
cv2.destroyAllWindows()

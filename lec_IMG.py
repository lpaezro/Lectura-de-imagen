#Librería
import cv2 #clase estatica
from cv2 import imshow #importacion del metodo

"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe" #referencia al nombre de la imagen de *algun formato
#imgText="anime" #ejemplo

#PROCESO DE LECTURA DE IMAGEN 

img= cv2.imread(imgText+'.png') #imread carga una imagen desde un archivo especificado de la variable imgText concatenando segun el MISMO formato de imagen
#img= cv2.imread(imgText+'.jpg')   #ejemplo

#cv2.cvtColor() metodo que se usa para convertir una imagen de un espacio de color a otro
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # COLOR_BGR2GRAY convierte la imagen a gris, la cual elimina los campos RGB y la cambia a escala de grises.
cv2.imshow('Gris', img_gris) #nombre de la ventana 'gris', referecia a img_gris


"""
--------otros elementos--------
COLOR_BGR2BGRA =tono normal de la imagen
COLOR_RGBA2BGRA = tonos rojos
COLOR_BGR2GRAY =escala de grises


"""



b = img.copy()  #lo siguiente toma la imagen, la copia y muestra la misma imagen en tono azul 
b[:, :, 1] = 0  #b[:, :, 0] = 0  cambian imagen a verde     |b[:, :, 0] = 0 cambia la imagen a rojo
b[:, :, 2] = 0  #b[:, :, 2] = 0                             |b[:, :, 1] = 0
cv2.imshow('B-RGB', b)


#los 0 queda inmodificado el color mas si se cambia el numero se presenta la modificacion de la gama de color
# los : (dos puntos tambien cambian el color de la imagen si se introduce valor numerico) 

#b[:, :, 1] = 0  algun tipo de rosado                       |b[:, :, 2] = 0 #azul mas claro
#b[:, :, 1] = 0                                             |b[:, :, 2] = 0


#b[:, :, 0] = 0                                             |b[:, :, 2] = 1  #azul oscuro
#b[:, :, 0] = 0                                             |b[:, :, 2] = 2 


g = img.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0
cv2.imshow('G-RGB', g)



imshow('Imagen Original',img)# Usando el método imshow() permite la visualización de la imagen de modo que:
#'imagen original' dara el nombre a la ventana y img buscara la imagen por medio de imread.
# ('nombre de la ventana',parametro-variable en donde se muestra)

cv2.waitKey(0)##espera a que el usuario presione cualquier tecla. El 0 evita que la pantalla se cierre
cv2.destroyAllWindows()# metodo.finaliza el proceso y cierra todas las ventanas abiertas 
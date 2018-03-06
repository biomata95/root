import sys
import os
import numpy as np
import numpy.random as rnd
import glob
import cv2
import math
import colorsys
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

def leitura(arquivo):
	img = cv2.imread(arquivo) 
	return img

def visualizarImagem(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def histograma(imagem,lista):
	histTeste = cv2.calcHist([imagem],[0],None,[256],[0,256])
	matrizValores = [[0.0 for i in range(0,4)]for j in range(0,len(lista))]
	correlation=0
	quiQuadrado=0
	interse=0
	battha=0
	for i in range(0,len(lista)):
		comparativa=cv2.imread(lista[i])
		histComparativa = cv2.calcHist([comparativa],[0],None,[256],[0,256])
		correlation = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CORREL)
		correlation=str(correlation)
		quiQuadrado = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CHISQR)
		quiQuadrado=str(quiQuadrado)
		interse = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_INTERSECT)
		interse=str(interse)
		battha = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_BHATTACHARYYA)
		battha=str(battha)
		matrizValores[i][0]=correlation[:5]
		matrizValores[i][1]=quiQuadrado[:5]
		matrizValores[i][2]=interse[:5]
		matrizValores[i][3]=battha[:5]


	fig = plt.figure("Histograma Comparacoes")

	fig.suptitle("Histograma Comparacoes", fontsize = 20)
	plt.rcParams["figure.figsize"] = [15,7]
	fig, axes = plt.subplots(nrows=3,ncols=7)

	axes[0,0].imshow(imagem)
	axes[0,0].axis('off')
	axes[0,0].set_title('Figura Teste')
	axes[0,1].axis('off')
	axes[0,1].set_title('Escala')
	axcolor = 'lightgoldenrodyellow'
	escala = plt.axes([0.23, 0.67, 0.13, 0.21], facecolor=axcolor)
	radio = RadioButtons(escala, ('Correlacao','QuiQuadrado','Intersecao','BHATTACHARYYA'))
	k=0
	contL=0
	for i in range(0,3):
		cont=0
		for j in range(0,math.trunc(len(lista)/2)):
			if(i==0):
				axes[i,j].axis('off')
			else:
				imag=cv2.imread(lista[k])
				axes[i,j].axis('off')

				coluna=matrizValores[k]			
				
				if(i==1):
					rax = plt.axes([0.085+cont, 0.4, 0.05, 0.21], facecolor=axcolor)
					radio = RadioButtons(rax, (coluna[0],coluna[1],coluna[2],coluna[3]))
					cont=cont+0.14
				if(i==2):	
					rax2 = plt.axes([0.085+cont, 0.004+contL, 0.05, 0.21], facecolor=axcolor)
					radio = RadioButtons(rax2, (coluna[0],coluna[1],coluna[2],coluna[3]))
					cont=cont+0.14
				axes[i,j].imshow(imag)
				k=k+1
		contL=contL+0.07

	fig.show()
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def main():

	arquivo=sys.argv[1]; # nome do arquivo -> imagem
	lista=glob.glob("Archive/*.png") # Varreduras dos arquivos .png do diretorio Archive/
	arquivo=sys.argv[1]; # nome do arquivo -> imagem
	img=leitura(arquivo)
	histograma(img,lista)


if __name__ == "__main__":
	main()

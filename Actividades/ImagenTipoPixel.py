import numpy as np
from PIL import Image   

def matriz(matriz: np.ndarray, factor_escala: int =20) -> None:
    paleta = {  
        0: (255,255,255), # BLANCO 
        1: (255,0,0),     # ROJO 
        2: (0,0,0),     # NEGRO
    }

    alto, ancho = matriz.shape
    img_rgb = np.zeros((alto, ancho, 3), dtype=np.uint8)
    
    for y in range(alto):
        for x in range(ancho):
            color = paleta.get(matriz[y,x], (255,255,255)) 
            img_rgb[y,x] = color

    img = Image.fromarray(img_rgb, mode='RGB')
    w, h = img.size
    img_up = img.resize((w*factor_escala, h*factor_escala), resample=Image.Resampling.NEAREST)
    
    img_up.show()


corazon = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,2,2,2,0,0,0,2,2,2,0,0,0],
    [0,0,2,1,1,1,2,0,2,1,1,1,2,0,0],
    [0,2,1,1,0,1,1,2,1,1,1,1,1,2,0],
    [0,2,1,0,1,1,1,1,1,1,1,1,1,2,0],
    [0,2,1,0,1,1,1,1,1,1,1,1,1,2,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
], dtype=np.uint8)

matriz(corazon, factor_escala=30)
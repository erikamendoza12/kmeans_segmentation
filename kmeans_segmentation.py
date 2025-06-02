import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt
import random
from skimage.viewer import ImageViewer  # Para visualización básica

def read_dicom_3d(directory):
    """
    Lee un conjunto de imágenes DICOM de un directorio y reconstruye un volumen 3D.

    Parameters:
        directory (str): Ruta al directorio que contiene los archivos DICOM.

    Returns:
        volume (numpy.ndarray): Volumen 3D reconstruido a partir de los cortes DICOM.
    """
    slices = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".dcm"):
            filepath = os.path.join(directory, filename)
            ds = pydicom.dcmread(filepath)
            slices.append(ds.pixel_array)
    volume = np.stack(slices, axis=-1)
    return volume

# Ruta a las imágenes DICOM
path = r"D:\MAESTRÍA\INTELIGENCIA ARTIFICIAL\TP2\DICOM"
image = read_dicom_3d(path)

# Cálculo de los valores mínimo y máximo de intensidad
I_max = np.max(image)
I_min = np.min(image)

# Generación aleatoria de los centroides iniciales
C1 = random.randint(round(abs(I_min)), round(abs(I_max)))
C2 = random.randint(round(abs(I_min)), round(abs(I_max)))

# Inicialización de variables
diferencia_C1 = 2
diferencia_C2 = 2
iteraciones = 0

# Algoritmo K-means personalizado para segmentación binaria
while diferencia_C1 >= 1 or diferencia_C2 >= 1:
    N1 = N2 = S1 = S2 = 0

    # Asignación de cada voxel al centroide más cercano
    for value in np.nditer(image):
        if abs(value - C1) < abs(value - C2):
            N1 += 1
            S1 += value
        else:
            N2 += 1
            S2 += value

    # Re-cálculo de los centroides
    promedio_C1 = S1 / N1 if N1 != 0 else C1
    promedio_C2 = S2 / N2 if N2 != 0 else C2

    # Evaluación de la convergencia
    diferencia_C1 = abs(promedio_C1 - C1)
    diferencia_C2 = abs(promedio_C2 - C2)

    if diferencia_C1 >= 1 or diferencia_C2 >= 1:
        C1 = promedio_C1
        C2 = promedio_C2
    else:
        # Generación de la imagen binarizada usando el centroide de mayor valor
        umbral = max(promedio_C1, promedio_C2)
        image_binarized = image > umbral

    iteraciones += 1

print(f"Convergencia alcanzada en {iteraciones} iteraciones.")

# Visualización
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image[:, :, image.shape[2] // 2], cmap='gray')
plt.title("Corte Medio Original")

plt.subplot(1, 2, 2)
plt.imshow(image_binarized[:, :, image_binarized.shape[2] // 2], cmap='gray')
plt.title("Segmentación Binaria")
plt.show()

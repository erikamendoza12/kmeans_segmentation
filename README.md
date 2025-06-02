# Segmentación de Volumen DICOM 3D mediante K-means

Este repositorio contiene una implementación en Python de un algoritmo de segmentación basado en K-means para imágenes médicas en formato DICOM 3D.

## 📋 Descripción

El objetivo del proyecto es aplicar una segmentación binaria utilizando el algoritmo K-means con dos centroides. La segmentación se realiza sobre un volumen reconstruido a partir de múltiples cortes DICOM, y se visualiza un corte axial central del volumen original y segmentado.

## 🧠 Tecnologías utilizadas

- Python 3.8+
- NumPy
- pydicom
- matplotlib
- scikit-image (para `ImageViewer`, opcional)


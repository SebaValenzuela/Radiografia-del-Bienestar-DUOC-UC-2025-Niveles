from wordcloud import WordCloud, ImageColorGenerator
from io import BytesIO
import pandas as pd
from PIL import Image
import numpy as np

def crear_wordcloud(df: pd.DataFrame, columnas: list, genero: str = None,
                     ancho=800, alto=400, max_words=200, mask_path="plots/images/cloud_mask.png") -> BytesIO:

    # Filtrar por género
    df_filtered = df.copy()
    if genero in ["Masculino", "Femenino"]:
        df_filtered = df_filtered[df_filtered["GENERO"] == genero]

    # Combinar todas las palabras
    palabras = []
    for col in columnas:
        serie = df_filtered[col].dropna().astype(str)
        for texto in serie:
            palabras.extend(texto.split())
    texto_completo = " ".join(palabras)

    # Cargar máscara en escala de grises
    mask_img = Image.open(mask_path).convert("L")  # L = grayscale
    mask = np.array(mask_img)

    # Invertir colores: nube negra -> blanca, fondo transparente -> negro
    mask = 255 - mask

    # Generar WordCloud
    wc = WordCloud(
        width=ancho, height=alto, max_words=max_words,
        background_color="white",
        mask=mask,
        contour_color='black'
    ).generate(texto_completo)

    # Guardar en buffer
    buf = BytesIO()
    wc.to_image().save(buf, format="PNG")
    buf.seek(0)
    return buf

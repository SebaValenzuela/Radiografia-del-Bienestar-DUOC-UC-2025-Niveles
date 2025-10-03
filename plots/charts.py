import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd

def crear_piechart(df: pd.DataFrame, columna: str, titulo: str = None) -> BytesIO:
    # Contar frecuencia de valores en la columna
    counts = df[columna].value_counts()

    # Crear gráfico
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ["#2AA5F9", "#143348", "#A5A5A5"]
    wedges, texts, autotexts = ax.pie(
        counts.values,
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
    )

    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontsize(14)

    # Agregar leyenda abajo
    ax.legend(
        wedges, 
        counts.index,
        title="",
        loc="lower center", 
        bbox_to_anchor=(0.5, -0.2),
        ncol=2,
        frameon=False
    )

    if titulo:
        ax.set_title(titulo)

    # Guardar en buffer
    buf = BytesIO()
    plt.savefig(buf, format="PNG", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return buf

# def crear_barchart(df: pd.DataFrame, columnas: list, titulo: str = None) -> BytesIO:
#     # Definir colores por defecto si no se pasan
#     if colores is None:
#         colores = plt.cm.Paired.colors  # paleta de Matplotlib

#     # Preparar figura
#     fig, ax = plt.subplots(figsize=(8, 6))

#     # Posiciones de las barras
#     n_cols = len(columnas)
#     indices = range(len(df))  # si quieres índices del df, pero para categóricas conviene agrupar

#     # Agrupar y graficar cada columna
#     for i, col in enumerate(columnas):
#         counts = df[col].value_counts()
#         ax.bar(
#             counts.index + f" ({col})",  # etiquetas con columna
#             counts.values,
#             color=colores[i % len(colores)],
#             label=col
#         )

#     # Estilo del gráfico
#     ax.set_ylabel("Cantidad")
#     if titulo:
#         ax.set_title(titulo)
#     ax.legend()
#     plt.xticks(rotation=45, ha="right")

#     # Guardar en buffer
#     buf = BytesIO()
#     plt.tight_layout()
#     plt.savefig(buf, format="PNG")
#     plt.close(fig)
#     buf.seek(0)
#     return buf

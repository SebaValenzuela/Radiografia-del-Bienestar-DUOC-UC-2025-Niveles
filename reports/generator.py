from plots.wordclouds import crear_wordcloud
from plots.charts import crear_piechart, crear_barchart
from utils.pptx_utils import rellenar_template

def generar_global_report(df, df_2022, template_path="reports/templates/template-global.pptx", output_path="reports/output/global_final.pptx"):
    columnas = ["PRAB01[PRA01]", "PRAB01[PRA02]", "PRAB01[PRA03]"]
    columnas_2022 = ["ExpEmocional_01", "ExpEmocional_02", "ExpEmocional_03"]

    wc_global = crear_wordcloud(df, columnas=columnas, genero=None)
    wc_hombres = crear_wordcloud(df, columnas=columnas, genero="Masculino")
    wc_mujeres = crear_wordcloud(df, columnas=columnas, genero="Femenino")
    wc_2022 = crear_wordcloud(df_2022, columnas=columnas_2022, genero=None)
    pc_gender = crear_piechart(df, columna="GENERO", titulo="Sexo")
    pc_student_day = crear_piechart(df, columna="JORNADA", titulo="Jornada")
    pc_student_type = crear_piechart(df, columna="TIPO_ALUMNO", titulo="Tipo de Alumno")
    bc_sedes = crear_barchart(df, columna="SEDE", titulo="Sede")
    bc_escuelas = crear_barchart(df, columna="ESCUELA", titulo="Escuela")

    placeholders = {
        "wordcloud_global": wc_global,
        "wordcloud_hombres": wc_hombres,
        "wordcloud_mujeres": wc_mujeres,
        "wordcloud_2022": wc_2022,
        "gender_pie_chart": pc_gender,
        "student_day_pie_chart": pc_student_day,
        "student_type_pie_chart": pc_student_type,
        "sedes_bar_chart": bc_sedes,
        "escuelas_bar_chart": bc_escuelas,
    }

    rellenar_template(template_path, output_path, placeholders)

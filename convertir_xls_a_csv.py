import pandas as pd
import os

carpeta_entrada = "datos_xls"
carpeta_salida = "datos_csv"
os.makedirs(carpeta_salida, exist_ok=True)

for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".xls"):
        ruta_xls = os.path.join(carpeta_entrada, archivo)
        nombre_csv = os.path.splitext(archivo)[0] + ".csv"
        ruta_csv = os.path.join(carpeta_salida, nombre_csv)

        try:
            # Lee todas las tablas HTML dentro del archivo
            tablas = pd.read_html(ruta_xls, flavor="lxml")

            if len(tablas) >= 10:
                df = tablas[9]  # Seleccionamos la tabla 9 directamente
                df.to_csv(ruta_csv, index=False)
                print(f"✔️ Convertido: {archivo} → {nombre_csv}")
            else:
                print(f"⚠️ No hay suficientes tablas en: {archivo}")
        except Exception as e:
            print(f"❌ Error al procesar {archivo}: {e}")

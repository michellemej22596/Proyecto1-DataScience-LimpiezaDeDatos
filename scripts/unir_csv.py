import pandas as pd
import os

carpeta_csv = "datos_csv"
csvs = [f for f in os.listdir(carpeta_csv) if f.endswith(".csv")]

df_unido = pd.DataFrame()

for archivo in csvs:
    ruta = os.path.join(carpeta_csv, archivo)

    try:
        # Leer el CSV ignorando la primera fila
        df = pd.read_csv(ruta, header=1)
        df_unido = pd.concat([df_unido, df], ignore_index=True)
        print(f"✔️ Unido: {archivo}")
    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")

# Guardar el archivo combinado
df_unido.to_csv("establecimientos_unidos.csv", index=False)
print("✅ Archivo final generado: establecimientos_unidos.csv")

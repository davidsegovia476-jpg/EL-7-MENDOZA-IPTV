import os

# ==============================================================================
# CONFIGURACIÓN COMPATIBLE MUNDIAL - SIN TOKENS NI PROXIES CAÍDOS
# ==============================================================================
URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def generar_m3u():
    print("\n--- Generando lista compatible nativa ---")
    
    # Este formato le indica al reproductor que cargue el reproductor web interno
    # Es el estándar más seguro para que no dependas de páginas de terceros.
    contenido_m3u = (
        f'#EXTM3U\n'
        f'#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina" tvg-id="" tvg-logo="" radio="false", {NOMBRE_CANAL_M3U}\n'
        f'{URL_YOUTUBE_LIVE}\n'
    )

    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_final_archivo = os.path.join(ruta_carpeta, NOMBRE_ARCHIVO_M3U)
    
    try:
        with open(ruta_final_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_m3u)
        print("✅ ¡Archivo .m3u público e inmortal creado con éxito!")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")

if __name__ == "__main__":
    generar_m3u()


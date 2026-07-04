import os

# ==============================================================================
# CONFIGURACIÓN PÚBLICA MUNDIAL (COMPATIBLE CON CUALQUIER REPRODUCTOR)
# ==============================================================================
# Este es el código único del directo de YouTube de Canal 7 Mendoza
ID_YOUTUBE = "Vh8xmLBJtR8" 
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def generar_m3u():
    print("\n--- Creando lista IPTV para reproducción pública ---")
    
    # Este formato transforma el directo en un .m3u8 real que abre cualquier TV
    enlace_publico = f"https://workers.dev{ID_YOUTUBE}.m3u8"
    
    contenido_m3u = (
        f'#EXTM3U\n'
        f'#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n'
        f'{enlace_publico}\n'
    )

    # Guarda el archivo de forma automática en la carpeta del repositorio
    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_final_archivo = os.path.join(ruta_carpeta, NOMBRE_ARCHIVO_M3U)
    
    try:
        with open(ruta_final_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_m3u)
        print("✅ ¡Archivo .m3u generado con éxito para todo el público!")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")

if __name__ == "__main__":
    generar_m3u()


import subprocess
import time
import os
import sys

# ==============================================================================
# CONFIGURACIÓN GENERAL (MÉTODO ULTRA SEGURO SIN ERRORES)
# ==============================================================================
URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"
TIEMPO_BUCLE = 14400 
def obtener_enlace_m3u8(url_youtube):
    try:
        # El servidor remoto usará yt-dlp para extraer el enlace directo
        comando = ["yt-dlp", "--quiet", "--no-warnings", "-g", "-f", "best", url_youtube]
        enlace = subprocess.check_output(comando, text=True, stderr=subprocess.DEVNULL).strip()
        if enlace and "googlevideo.com" in enlace:
            return enlace
    except:
        pass
    return None

def generar_m3u():
    print("🤖 Buscando transmisión de El Siete Mendoza...")
    enlace_m3u8 = obtener_enlace_m3u8(URL_YOUTUBE_LIVE)
    
    if not enlace_m3u8: 
        print("⚠️ YouTube bloqueado. Usando servidor web oficial como respaldo...")
        enlace_m3u8 = "https://bofstreaming.com"
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Archivo M3U creado con éxito en el servidor remoto!")

if __name__ == "__main__":
    generar_m3u()

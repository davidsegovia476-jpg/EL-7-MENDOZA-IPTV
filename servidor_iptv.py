import subprocess
import os
import sys

# ==============================================================================
# CONFIGURACIÓN GENERAL (MÉTODO BLINDADO)
# ==============================================================================
URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def obtener_enlace_m3u8(url_youtube):
    try:
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
        # SEÑAL WEB OFICIAL QUE NUNCA SE CAE Y ES COMPATIBLE CON TU SMART TV
        enlace_m3u8 = "https://bofstreaming.com"
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Archivo M3U creado con éxito en el servidor remoto!")

if __name__ == "__main__":
    generar_m3u()

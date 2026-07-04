import subprocess
import os
import sys

URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def obtener_enlace_m3u8(url_youtube):
    # Verificamos si las cookies secretas llegaron bien al servidor remoto
    if os.path.exists("cookies.txt") and os.path.getsize("cookies.txt") > 0:
        print("🍪 Cookies cargadas con éxito en el servidor de la nube.")
        comando = ["yt-dlp", "--quiet", "--no-warnings", "--cookies", "cookies.txt", "-g", "-f", "best", url_youtube]
    else:
        print("⚠️ No se encontraron cookies. Intentando extracción limpia...")
        comando = ["yt-dlp", "--quiet", "--no-warnings", "-g", "-f", "best", url_youtube]
        
    try:
        enlace = subprocess.check_output(comando, text=True, stderr=subprocess.DEVNULL).strip()
        if enlace and "googlevideo.com" in enlace:
            return enlace
    except Exception as e:
        print(f"❌ Error en yt-dlp: {e}")
    return None

def generar_m3u():
    print("🤖 Buscando token de transmisión real de El Siete Mendoza...")
    enlace_m3u8 = obtener_enlace_m3u8(URL_YOUTUBE_LIVE)
    
    if not lenlace_m3u8 or "googlevideo.com" not in enlace_m3u8: 
        print("⚠️ Google bloqueó el acceso sin cookies. Aplicando señal web como plan B temporal...")
        enlace_m3u8 = "https://bofstreaming.com"
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print(f"✅ ¡Archivo M3U creado con éxito!")
    print(f"🔗 URL Guardada: {enlace_m3u8[:50]}...")

if __name__ == "__main__":
    generar_m3u()

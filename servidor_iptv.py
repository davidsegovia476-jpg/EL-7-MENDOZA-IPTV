import subprocess
import os

URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def obtener_enlace_m3u8(url_youtube):
    if os.path.exists("cookies.txt") and os.path.getsize("cookies.txt") > 0:
        comando = ["yt-dlp", "--quiet", "--no-warnings", "--cookies", "cookies.txt", "-g", "-f", "best", url_youtube]
    else:
        comando = ["yt-dlp", "--quiet", "--no-warnings", "-g", "-f", "best", url_youtube]
        
    try:
        enlace = subprocess.check_output(comando, text=True, stderr=subprocess.DEVNULL).strip()
        if enlace and "googlevideo.com" in enlace:
            return enlace
    except:
        pass
    return None

def generar_m3u():
    enlace_m3u8 = obtener_enlace_m3u8(URL_YOUTUBE_LIVE)
    
    # AQUÍ CORREGIMOS EL ERROR: Quitamos la 'l' que hacía fallar al servidor
    if not enlace_m3u8 or "googlevideo.com" not in enlace_m3u8: 
        enlace_m3u8 = "https://bofstreaming.com"
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)

if __name__ == "__main__":
    generar_m3u()

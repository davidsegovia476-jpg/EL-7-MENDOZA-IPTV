import subprocess
import os
import sys

# ==============================================================================
# CONFIGURACIÓN CON TU URL REAL DE YOUTUBE (¡LA QUE SÍ ABRE!)
# ==============================================================================
URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def obtener_enlace_m3u8(url_youtube):
    try:
        # El servidor de la nube usará yt-dlp para extraer el token oculto de Google Video
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
    
    # Si por alguna razón la extracción falla un segundo, volvemos a intentar con más fuerza
    if not enlace_m3u8 or "googlevideo.com" not in enlace_m3u8:
        try:
            comando_fuerza = ["yt-dlp", "-g", "-f", "95", URL_YOUTUBE_LIVE]
            enlace_m3u8 = subprocess.check_output(comando_fuerza, text=True, stderr=subprocess.DEVNULL).strip()
        except:
            pass

    # SI TODO FALLA, DEJAMOS TU URL ORIGINAL COMO RESPALDO EXCLUSIVO
    if not enlace_m3u8 or "googlevideo.com" not in enlace_m3u8: 
        print("⚠️ Extracción remota con demora. Guardando tu URL de respaldo directa...")
        enlace_m3u8 = URL_YOUTUBE_LIVE
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Archivo M3U creado con éxito usando tu enlace correcto!")

if __name__ == "__main__":
    generar_m3u()

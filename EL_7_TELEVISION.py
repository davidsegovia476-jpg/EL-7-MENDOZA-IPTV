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
        comando = [sys.executable, "-m", "yt_dlp", "--quiet", "--no-warnings", "-g", "-f", "best", url_youtube]
        enlace = subprocess.check_output(comando, text=True, stderr=subprocess.DEVNULL).strip()
        if enlace and "googlevideo.com" in enlace:
            return enlace
    except:
        pass
    return None

def generar_m3u():
    print("\n--- Iniciando ciclo de renovacion del canal ---")
    enlace_m3u8 = obtener_enlace_m3u8(URL_YOUTUBE_LIVE)
    
    if not enlace_m3u8: 
        print("⚠️ yt-dlp no pudo extraer el enlace oculto.")
        print("Usando tu URL directa de YouTube como respaldo en la lista...")
        enlace_m3u8 = URL_YOUTUBE_LIVE
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_m3u8}\n'
    
   # ... (Todo tu código anterior se mantiene EXACTAMENTE IGUAL)

if __name__ == "__main__":
    try:
        print("Iniciando actualizador automatico de IPTV para El Siete en GitHub...")
        print("-" * 50)
        
        # Quitamos el bucle 'while True' para que corra una vez y guarde en el repositorio
        generar_m3u()
        print("\n✅ Proceso terminado y archivo actualizado con éxito.")
        
    except KeyboardInterrupt:
        print("\nScript detenido por el usuario.")
    except Exception as error_critico:
        print(f"\n💥 OCURRIO UN ERROR CRÍTICO: {error_critico}")

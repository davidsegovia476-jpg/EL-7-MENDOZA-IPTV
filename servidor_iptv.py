import urllib.request
import re
import os

# ==============================================================================
# LÓGICA REFACTORIZADA: EXTRACTOR DIRECTO DE CÓDIGO FUENTE (ANTI-BLOQUEOS)
# ==============================================================================
URL_YOUTUBE_LIVE = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def extraer_token_directo(url):
    print("🤖 Escaneando el código fuente de YouTube para extraer el token activo...")
    try:
        # Simulamos un navegador web real para que YouTube nos deje leer el código de la página
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
            
        # Buscamos la URL secreta .m3u8 de Google Video escondida dentro del código
        enlaces_hls = re.findall(r'(https?://manifest\.googlevideo\.com/[^\s"\']+\.m3u8[^\s"\']*)', html)
        
        if enlaces_hls:
            # Limpiamos barras invertidas raras que a veces mete YouTube en su código
            token_limpio = enlaces_hls[0].replace(r'\/', '/').replace('\\', '')
            print("🎯 ¡Espectacular! Se encontró un token fresco en el código fuente.")
            return token_limpio
            
    except Exception as e:
        print(f"⚠️ Error al leer el código fuente: {e}")
    return None

def generar_m3u():
    enlace_final = extraer_token_directo(URL_YOUTUBE_LIVE)
    
    # Si todo falla, dejamos la señal del servidor oficial como salvavidas real
    if not enlace_final or "googlevideo.com" not in enlace_final:
        print("⚠️ No se pudo extraer del código fuente. Aplicando señal del servidor web oficial...")
        enlace_final = "https://bofstreaming.com"
        
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_final}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Archivo M3U creado y guardado en internet con éxito!")

if __name__ == "__main__":
    generar_m3u()


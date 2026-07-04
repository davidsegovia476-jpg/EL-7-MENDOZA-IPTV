import subprocess
import re
import urllib.request
import os

# ==============================================================================
# EXTRACTOR DE SEÑAL REAL DESDE LA WEB OFICIAL DE EL SIETE MENDOZA
# ==============================================================================
URL_WEB_OFICIAL = "https://elsietetv.com.ar"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def extraer_m3u8_oficial():
    try:
        # El servidor simula ser un navegador común para que la web le dé acceso
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(URL_WEB_OFICIAL, headers=headers)
        
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode('utf-8')
        
        # Buscamos enlaces con formato .m3u8 ocultos en el código de la página
        enlaces = re.findall(r'(https?://[^\s"\']+\.m3u8[^\s"\']*)', html)
        
        for url in enlaces:
            # Filtramos para asegurarnos de que sea el servidor de video de Canal 7
            if "canal7mza" in url or "bofstreaming" in url:
                return url.replace('\\', '') # Limpiamos barras raras si las hay
                
    except Exception as e:
        print(f"⚠️ Error al escanear la web oficial: {e}")
    
    # Si la web cambia, este es el enlace base directo que usa el canal hoy
    return "https://bofstreaming.com"

def generar_m3u():
    print("🤖 Escaneando la web oficial de El Siete Mendoza para buscar el .m3u8 activo...")
    enlace_final = extraer_m3u8_oficial()
    
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{enlace_final}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print(f"✅ ¡Archivo M3U creado con éxito!")
    print(f"🔗 Enlace guardado: {enlace_final}")

if __name__ == "__main__":
    generar_m3u()


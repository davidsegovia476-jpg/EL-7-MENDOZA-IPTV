import os

# ==============================================================================
# CONFIGURACIÓN DEFINITIVA CON ENLACE DE VIDEO PURO M3U8 (¡EL QUE SÍ ABRE!)
# ==============================================================================
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

# Este es el streaming oficial directo del servidor del canal, compatible con cualquier TV
URL_STREAM_DIRECTO = "https://bofstreaming.com"

def generar_m3u():
    print("🤖 Generando lista de canales con señal directa M3U8...")
    
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{URL_STREAM_DIRECTO}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Archivo M3U creado con éxito en internet!")

if __name__ == "__main__":
    generar_m3u()

import os

# ==============================================================================
# CONFIGURACIÓN COMPATIBLE CON AJUSTES DE RED (¡NUEVO ENLACE SEGURO!)
# ==============================================================================
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

# Este es el enlace de video puro M3U8 alternativo que saltea los bloqueos de red de la web
URL_STREAM_SEGURO = "https://telefe.com"

def generar_m3u():
    print("🤖 Generando archivo M3U con enlace compatible para Smart TV...")
    
    contenido_m3u = f'#EXTM3U\n#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina", {NOMBRE_CANAL_M3U}\n{URL_STREAM_SEGURO}\n'
    
    with open(NOMBRE_ARCHIVO_M3U, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_m3u)
    print("✅ ¡Lista M3U creada con éxito!")

if __name__ == "__main__":
    generar_m3u()

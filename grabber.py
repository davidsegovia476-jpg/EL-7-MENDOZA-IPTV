

import os
import subprocess
import re

# Configuración
channel_url = "https://youtu.be/Vh8xmLBJtR8"
output_file = "canal7mendoza.m3u"

print("Instalando/Actualizando yt-dlp...")
# Aseguramos tener yt-dlp instalado en el entorno de GitHub
subprocess.run(["pip", "install", "-U", "yt-dlp"], stdout=subprocess.DEVNULL)

print("Buscando el enlace de streaming .m3u8 en vivo...")
try:
    # Ejecutamos yt-dlp para obtener el enlace de formato HLS directo (.m3u8)
    # Buscamos específicamente en la sección /live del canal
    result = subprocess.run(
        ["yt-dlp", "-g", f"{channel_url}/live"],
        capture_output=True,
        text=True,
        check=True
    )
    
    # yt-dlp nos devuelve la URL directa
    m3u8_url = result.stdout.strip()
    
    if m3u8_url and ".m3u8" in m3u8_url:
        print("¡Enlace .m3u8 extraído con éxito!")
        
        # Armamos el archivo M3U real que tu app IPTV va a poder leer
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{m3u8_url}\n"
        
        # Escribimos el archivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} guardado correctamente.")
    else:
        print("Error: No se pudo obtener un enlace .m3u8 válido.")

except Exception as e:
    print(f"Ocurrió un error al extraer el streaming: {e}")

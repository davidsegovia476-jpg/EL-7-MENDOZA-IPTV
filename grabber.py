import os
import subprocess
import re

channel_id = "UC64ZNqX0FQHabP8iIkmnR3A"
output_file = "canal7mendoza.m3u"

print("Instalando/Actualizando yt-dlp con parches de compatibilidad...")
# Instalamos la versión más reciente para evitar fallos de firmas de YouTube
subprocess.run(["pip", "install", "-U", "yt-dlp"], stdout=subprocess.DEVNULL)

print("Extrayendo el stream original .m3u8...")
try:
    # Usamos parámetros avanzados de yt-dlp para simular un reproductor móvil (Android/iOS)
    # Esto evita el 99% de los bloqueos anti-bot que hace YouTube en los servidores de GitHub
    live_url = f"https://www.youtube.com/channel/{channel_id}/live"
    result = subprocess.run(
        ["yt-dlp", "-g", "--extractor-args", "youtube:player_client=android", "--no-warnings", live_url],
        capture_output=True,
        text=True,
        check=True
    )
    
    m3u8_url = result.stdout.strip()
    
    if m3u8_url and (".m3u8" in m3u8_url or "manifest" in m3u8_url):
        print("¡Enlace nativo localizado con éxito!")
        
        # Estructura M3U oficial que cualquier aplicación IPTV puede reproducir al instante
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{m3u8_url}\n"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} actualizado de forma limpia.")
    else:
        print("Error: El servidor no devolvió una estructura .m3u8 compatible.")

except Exception as e:
    print(f"No se pudo extraer la transmisión. Motivo: {e}")


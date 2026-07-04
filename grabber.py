
import os
import requests
import re

# Configuración
channel_url = "https://www.youtube.com/watch?v=Vh8xmLBJtR8"
output_file = "canal7mendoza.m3u"

# Encabezado para simular un navegador web normal
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9"
}

print("Buscando la transmisión en vivo actual de Canal 7 Mendoza...")

try:
    # Forzamos a buscar en la sección /live del canal para ir directo al grano
    response = requests.get(f"{channel_url}/live", headers=headers, timeout=15)
    html_content = response.text

    # Buscamos el ID del video usando una expresión regular en el código de la página
    # YouTube suele guardar el ID del video actual en "videoDetails":{"videoId":"XXXXXXX"} o en las etiquetas canónicas
    video_id_match = re.search(r'"liveStreamability".*?"videoId":"([^"]+)"', html_content)
    
    if not video_id_match:
        # Intento de respaldo si el formato de la página cambió ligeramente
        video_id_match = re.search(r'href="https://youtube.com\?v=([^"]+)"', html_content)

    if video_id_match:
        video_id = video_id_match.group(1)
        # Creamos la URL limpia y directa de YouTube
        youtube_live_url = f"https://youtube.com?v={video_id}"
        print(f"¡Encontrado! Video ID actual: {video_id}")
        
        # Creamos el contenido del archivo M3U
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{youtube_live_url}\n"
        
        # Guardamos el archivo
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} actualizado correctamente.")
        
    else:
        print("No se pudo encontrar una transmisión en vivo activa en este momento.")

except Exception as e:
    print(f"Ocurrió un error al conectar con YouTube: {e}")

import os
import requests

# Configuración de rutas
info_file = "youtube_channel_info.txt"
output_file = "canal7mendoza.m3u"

# Encabezados para evitar bloqueos de YouTube
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

m3u_content = "#EXTM3U\n"

if os.path.exists(info_file):
    with open(info_file, "r") as f:
        url = f.read().strip()
    
    if url:
        try:
            # Buscar el stream en vivo en la página del canal
            response = requests.get(url, headers=headers, timeout=15)
            page_text = response.text
            
            # Buscar el token del directo (video_id)
            if 'videoDetails' in page_text or 'liveStreamability' in page_text:
                # Extraemos el ID del video usando una búsqueda simple de texto
                start_idx = page_text.find('/watch?v=')
                if start_idx != -1:
                    video_id = page_text[start_idx+9 : start_idx+20]
                    
                    # Estructura del enlace M3U8 genérico que procesan los reproductores
                    stream_url = f"https://www.youtube.com/watch?v={video_id}"
                    
                    # Si tu reproductor IPTV no soporta links directos de YouTube, 
                    # puedes usar el formato de pasarela m3u8 (común en servidores de IPTV):
                    # stream_url = f"https://vercel.app{stream_url}"

                    m3u_content += f'#EXTINF:-1 tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
                    m3u_content += f"{stream_url}\n"
                    print(f"Token/ID extraído exitosamente: {video_id}")
        except Exception as e:
            print(f"Error al procesar el canal: {e}")

# Guardar la lista M3U actualizada
with open(output_file, "w", encoding="utf-8") as out:
    out.write(m3u_content)

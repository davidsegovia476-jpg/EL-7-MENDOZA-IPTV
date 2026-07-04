import os
import requests

output_file = "canal7mendoza.m3u"
video_id = "Vh8xmLBJtR8"

print("Extrayendo el enlace nativo .m3u8 de YouTube...")

try:
    # Usamos un servidor proxy público que extrae la URL real de Google Video sin bloqueos
    proxy_url = f"https://vercel.app{video_id}"
    response = requests.get(proxy_url, timeout=15)
    m3u8_url = response.text.strip()

    # Si el proxy nos devuelve la URL correcta de Google, armamos el M3U
    if m3u8_url and "googlevideo.com" in m3u8_url:
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{m3u8_url}\n"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("¡Éxito! Archivo M3U creado con el enlace original de YouTube.")
    else:
        print("Error: El servidor no devolvió una URL de YouTube válida.")

except Exception as e:
    print(f"Error al extraer la transmisión: {e}")

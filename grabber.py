import os
import subprocess

# El archivo final para tu IPTV
output_file = "canal7mendoza.m3u"

# El ID fijo de la transmisión en vivo de Canal 7 Mendoza que descubrimos
video_id = "Vh8xmLBJtR8"

print("Instalando/Actualizando yt-dlp de forma silenciosa...")
# Instalamos la última versión de yt-dlp para tener los parches de YouTube al día
subprocess.run(["pip", "install", "-U", "yt-dlp"], stdout=subprocess.DEVNULL)

print("Extrayendo el enlace .m3u8 nativo de los servidores de Google Video...")

try:
    # Construimos la URL del directo
    live_url = f"https://youtube.com{video_id}"
    
    # Ejecutamos yt-dlp simulando un cliente Android para evitar bloqueos de IP
    result = subprocess.run(
        ["yt-dlp", "-g", "--extractor-args", "youtube:player_client=android", "--no-warnings", live_url],
        capture_output=True,
        text=True,
        check=True
    )
    
    # Capturamos la URL .m3u8 larga que nos devuelve
    m3u8_url = result.stdout.strip()
    
    if m3u8_url and ("googlevideo.com" in m3u8_url or ".m3u8" in m3u8_url):
        print("¡Enlace nativo extraído con éxito!")
        
        # Armamos el archivo M3U con la estructura correcta para tu app
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{m3u8_url}\n"
        
        # Guardamos el archivo físicamente en tu repositorio
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} actualizado correctamente.")
    else:
        print("Error: No se recibió una URL de Google Video válida.")

except Exception as e:
    print(f"Error crítico al extraer el streaming: {e}")


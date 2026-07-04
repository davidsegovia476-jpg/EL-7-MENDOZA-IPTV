import os
import subprocess

# Usamos el ID del canal directamente en lugar de la URL corta
channel_id = "UC64ZNqX0FQHabP8iIkmnR3A"
output_file = "canal7mendoza.m3u"

print("Actualizando yt-dlp...")
subprocess.run(["pip", "install", "-U", "yt-dlp"], stdout=subprocess.DEVNULL)

print("Extrayendo enlace .m3u8 en vivo mediante ID de canal...")
try:
    # URL directa de la transmisión en vivo basada en el ID del canal
    live_url = f"https://youtube.com{channel_id}/live"
    
    # Ejecutamos yt-dlp con parámetros optimizados para evitar bloqueos
    result = subprocess.run(
        ["yt-dlp", "-g", "--no-warnings", live_url],
        capture_output=True,
        text=True,
        check=True
    )
    
    m3u8_url = result.stdout.strip()
    
    # Validamos que obtuvimos un enlace de manifiesto válido
    if m3u8_url and ("manifest" in m3u8_url or ".m3u8" in m3u8_url):
        print("¡Enlace .m3u8 extraído con éxito!")
        
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{m3u8_url}\n"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} creado exitosamente.")
    else:
        print("YouTube no devolvió un enlace .m3u8 válido.")

except Exception as e:
    print(f"Error crítico al extraer el stream: {e}")


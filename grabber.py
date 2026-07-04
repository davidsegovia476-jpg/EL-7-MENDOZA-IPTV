import os

# El nombre del archivo final para tu IPTV
output_file = "canal7mendoza.m3u"

# El ID real que me diste del directo de Canal 7 Mendoza
video_id = "Vh8xmLBJtR8"

print("Generando lista M3U con la URL de YouTube corregida...")

try:
    # CORRECCIÓN: Agregamos la barra y el 'watch?v=' que faltaban
    youtube_url = f"https://youtube.com{video_id}"

    # Armamos el archivo M3U con el formato que tu reproductor necesita
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{youtube_url}\n"

    # Guardamos el archivo en tu repositorio
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! Archivo {output_file} creado con la URL correcta.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


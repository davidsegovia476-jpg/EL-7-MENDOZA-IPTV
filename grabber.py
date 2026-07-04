import os

# El nombre del archivo que leerá tu aplicación IPTV
output_file = "canal7mendoza.m3u"

# El ID fijo y real que nos pasaste del directo de Canal 7 Mendoza
video_id = "Vh8xmLBJtR8"

print("Generando lista M3U con la URL fija de YouTube...")

try:
    # Creamos la URL directa usando el ID permanente
    youtube_url = f"https://youtube.com{video_id}"

    # Armamos la estructura M3U limpia y correcta
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{youtube_url}\n"

    # Escribimos el archivo en el repositorio
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! El archivo {output_file} se ha creado correctamente.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


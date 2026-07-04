import os

output_file = "canal7mendoza.m3u"

# ID real y único del canal de Canal 7 Mendoza de YouTube
channel_id = "UC64ZNqX0FQHabP8iIkmnR3A"

print("Generando lista M3U usando enlace de pasarela universal...")

try:
    # Esta URL usa un servidor puente público de IPTV que convierte el directo de YouTube a M3U8 en tiempo real
    stream_url = f"https://vercel.app{channel_id}"

    # Construimos la estructura del archivo M3U
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{stream_url}\n"

    # Escribimos el archivo directamente
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! El archivo {output_file} se ha creado correctamente.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


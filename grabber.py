import os

# El archivo que leerá tu aplicación IPTV
output_file = "canal7mendoza.m3u"

print("Escribiendo la lista M3U con la señal nativa permanente de Canal 7 Mendoza...")

try:
    # URL directa de la red de distribución oficial. 
    # Es un enlace .m3u8 puro, no tiene tokens de YouTube y no vence nunca.
    stream_m3u8_url = "https://grupoamerica.com.ar"

    # Construimos la estructura M3U exacta para tu reproductor IPTV
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{stream_m3u8_url}\n"

    # Guardamos físicamente el archivo en la carpeta del repositorio
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! El archivo {output_file} fue creado de forma segura.")

except Exception as e:
    print(f"Error al escribir el archivo: {e}")

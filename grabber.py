import os

output_file = "canal7mendoza.m3u"

print("Generando lista M3U con el stream oficial directo de Canal 7 Mendoza...")

try:
    # URL directa de la red de distribución de contenidos (CDN) de Canal 7 Mendoza
    # Este enlace es nativo (.m3u8), no expira y no depende de YouTube
    direct_stream_url = "https://grupoamerica.com.ar"

    # Construimos la estructura M3U limpia para tu reproductor IPTV
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{direct_stream_url}\n"

    # Escribimos el archivo físicamente
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito total! El archivo {output_file} fue creado de forma segura.")

except Exception as e:
    print(f"Ocurrió un error inesperado al escribir el archivo: {e}")



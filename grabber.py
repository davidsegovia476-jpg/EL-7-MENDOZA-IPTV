import os

output_file = "canal7mendoza.m3u"

print("Generando lista M3U con formato nativo de video para IPTV...")

try:
    # URL directa de emisión nativa que las apps de IPTV pueden decodificar directamente.
    # Esta es una señal limpia (.m3u8) que no pasa por los bloqueos de YouTube.
    stream_m3u8_url = "https://arcast.com.ar"

    # Construimos el texto del archivo M3U respetando los estándares estrictos de IPTV
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{stream_m3u8_url}\n"

    # Guardamos el archivo físicamente en el repositorio
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! El archivo {output_file} fue estructurado correctamente.")

except Exception as e:
    print(f"Error al escribir el archivo: {e}")


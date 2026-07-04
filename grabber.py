import os
import requests

# La API oficial que descubriste en la página del canal
api_url = "https://www.elsietetv.com.ar/api/youtube.php?type=playlistItems&maxResults=50&playlistId=PLDedS24i-fT8JuyhhxozRV-VQlJvM3Wjn"
output_file = "canal7mendoza.m3u"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Consultando la API interna de El Siete TV...")

try:
    response = requests.get(api_url, headers=headers, timeout=15)
    data = response.json()
    
    # Buscamos el ID del video más reciente dentro de los items de la respuesta JSON
    if "items" in data and len(data["items"]) > 0:
        # El primer elemento de la lista suele ser el último directo o video subido
        first_item = data["items"][0]
        
        # Estructura típica del JSON de la API de YouTube v3
        video_id = first_item["snippet"]["resourceId"]["videoId"]
        youtube_url = f"https://www.youtube.com/watch?v={video_id}"
        
        print(f"¡Video localizado con éxito! ID: {video_id}")
        
        # Armamos el archivo M3U con el link directo para tu reproductor
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{youtube_url}\n"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} actualizado correctamente.")
        
    else:
        print("No se encontraron videos en la respuesta de la API.")

except Exception as e:
    # Intento de respaldo si la estructura cambia ligeramente
    print(f"Error al procesar la API: {e}")


import os
import requests

api_url = "https://elsietetv.com.ar"
output_file = "canal7mendoza.m3u"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Consultando la API de El Siete TV...")

try:
    response = requests.get(api_url, headers=headers, timeout=15)
    data = response.json()
    
    # Validamos que existan elementos en la respuesta
    if "items" in data and len(data["items"]) > 0:
        # CORRECCIÓN: Agregamos [0] para extraer SOLO el primer video (el más reciente)
        first_item = data["items"][0]
        
        # Extraemos el ID del video desde la estructura oficial del JSON
        video_id = first_item["snippet"]["resourceId"]["videoId"]
        youtube_url = f"https://youtube.com{video_id}"
        
        print(f"¡Video localizado con éxito! ID: {video_id}")
        
        # Armamos la lista M3U estructurada
        m3u_content = "#EXTM3U\n"
        m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
        m3u_content += f"{youtube_url}\n"
        
        # Guardamos el archivo final
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print(f"Archivo {output_file} guardado correctamente en la raíz.")
        
    else:
        print("La API no devolvió ningún video en este momento.")

except Exception as e:
    print(f"Error crítico al procesar los datos de la API: {e}")


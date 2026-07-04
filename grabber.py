
import os

# Nombre del archivo que leerá tu reproductor IPTV
output_file = "canal7mendoza.m3u"

print("Escribiendo la lista M3U con tu URL exacta de tracking...")

try:
    # Escribimos la URL completa de forma literal, exactamente igual a como me la pasaste
    url_exacta = "https://rr4---sn-uxax4vopj55gb-hq1e.googlevideo.com/videoplayback/id/Vh8xmLBJtR8.408/itag/96/source/yt_live_broadcast/expire/1783210946/ei/Yk9JapGeOOeaobIPru-GkAE/ip/2802:8012:402c:2b00:e5dc:89da:4d3c:b578/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/rqh/1/hls_chunk_host/rr4---sn-uxax4vopj55gb-hq1e.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/gcr/ar/bui/ARmQxEVTWC9YDVxA0wvnmlXk_IQhG6yrD8-U-6h-HwzH2WEIPssKV7nG0k1ASl_LOYmfrDMZB-4xCESG/spc/SQ-umliKOwbg7Is7ITV8orFAeQHqyutTnSdB77BQVhIqp3ql7A/vprv/1/reg/0/playlist_type/DVR/hcs/sd/initcwndbps/2060000/met/1783189348,/mh/Ha/mm/44/mn/sn-uxax4vopj55gb-hq1e/ms/lva/mv/m/mvi/4/pl/43/rmhost/rr1---sn-uxax4vopj55gb-hq1e.googlevideo.com/rms/lva,lva/keepalive/yes/fexp/51565115,52017146/mt/1783188980/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,rqh,xpc,gcr,bui,spc,vprv,reg,playlist_type/sig/AHEqNM4wRAIgSVii3OYCKY2WBq6aQWgwg4JiQj5of3_9zFEDQGVL3CACICdjs8Kwyvv8Oz8aDONZ2enXXOquokrw9_T5T3F0hX4t/lsparams/hls_chunk_host,hcs,initcwndbps,met,mh,mm,mn,ms,mv,mvi,pl,rmhost,rms/lsig/APaTxxMwRgIhAOjugTfbI3Z7nd5xC0N5UyC6OwYr1rWabWCcQbt6WGwfAiEAqTcm8DXpLwj00_goip-RZO1EKr0a8M9bgcuF33BNSaI%3D/playlist/index.m3u8/sq/2071010/goap/lmt%3D888/govp/lmt%3D888/dur/5.000/file/seg.ts"

    # Construimos el formato M3U estándar para tu aplicación IPTV
    m3u_content = "#EXTM3U\n"
    m3u_content += f'#EXTINF:-1 tvg-id="Canal7Mendoza" tvg-name="Canal 7 Mendoza" tvg-logo="https://elsietetv.com.ar" group-title="Mendoza",Canal 7 Mendoza\n'
    m3u_content += f"{url_exacta}\n"

    # Guardamos el archivo físicamente en tu repositorio
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(m3u_content)
        
    print(f"¡Éxito! Archivo {output_file} creado con tu URL exacta.")

except Exception as e:
    print(f"Ocurrió un error inesperado al escribir el archivo: {e}")

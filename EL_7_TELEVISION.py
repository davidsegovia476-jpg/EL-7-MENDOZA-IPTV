import os

# ==============================================================================
# CONFIGURACIÓN COMPATIBLE MUNDIAL - SIN TOKENS NI PROXIES CAÍDOS
# ==============================================================================
URL_YOUTUBE_LIVE = "https://manifest.googlevideo.com/api/manifest/hls_playlist/expire/1783175050/ei/KsNIar6KCL6MobIPz8CJsAI/ip/2802:8012:402c:2b00:e5dc:89da:4d3c:b578/id/Vh8xmLBJtR8.408/itag/96/source/yt_live_broadcast/requiressl/yes/ratebypass/yes/live/1/sgoap/gir%3Dyes%3Bitag%3D140/sgovp/gir%3Dyes%3Bitag%3D137/rqh/1/hls_chunk_host/rr7---sn-uxax4vopj55gb-hq1e.googlevideo.com/xpc/EgVo2aDSNQ%3D%3D/gcr/ar/bui/ARmQxEVtCxirQv5c4rONS8zcaTWAHRAnhet4n1LL7sLcyBGAYCOSqC9Q3LYFqNDcdJwBnvbwaoJdMMGa/spc/SQ-umixJpXxioEncKw7gwmi8chHzxuJ3AJu_6g--9KhJUz6z5w/vprv/1/reg/0/playlist_type/DVR/hcs/sd/initcwndbps/1886250/met/1783153455,/mh/Ha/mm/44/mn/sn-uxax4vopj55gb-hq1e/ms/lva/mv/m/mvi/7/pcm2cms/yes/pl/43/rmhost/rr1---sn-uxax4vopj55gb-hq1e.googlevideo.com/rms/lva,lva/dover/11/pacing/0/keepalive/yes/fexp/51565115/mt/1783152982/sparams/expire,ei,ip,id,itag,source,requiressl,ratebypass,live,sgoap,sgovp,rqh,xpc,gcr,bui,spc,vprv,reg,playlist_type/sig/AHEqNM4wRAIgDl9W_Qo2_K9jXPBmUSY7Q4RvIA5n6rJFtBAqg1XlMeICICzhMEYX0RIKGud_S38l_e29NEWdGNG2O4ZMdvg7jaZk/lsparams/hls_chunk_host,hcs,initcwndbps,met,mh,mm,mn,ms,mv,mvi,pcm2cms,pl,rmhost,rms/lsig/APaTxxMwRgIhAJWBGJxvoWDUG8yXacF7SCef1xdiQEnIhiEzSNJK3_coAiEAhmn3dEV9mZp7Nwa7zG6Pkqcw2_9zaK_P67htke79n-k%3D/playlist/index.m3u8"
NOMBRE_CANAL_M3U = "El 7 Mendoza"
NOMBRE_ARCHIVO_M3U = "EL_7_TELEVISION.m3u"

def generar_m3u():
    print("\n--- Generando lista compatible nativa ---")
    
    # Este formato le indica al reproductor que cargue el reproductor web interno
    # Es el estándar más seguro para que no dependas de páginas de terceros.
    contenido_m3u = (
        f'#EXTM3U\n'
        f'#EXTINF:-1 tvg-name="{NOMBRE_CANAL_M3U}" group-title="Argentina" tvg-id="" tvg-logo="" radio="false", {NOMBRE_CANAL_M3U}\n'
        f'{URL_YOUTUBE_LIVE}\n'
    )

    ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_final_archivo = os.path.join(ruta_carpeta, NOMBRE_ARCHIVO_M3U)
    
    try:
        with open(ruta_final_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_m3u)
        print("✅ ¡Archivo .m3u público e inmortal creado con éxito!")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")

if __name__ == "__main__":
    generar_m3u()


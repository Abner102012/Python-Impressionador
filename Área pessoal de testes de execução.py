from dic import dicionario_vimeo
from pprint import pprint

info = dicionario_vimeo["data"]

for item in info:
    video_uri = item["uri"]
    nome = item["name"]
    duracao = item["duration"]
    pprint(video_uri)
    link_540p = ""
    link_720p = ""
    link_1080p = ""
    lista_downloads = item["download"]
    for dicionario_download in lista_downloads:
        if dicionario_download["rendition"] == "540p":
            link_540p = dicionario_download["link"]
        elif dicionario_download["rendition"] == "720p":
            link_720p = dicionario_download["link"]
        elif dicionario_download["rendition"] == "1080p":
            link_1080p = dicionario_download["link"]
    dic_item = {'uri': video_uri, 'nome': nome, 'duracao': duracao, 'link540p': link_540p, 'link720p': link_720p, 'link1080p': link_1080p},
    Video.append(dic_item)
    print(video_uri, nome, duracao)
    print(link_540p)
    print(link_720p)
    print(link_1080p)
print(Video)

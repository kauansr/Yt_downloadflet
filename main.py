import flet as ft
from pytube import YouTube, Playlist
import os

def main(page: ft.Page):

    page.title = 'Youtube downloader'
    page.window_maximized = True
    page.add(ft.Text('Youtube dowloader', size=30, color='green'))


    def get_yt_downloader_audio(e):
        url = tf1.value
        ytb = YouTube(url)
        audio = ytb.streams.get_audio_only()
        audio_downl = audio.download("downloads/audios")
        base, ext = os.path.splitext(audio_downl)
        novo_arquivo = base + '.mp3'
        os.rename(audio_downl, novo_arquivo)
        t.value = f'Baixado audio {novo_arquivo}'

        page.update()

        


    def get_yt_downloader_video(e):
        url = tf1.value
        ytb = YouTube(url)
        audio = ytb.streams.get_highest_resolution()
        audio_downl = audio.download("downloads/video")
        base, ext = os.path.splitext(audio_downl)
        novo_arquivo = base + '.mp4'
        os.rename(audio_downl, novo_arquivo)
        t.value = f'Baixado video {novo_arquivo}'

        page.update()

    def get_yt_downloader_audio_playlist(e):
        url = tf1.value
        yt = Playlist(url)
        for musicas in yt.video_urls:
                ys = YouTube(musicas)
                print('Titulo:', ys.title, 'Baixando...')
                musica = ys.streams.get_audio_only()
                baixa = musica.download(
                    output_path="downloads/playlist/audios")
                base, ext = os.path.splitext(baixa)
                novo_arquivo = base + '.mp3'
                os.rename(baixa, novo_arquivo)

                t.value = f'Baixado playlist audio {novo_arquivo}'
                
        t.value = f'Baixado audios da playlist'
        
        page.update()


    def get_yt_downloader_video_playlist(e):
        url = tf1.value
        yt = Playlist(url)

        for videos in yt.video_urls:
            ys = YouTube(videos)
            print('Titulo:', ys.title, 'Baixando...')
            video = ys.streams.get_highest_resolution()
            baixa = video.download(
                output_path="downloads/playlist/videos")
            t.value = f'Baixado playlist video {ys.title}'

        t.value = f'Baixado videos playlist'

        page.update()    

    t = ft.Text()
    tf1 = ft.TextField(label='Digite o link de video ou playlist')

    butons = ft.ResponsiveRow([
        ft.ElevatedButton(text='Audio', col={"sm": 6}, on_click=get_yt_downloader_audio),
        ft.ElevatedButton(text='Video', col={"sm": 6}, on_click=get_yt_downloader_video),
        ft.ElevatedButton(text='Playlist video', col={"sm": 6}, on_click=get_yt_downloader_video_playlist),
        ft.ElevatedButton(text='Playlist audio', col={"sm": 6}, on_click=get_yt_downloader_audio_playlist)
    ]
    )


    page.add(tf1, butons, t)

    
ft.app(target=main)
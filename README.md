# Organizador de Arquivos

Este script Python organiza os arquivos em um diretório específico com base em suas extensões.


## Como executar

vá na pasta dist e execute o organizar.exe
em seguida uma pequena janela vai abrir e lá você clica no botao e seleciona o diretório a ser organizado

## Como funciona

O script define um dicionário de extensões de arquivo para categorias. Cada chave no dicionário é uma extensão de arquivo e o valor correspondente é a categoria do arquivo. Aqui estão algumas das categorias definidas:

- Imagens: jpeg, jpg, png, ico, gif, svg
- SQL: sql
- Executáveis: exe, msi
- PDF: pdf
- Excel: xlsx, csv
- Arquivos compactados: rar, zip, gz, tar
- Word: docx
- Torrent: torrent
- Texto: txt
- Python: ipynb, py
- PowerPoint: pptx, ppt
- Áudio: mp3, wav
- Vídeo: mp4, m3u8, webm, ts
- JSON: json
- Web: css, js, html

## Como usar

se quiser adicionar algum tipo de extensão, vá até o dicionario extensions e adicione o formato de arquivo e para qual pasta ele deve ir

para criar uma nova build execute o seguinte comando

pyinstaller --onefile organizar.py

## Caso queria ajudar

faça uma interface melhor para o programa (não sei usar o tkinter direito)
adicione novos tipos de arquivos ou separe melhor as pastas

import os
import glob
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import filedialog

def organizar(path: str):
    extensions = {
        "jpeg": "imagens",
        "jpg": "imagens",
        "png": "imagens",
        "ico": "imagens",
        "gif": "imagens",
        "svg": "imagens",
        "sql": "sql",
        "exe": "exe",
        "msi": "exe",
        "pdf": "pdf",
        "xlsx": "excel",
        "csv": "excel",
        "rar": "arquivo",
        "zip": "arquivo",
        "gz": "arquivo",
        "tar": "arquivo",
        "docx": "palavra",
        "torrent": "torrent",
        "txt": "txt",
        "ipynb": "python",
        "py": "python",
        "pptx": "powerpoint",
        "ppt": "powerpoint",
        "mp3": "audio",
        "wav": "áudio",
        "mp4": "vídeo",
        "m3u8": "vídeo",
        "webm": "vídeo",
        "ts": "vídeo",
        "json": "json",
        "css": "web",
        "js": "web",
        "html": "web",
        "apk": "apk",
        "sqlite3": "sqlite3",
        "jar": "modMinecraft",
        "bmp":"imagens",
    }
        
    for extension, folder_name in extensions.items():
        # Pega todos os arquivos que terminam com a extensão
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        print(f"[*] Encontrados {len(files)} corquivos com extensão '{extension}'")
        
        if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # Cria a pasta se não existir
            print(f"[+] Making {folder_name} folder")
            os.mkdir(os.path.join(path, folder_name))
            
        for file in files:
            # Para cada arquivo, move para a pasta correspondente
            basename = os.path.basename(file)
            dst = os.path.join(path, folder_name, basename)
            print(f"[*] Movendo {file} para {dst}")
            shutil.move(file, dst)

def select_directory():
    directory = filedialog.askdirectory()
    print(f"Selected directory: {directory}")
    organizar(directory)

root = tk.Tk()
button = tk.Button(root, text="Select Directory", command=select_directory)
button.pack()

root.mainloop()
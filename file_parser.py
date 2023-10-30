import sys
from pathlib import Path
import re

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []

DOC = []
DOCX = []
TXT = []
PDF = []
XLSX = []
PPTX = []

MP3_AUDIOS = []
OGG_AUDIOS = []
WAV_AUDIOS = []
AMR_AUDIOS = []

ZIP_ARCHIVES = []
GZ_ARCHIVES = []
RAR_ARCHIVES = []

OTHER = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,
    'DOC': DOC,
    'DOCX': DOCX,
    'TXT': TXT,
    'PDF': PDF,
    'XLSX': XLSX,
    'PPTX': PPTX,
    'MP3': MP3_AUDIOS,
    'OGG': OGG_AUDIOS,
    'WAV': WAV_AUDIOS,
    'AMR': AMR_AUDIOS,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'RAR': RAR_ARCHIVES,
    'OTHER': OTHER,   
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()  

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():  
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        extension = get_extension(item.name)
        full_name = folder / item.name
        print(full_name)
        if not extension:
            OTHER.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)  
                OTHER.append(full_name)

if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'AUDIO mp3: {MP3_AUDIOS}')
    print(f'Archives zip: {ZIP_ARCHIVES}')

    print(f'EXTENSIONS: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
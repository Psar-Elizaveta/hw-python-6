from pathlib import Path
import shutil
import sys
import file_parser
from normalize import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()

def main(folder: Path):
    file_parser.scan(folder)
    for file in file_parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in file_parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in file_parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in file_parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in file_parser.MP3_AUDIOS:
        handle_media(file, folder / 'audio' / 'MP3_AUDIOS')
    for file in file_parser.OGG_AUDIOS:
        handle_media(file, folder / 'audio' / 'OGG_AUDIOS')
    for file in file_parser.WAV_AUDIOS:
        handle_media(file, folder / 'audio' / 'WAV_AUDIOS')
    for file in file_parser.AMR_AUDIOS:
        handle_media(file, folder / 'audio' / 'AMR_AUDIOS')
    for file in file_parser.AVI_VIDEOS:
        handle_media(file, folder / 'audio' / 'AVI_VIDEOS')
    for file in file_parser.MP4_VIDEOS:
        handle_media(file, folder / 'audio' / 'MP4_VIDEOS')
    for file in file_parser.MOV_VIDEOS:
        handle_media(file, folder / 'audio' / 'MOV_VIDEOS')
    for file in file_parser.MKV_VIDEOS:
        handle_media(file, folder / 'audio' / 'MKV_VIDEOS')
    for file in file_parser.DOC:
        handle_media(file, folder / 'audio' / 'DOC')
    for file in file_parser.DOCX:
        handle_media(file, folder / 'audio' / 'DOCX')
    for file in file_parser.TXT:
        handle_media(file, folder / 'audio' / 'TXT')
    for file in file_parser.PDF:
        handle_media(file, folder / 'audio' / 'PDF')
    for file in file_parser.XLSX:
        handle_media(file, folder / 'audio' / 'XLSX')
    for file in file_parser.PPTX:
        handle_media(file, folder / 'audio' / 'PPTX')
    for file in file_parser.RAR_ARCHIVES:
        handle_media(file, folder / 'audio' / 'RAR_ARCHIVES')
    for file in file_parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'ZIP_ARCHIVES')
    for file in file_parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'GZ_ARCHIVES')
    for file in file_parser.OTHER:
        handle_media(file, folder / 'OTHER')
    for folder in file_parser.FOLDERS[::-1]:
        try:
            folder.rmdir()
        except OSError:
            print(f'Error during remove folder {folder}')

if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())
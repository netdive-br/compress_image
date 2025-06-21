import os
import sys
from pillow_heif import register_heif_opener
from PIL import Image

# Ativa suporte a HEIC
register_heif_opener()

def converter_heic_para_jpeg(pasta_origem):
    if not os.path.isdir(pasta_origem):
        print(f"Erro: pasta não encontrada -> {pasta_origem}")
        return

    arquivos_convertidos = 0

    for arquivo in os.listdir(pasta_origem):
        if arquivo.lower().endswith((".heic", ".heif")):
            caminho_heic = os.path.join(pasta_origem, arquivo)
            nome_base = os.path.splitext(arquivo)[0]
            caminho_jpeg = os.path.join(pasta_origem, nome_base + ".jpg")

            try:
                imagem = Image.open(caminho_heic).convert("RGB")
                imagem.save(caminho_jpeg, "JPEG", quality=95, optimize=True)
                print(f"✔ Convertido: {arquivo} -> {nome_base}.jpg")
                arquivos_convertidos += 1
            except Exception as e:
                print(f"❌ Falha ao converter {arquivo}: {e}")

    if arquivos_convertidos == 0:
        print("Nenhum arquivo .heic encontrado.")
    else:
        print(f"\nTotal convertido: {arquivos_convertidos} arquivo(s)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convert_heic_jpeg.py /caminho/para/as/imagens")
    else:
        pasta = sys.argv[1]
        converter_heic_para_jpeg(pasta)

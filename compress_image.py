import os
import sys
import hashlib
import shutil
import tinify
from tqdm import tqdm
from dotenv import load_dotenv

# 🔒 Carrega a chave da API do arquivo .env
load_dotenv()
TINIFY_API_KEY = os.getenv("TINIFY_API_KEY")

if not TINIFY_API_KEY:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

tinify.key = TINIFY_API_KEY


def calcular_hash(caminho):
    """Calcula hash SHA256 do conteúdo do arquivo."""
    h = hashlib.sha256()
    with open(caminho, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def adicionar_sufixo_web(nome_arquivo):
    """Adiciona sufixo '_web' antes da extensão."""
    nome, ext = os.path.splitext(nome_arquivo)
    return f"{nome}_web{ext}"


def comprimir_imagens(pasta_origem):
    pasta_web = os.path.join(pasta_origem, "WEB")
    os.makedirs(pasta_web, exist_ok=True)

    extensoes = (".jpg", ".jpeg", ".png")
    arquivos = sorted([
    f for f in os.listdir(pasta_origem)
    if f.lower().endswith(extensoes) and os.path.isfile(os.path.join(pasta_origem, f))
    ])


    if not arquivos:
        print("Nenhuma imagem encontrada para compressão.")
        return

    hashes = {}

    total_economia = 0
    total_original = 0
    total_final = 0

    print(f"\n🔧 Iniciando compressão de {len(arquivos)} imagens na pasta: {pasta_origem}\n")
    for arquivo in tqdm(arquivos, desc="Comprimindo imagens", unit="img"):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        nome_comprimido = adicionar_sufixo_web(arquivo)
        destino = os.path.join(pasta_web, nome_comprimido)

        try:
            tamanho_original = os.path.getsize(caminho_arquivo)
            hash_img = calcular_hash(caminho_arquivo)

            if hash_img in hashes:
                imagem_base = hashes[hash_img]
                origem = os.path.join(pasta_web, imagem_base)
                shutil.copyfile(origem, destino)
                tamanho_comprimido = os.path.getsize(destino)
                tqdm.write(f"🔁 {arquivo} é duplicata — copiado como {nome_comprimido}.")
            else:
                source = tinify.from_file(caminho_arquivo)
                source.to_file(destino)
                tamanho_comprimido = os.path.getsize(destino)
                hashes[hash_img] = nome_comprimido

            economia = tamanho_original - tamanho_comprimido
            total_economia += economia
            total_original += tamanho_original
            total_final += tamanho_comprimido

            tqdm.write(
                f"📉 {arquivo}: {tamanho_original / 1024:.1f} KB → {tamanho_comprimido / 1024:.1f} KB "
                f"(economia: {economia / 1024:.1f} KB)"
            )

        except tinify.errors.AccountError:
            print("\n❌ Erro: chave da API inválida ou limite excedido.")
            break
        except tinify.errors.ClientError as e:
            print(f"\n⚠️ Erro no arquivo {arquivo}: {e}")
        except Exception as e:
            print(f"\n⚠️ Erro inesperado no arquivo {arquivo}: {e}")

    print(f"\n✅ Compressão concluída! Arquivos otimizados salvos em: {pasta_web}")
    print(f"\n📊 Tamanho total original: {total_original / 1024:.1f} KB")
    print(f"📦 Tamanho total comprimido: {total_final / 1024:.1f} KB")
    print(f"💰 Economia total: {total_economia / 1024:.1f} KB "
          f"({(total_economia / total_original * 100):.1f}% de redução)")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pasta = sys.argv[1]
    else:
        pasta = input("Digite o caminho da pasta com as imagens: ").strip()

    if os.path.isdir(pasta):
        comprimir_imagens(pasta)
    else:
        print("❌ Pasta inválida. Verifique o caminho informado.")

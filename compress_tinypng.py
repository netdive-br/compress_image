import os
import tinify
from tqdm import tqdm
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()
TINIFY_API_KEY = os.getenv("TINIFY_API_KEY")

if not TINIFY_API_KEY:
    raise ValueError("A chave da API não foi encontrada. Verifique o arquivo .env.")

# Define a chave da API no Tinify
tinify.key = TINIFY_API_KEY


def comprimir_imagens(pasta_origem):
    pasta_web = os.path.join(pasta_origem, "WEB")
    os.makedirs(pasta_web, exist_ok=True)

    extensoes_validas = (".jpg", ".jpeg", ".png")

    arquivos = [
        f
        for f in os.listdir(pasta_origem)
        if f.lower().endswith(extensoes_validas)
        and os.path.isfile(os.path.join(pasta_origem, f))
    ]

    if not arquivos:
        print("Nenhuma imagem encontrada para compressão.")
        return

    print(f"Iniciando compressão de {len(arquivos)} imagens...\n")

    for arquivo in tqdm(arquivos, desc="Comprimindo imagens", unit="img"):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(pasta_web, arquivo)

        try:
            source = tinify.from_file(caminho_arquivo)
            source.to_file(destino)
        except tinify.errors.AccountError:
            print("⚠️ Erro: chave da API inválida ou limite excedido.")
            break
        except tinify.errors.ClientError:
            print(
                f"⚠️ Erro no arquivo {arquivo}: formato inválido ou imagem corrompida."
            )
        except Exception as e:
            print(f"⚠️ Erro inesperado com {arquivo}: {e}")

    print("\n✅ Compressão finalizada.")


if __name__ == "__main__":
    pasta = input("Digite o caminho da pasta com as imagens: ").strip()
    if os.path.isdir(pasta):
        comprimir_imagens(pasta)
    else:
        print("Pasta inválida.")

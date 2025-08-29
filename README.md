# 🖼️ Compress Image - Otimizador de Imagens com TinyPNG

Este projeto é um script em **Python** para **compressão automática de imagens** (JPG e PNG) utilizando a API do [TinyPNG](https://tinypng.com/developers).
Ele otimiza imagens em lote, evita duplicatas através de **hash SHA256** e organiza os arquivos comprimidos em uma pasta separada.

---

## 🚀 Funcionalidades

* 🔧 Compressão de imagens em lote (JPG/JPEG/PNG)
* 📉 Redução de tamanho mantendo a qualidade
* 🔁 Detecção de imagens duplicadas para evitar compressão repetida
* 📂 Criação automática da pasta `WEB` para armazenar imagens otimizadas
* 📊 Relatório final com economia total de espaço

---

## 📦 Requisitos

* Python **3.8+**
* Conta na [API do TinyPNG](https://tinypng.com/developers) (plano gratuito inclui **500 compressões por mês**)

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/compress-image.git
cd compress-image

# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 📑 Arquivo `requirements.txt`

Se ainda não existir, crie um arquivo com o seguinte conteúdo:

```
tinify
tqdm
python-dotenv
```

---

## 🔑 Configuração da API

Crie um arquivo **`.env`** na raiz do projeto com sua chave da API do TinyPNG:

```
TINIFY_API_KEY=SUACHAVEAQUI
```

> ⚠️ **Importante:** nunca compartilhe sua chave da API em repositórios públicos.

---

## ▶️ Uso

### 1. Executar diretamente

```bash
python compress_image.py /caminho/para/sua/pasta
```

### 2. Caso não informe o caminho

O programa pedirá que você digite manualmente o caminho da pasta com imagens.

---

## 📂 Estrutura do resultado

Supondo que sua pasta seja `imagens/`, após a execução será criada:

```
imagens/
│── foto1.jpg
│── foto2.png
│── ...
│── WEB/
    ├── foto1_web.jpg
    ├── foto2_web.png
```

---

## 📊 Exemplo de saída

```
🔧 Iniciando compressão de 3 imagens na pasta: imagens/

📉 foto1.jpg: 2,345.0 KB → 789.2 KB (economia: 1,555.8 KB)
🔁 foto2.png é duplicata — copiado como foto2_web.png.
📉 foto3.jpg: 1,200.0 KB → 450.3 KB (economia: 749.7 KB)

✅ Compressão concluída! Arquivos otimizados salvos em: imagens/WEB

📊 Tamanho total original: 3,545.0 KB
📦 Tamanho total comprimido: 1,239.5 KB
💰 Economia total: 2,305.5 KB (65.0% de redução)
```

---

## ⚠️ Possíveis erros

* **❌ Erro: chave da API inválida ou limite excedido.**
  → Verifique sua chave no `.env` ou se já atingiu o limite de compressões gratuitas.

* **⚠️ Erro no arquivo X:**
  → Pode indicar formato não suportado ou arquivo corrompido.

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**.
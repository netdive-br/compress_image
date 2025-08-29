# 🖼️ Image Tools - Conversão e Compressão de Imagens

Este repositório contém dois utilitários em **Python** para tratamento de imagens:

1. **Conversão HEIC → JPEG** (`convert_heic_jpeg.py`)

   * Ideal para usuários de iPhone/Apple que recebem fotos em formato **HEIC/HEIF**.

2. **Compressão JPEG/PNG com TinyPNG** (`compress_image.py`)

   * Otimiza imagens, reduzindo o tamanho dos arquivos sem perda significativa de qualidade.

---

## 🚀 Funcionalidades

### `convert_heic_jpeg.py`

* Converte imagens **.heic / .heif** para **.jpg**
* Mantém boa qualidade (95%)
* Otimiza o arquivo final
* Salva o `.jpg` na mesma pasta da imagem original

### `compress_image.py`

* Comprime imagens **JPG/JPEG/PNG** usando a API do [TinyPNG](https://tinypng.com/developers)
* Evita compressão repetida de imagens duplicadas (usa hash SHA256)
* Cria uma pasta `WEB/` para armazenar os arquivos otimizados
* Gera relatório com estatísticas de economia de espaço

---

## 📦 Requisitos

* Python **3.8+**
* Dependências listadas em `requirements.txt`

```
pillow==11.2.1
pillow_heif==0.22.0
python-dotenv==1.1.0
tinify==1.7.0
tqdm==4.67.1
```

> 🔎 Obs: Dependências como `requests`, `certifi` etc. são instaladas automaticamente, não precisam ser listadas manualmente.

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/image-tools.git
cd image-tools

# Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Instalar dependências
pip install -r requirements.txt
```

---

## 🔑 Como obter a chave da API do TinyPNG

1. Acesse [https://tinypng.com/developers](https://tinypng.com/developers).
2. Clique em **Get your API key**.
3. Cadastre-se com um e-mail válido.
4. Você receberá sua chave de API (algo como `qJ3F4xAbCdEfGhIjKlMnOpQrStUvWxYz`).
5. O plano gratuito permite **até 500 compressões por mês**.

Crie um arquivo **`.env`** na raiz do projeto com a chave:

```
TINIFY_API_KEY=SUACHAVEAQUI
```

---

## ▶️ Uso

### 1. Conversor HEIC → JPEG

```bash
python convert_heic_jpeg.py /caminho/para/as/imagens
```

📂 Estrutura antes/depois:

```
imagens/
│── foto1.heic
│── foto2.heic
```

⬇️ Após conversão:

```
imagens/
│── foto1.heic
│── foto1.jpg
│── foto2.heic
│── foto2.jpg
```

---

### 2. Compressor de Imagens (TinyPNG)

```bash
python compress_image.py /caminho/para/as/imagens
```

📂 Estrutura antes:

```
imagens/
│── foto1.jpg
│── foto2.png
```

⬇️ Após compressão:

```
imagens/
│── foto1.jpg
│── foto2.png
│── WEB/
    ├── foto1_web.jpg
    ├── foto2_web.png
```

---

## 📊 Exemplo de saída do compressor

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

* **`❌ Erro: chave da API inválida ou limite excedido`**
  → Verifique sua chave no `.env` ou se já atingiu o limite gratuito de 500 imagens/mês.

* **`❌ Falha ao converter arquivo.heic`**
  → Pode indicar arquivo corrompido ou incompatível.

* **`Nenhuma imagem encontrada`**
  → Verifique se a pasta contém arquivos suportados.

---

## 📜 Licença

Este projeto é distribuído sob a licença **MIT**.

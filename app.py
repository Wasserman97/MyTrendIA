import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import os
import random  # Usado para simular a previsão do tempo

# Diretórios das imagens e vídeos
IMAGENS_DIR = "images/"
VIDEOS_DIR = "videos/"

# Tamanho das imagens (quando carregadas)
IMAGE_WIDTH = 250
IMAGE_HEIGHT = 250

# Tamanho inicial das labels (placeholders)
PLACEHOLDER_WIDTH = 20  # Em número de caracteres (não pixels)
PLACEHOLDER_HEIGHT = 10  # Em número de linhas (não pixels)

# Guarda-roupa virtual: Lista de peças que o usuário possui
guarda_roupa = {
    "calças": ["jeans escura", "calça bege", "calça preta"],
    "sapatos": ["tênis branco", "sapatos marrons", "tênis de cano alto"],
    "jaquetas": ["jaqueta preta", "jaqueta jeans"],
}


# Função para verificar se o arquivo existe
def verificar_arquivo(caminho):
    if not os.path.exists(caminho):
        messagebox.showerror("Erro", f"Arquivo não encontrado: {caminho}")
        return False
    return True


# Simulação de previsão do tempo (frio ou calor)
def previsao_tempo():
    clima = random.choice(["frio", "calor"])
    return clima


# Função para fornecer conselhos com base na camiseta selecionada
def conselho_ia(cor):
    clima = previsao_tempo()  # Simula a previsão do tempo

    if cor == "Amarela":
        if clima == "frio":
            conselho = (
                "Hoje está frio. Recomendo uma calça jeans escura e uma jaqueta preta. "
                "Você tem essas peças no seu guarda-roupa. Um tênis branco seria ideal."
            )
        else:
            conselho = (
                "Hoje está calor. Uma calça jeans escura e tênis branco ficariam ótimos. "
                "Você já tem essas peças no guarda-roupa. Aproveite o clima para ficar confortável!"
            )
    elif cor == "Azul":
        if clima == "frio":
            conselho = (
                "Está frio hoje. Combine a camiseta azul com uma calça bege e sapatos marrons. "
                "Você já tem essas peças no guarda-roupa, e uma jaqueta jeans seria perfeita."
            )
        else:
            conselho = (
                "Com o calor de hoje, sugiro calça bege e sapatos marrons para um estilo moderno. "
                "Se precisar de uma jaqueta leve, considere uma compra na Zara ou Riachuelo."
            )
    elif cor == "Vermelha":
        if clima == "frio":
            conselho = (
                "Está frio hoje. Tente uma jaqueta preta e calça jeans rasgada para um look ousado. "
                "Você tem a jaqueta no guarda-roupa, mas a calça rasgada pode ser encontrada na Zara."
            )
        else:
            conselho = (
                "Com o calor de hoje, sugiro calça jeans rasgada e tênis de cano alto. "
                "A calça você pode comprar na Riachuelo, se não a tiver."
            )
    elif cor == "Branca com manga preta":
        if clima == "frio":
            conselho = (
                "Hoje está frio. Sugiro calça preta e tênis de cano alto para um visual esportivo. "
                "Você já tem essas peças no guarda-roupa."
            )
        else:
            conselho = (
                "Está calor hoje. Uma calça preta e tênis de cano alto ficarão ótimos. "
                "Se quiser completar com um boné, recomendo conferir na Riachuelo."
            )
    else:
        conselho = "Escolha uma camiseta para receber conselhos de moda."

    # Atualiza o texto na label de conselho
    label_conselho.config(text=conselho)


# Função para reproduzir vídeos usando OpenCV
def reproduzir_video(caminho_video):
    if verificar_arquivo(caminho_video):
        cap = cv2.VideoCapture(caminho_video)
        if not cap.isOpened():
            messagebox.showerror("Erro", "Erro ao abrir o vídeo.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow("Vídeo", frame)

            # Pressione 'q' ou feche a janela para encerrar o vídeo
            if (
                cv2.waitKey(25) & 0xFF == ord("q")
                or cv2.getWindowProperty("Vídeo", cv2.WND_PROP_VISIBLE) < 1
            ):
                break

        cap.release()
        cv2.destroyAllWindows()


# Função para carregar e exibir imagens com redimensionamento
def mostrar_imagem(label, caminho_imagem):
    print(f"Tentando abrir a imagem: {caminho_imagem}")
    if verificar_arquivo(caminho_imagem):
        try:
            imagem = Image.open(caminho_imagem)
            # Redimensionar a imagem para o tamanho correto
            imagem = imagem.resize(
                (IMAGE_WIDTH, IMAGE_HEIGHT), Image.Resampling.LANCZOS
            )
            imagem_tk = ImageTk.PhotoImage(imagem)
            label.config(
                image=imagem_tk, width=IMAGE_WIDTH, height=IMAGE_HEIGHT
            )  # Ajusta o tamanho da label
            label.image = imagem_tk  # Mantenha a referência da imagem
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir a imagem: {e}")
    else:
        print(f"Arquivo {caminho_imagem} não encontrado!")


# Função para atualizar as imagens de acordo com a camiseta selecionada
def selecionar_camisa(cor):
    limpar_imagens()  # Limpa as imagens antes de carregar novas
    # Exibe as imagens primeiro
    if cor == "Amarela":
        mostrar_imagem(img_label_frente, os.path.join(IMAGENS_DIR, "amarelaFre.jpeg"))
        mostrar_imagem(img_label_costas, os.path.join(IMAGENS_DIR, "amarelaCos.jpeg"))
        mostrar_imagem(img_label_lado, os.path.join(IMAGENS_DIR, "amarelaDir.jpeg"))
    elif cor == "Azul":
        mostrar_imagem(img_label_frente, os.path.join(IMAGENS_DIR, "azulFre.jpeg"))
        mostrar_imagem(img_label_costas, os.path.join(IMAGENS_DIR, "azulEsq.jpeg"))
        mostrar_imagem(img_label_lado, os.path.join(IMAGENS_DIR, "azulDir.jpeg"))
    elif cor == "Vermelha":
        mostrar_imagem(img_label_frente, os.path.join(IMAGENS_DIR, "verFre.jpeg"))
        mostrar_imagem(img_label_costas, os.path.join(IMAGENS_DIR, "verCos.jpeg"))
        mostrar_imagem(img_label_lado, os.path.join(IMAGENS_DIR, "verDir.jpeg"))
    elif cor == "Branca com manga preta":
        mostrar_imagem(img_label_frente, os.path.join(IMAGENS_DIR, "brancaFre.jpeg"))
        mostrar_imagem(img_label_costas, os.path.join(IMAGENS_DIR, "brancaCos.jpeg"))
        mostrar_imagem(img_label_lado, os.path.join(IMAGENS_DIR, "brancaDir.jpeg"))
    else:
        messagebox.showerror("Erro", "Camiseta não encontrada.")

    # Atualiza o conselho de moda baseado na escolha da camiseta
    conselho_ia(cor)


# Função para reproduzir vídeo da camiseta selecionada
def ver_video(cor):
    if cor == "Amarela":
        reproduzir_video(os.path.join(VIDEOS_DIR, "amarelaVid.mp4"))
    elif cor == "Azul":
        reproduzir_video(os.path.join(VIDEOS_DIR, "azulVid.mp4"))
    elif cor == "Branca com manga preta":
        reproduzir_video(os.path.join(VIDEOS_DIR, "VidBrPr.mp4"))
    else:
        messagebox.showerror("Erro", "Vídeo não encontrado.")


# Função para limpar as imagens quando uma nova camiseta for selecionada
def limpar_imagens():
    img_label_frente.config(
        image="", text="Frente", width=PLACEHOLDER_WIDTH, height=PLACEHOLDER_HEIGHT
    )
    img_label_costas.config(
        image="", text="Costas", width=PLACEHOLDER_WIDTH, height=PLACEHOLDER_HEIGHT
    )
    img_label_lado.config(
        image="", text="Lado", width=PLACEHOLDER_WIDTH, height=PLACEHOLDER_HEIGHT
    )


# Configuração da interface principal
janela = tk.Tk()
janela.title("MyTrendIA - Simulação de Camisetas")
janela.geometry("950x750")
janela.config(bg="#2C3E50")  # Cor de fundo da janela

# Título do aplicativo com estilo
titulo = tk.Label(
    janela,
    text="MyTrendIA",
    font=("Helvetica", 36, "bold italic"),
    bg="#8E44AD",  # Roxo vibrante
    fg="white",
    relief="raised",
    padx=10,
    pady=10,
)
titulo.pack(pady=20)

# Subtítulo com estilo de moda
subtitulo = tk.Label(
    janela,
    text="Simulação de Looks Modernos",
    font=("Helvetica", 20, "italic"),
    bg="#2C3E50",
    fg="lightgray",
)
subtitulo.pack(pady=10)

# Frame para exibir as imagens com borda e estilo
frame_imagens = tk.Frame(janela, bg="#34495E", bd=5, relief="sunken", padx=20, pady=20)
frame_imagens.pack(pady=30)

# Label de placeholders para as imagens com borda estilizada
img_label_frente = tk.Label(
    frame_imagens,
    text="Frente",
    bg="#ECF0F1",
    width=PLACEHOLDER_WIDTH,
    height=PLACEHOLDER_HEIGHT,
    relief="groove",
    font=("Helvetica", 12),
    fg="#8E44AD",  # Roxo da moda
)
img_label_frente.grid(row=0, column=0, padx=15)

img_label_costas = tk.Label(
    frame_imagens,
    text="Costas",
    bg="#ECF0F1",
    width=PLACEHOLDER_WIDTH,
    height=PLACEHOLDER_HEIGHT,
    relief="groove",
    font=("Helvetica", 12),
    fg="#8E44AD",
)
img_label_costas.grid(row=0, column=1, padx=15)

img_label_lado = tk.Label(
    frame_imagens,
    text="Lado",
    bg="#ECF0F1",
    width=PLACEHOLDER_WIDTH,
    height=PLACEHOLDER_HEIGHT,
    relief="groove",
    font=("Helvetica", 12),
    fg="#8E44AD",
)
img_label_lado.grid(row=0, column=2, padx=15)

# Label para exibir o conselho da IA
label_conselho = tk.Label(
    janela,
    text="Escolha uma camiseta para receber conselhos de moda.",
    font=("Helvetica", 14),
    bg="#2C3E50",
    fg="white",
    pady=10,
)
label_conselho.pack(pady=20)

# Combobox para selecionar a camiseta com estilo
camisa_var = tk.StringVar()
camisas_opcoes = ["Amarela", "Azul", "Vermelha", "Branca com manga preta"]
camisa_menu = tk.OptionMenu(janela, camisa_var, *camisas_opcoes)
camisa_var.set("Selecione uma camiseta")
camisa_menu.config(
    width=30, font=("Helvetica", 14), bg="#F39C12", fg="black", relief="raised"
)
camisa_menu.pack(pady=15)

# Botões de ação com estilo
btn_mostrar_imagem = tk.Button(
    janela,
    text="Mostrar Imagens",
    command=lambda: selecionar_camisa(camisa_var.get()),
    width=30,
    bg="#3498DB",  # Azul vibrante
    fg="white",
    font=("Helvetica", 14, "bold"),
    relief="raised",
)
btn_mostrar_imagem.pack(pady=10)

btn_video = tk.Button(
    janela,
    text="Reproduzir Vídeo",
    command=lambda: ver_video(camisa_var.get()),
    width=30,
    bg="#E74C3C",  # Vermelho vibrante
    fg="white",
    font=("Helvetica", 14, "bold"),
    relief="raised",
)
btn_video.pack(pady=10)

# Loop principal da interface
janela.mainloop()

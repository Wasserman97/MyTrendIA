MyTrendIA - Simulação de Looks Modernos
MyTrendIA é um MVP (Produto Mínimo Viável) que simula uma assistente de moda usando uma interface gráfica. O sistema permite ao usuário escolher camisetas, visualizar suas imagens e vídeos, e receber recomendações de moda com base no guarda-roupa virtual e na previsão do tempo.

Funcionalidades:
Seleção de camisetas: Visualize camisetas em diferentes ângulos (frente, costas, lado).
Exibição de vídeos: Reproduza vídeos de camisetas.
Recomendações da IA: Receba sugestões de peças de roupa baseadas no guarda-roupa virtual e na previsão do tempo.
Simulação do clima: A IA considera se o clima do dia está frio ou quente para fazer recomendações.
Tecnologias Usadas:
Python: Linguagem principal.
Tkinter: Biblioteca para construção da interface gráfica.
PIL (Pillow): Para manipulação e exibição de imagens.
OpenCV: Para reprodução de vídeos.
Requisitos do Sistema:
Python 3.7 ou superior.
Instalação:
Clone o repositório ou baixe o código:

git clone https://github.com/seu-usuario/MyTrendIA.git
Entre no diretório do projeto:

cd MyTrendIA
Instale as dependências necessárias:

pip install tkinter Pillow opencv-python
Estrutura de Pastas: Crie as seguintes pastas para armazenar as imagens e vídeos no diretório raiz do projeto:

images/: Coloque todas as imagens das camisetas aqui, com os seguintes nomes:
amarelaFre.jpeg (Camiseta amarela - Frente)
amarelaCos.jpeg (Camiseta amarela - Costas)
amarelaDir.jpeg (Camiseta amarela - Lado)
azulFre.jpeg (Camiseta azul - Frente)
azulEsq.jpeg (Camiseta azul - Costas)
azulDir.jpeg (Camiseta azul - Lado)
verFre.jpeg (Camiseta vermelha - Frente)
verCos.jpeg (Camiseta vermelha - Costas)
verDir.jpeg (Camiseta vermelha - Lado)
brancaFre.jpeg (Camiseta branca com manga preta - Frente)
brancaCos.jpeg (Camiseta branca com manga preta - Costas)
brancaDir.jpeg (Camiseta branca com manga preta - Lado)
videos/: Coloque os vídeos das camisetas com os seguintes nomes:
amarelaVid.mp4 (Vídeo da camiseta amarela)
azulVid.mp4 (Vídeo da camiseta azul)
VidBrPr.mp4 (Vídeo da camiseta branca com manga preta)
Executar o programa:

Para rodar o programa, execute o seguinte comando no terminal:

bash
Copiar código
python app.py
Uso:
Ao executar o aplicativo, uma janela com a interface de moda será exibida.

Selecione uma camiseta no menu suspenso e clique no botão "Mostrar Imagens" para visualizar as imagens da camiseta em diferentes ângulos.

Clique no botão "Reproduzir Vídeo" para visualizar o vídeo da camiseta.

A IA exibirá uma recomendação de moda personalizada baseada nas peças disponíveis no guarda-roupa virtual e na previsão do tempo (simulada como "frio" ou "calor").

Frio: A IA sugerirá jaquetas ou peças mais quentes.
Calor: A IA recomendará roupas leves e confortáveis.
Exemplo de Guarda-Roupa Virtual:
Aqui está o exemplo das peças que o sistema considera no guarda-roupa virtual:

Calças: Jeans escura, calça bege, calça preta.
Sapatos: Tênis branco, sapatos marrons, tênis de cano alto.
Jaquetas: Jaqueta preta, jaqueta jeans.
Funcionalidades Finais:
Sugestões personalizadas: A IA vai sugerir o que usar com base nas peças que você já tem. Caso falte algo, ela também sugerirá lojas como Zara e Riachuelo.
Previsão do tempo: A IA vai ajustar suas sugestões com base no clima (simulado).
Melhorias Futuras:
Integração com API de Clima: Para trazer previsões reais e melhorar as sugestões baseadas no tempo.
Guarda-roupa customizável: Permitirá que os usuários adicionem ou removam peças do guarda-roupa virtual.
Sugestões de novos looks: Baseadas em análise de tendências de moda usando Machine Learning.

#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `F4` para abrir o terminal com o diretório na pasta no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `F4` para abrir o terminal com o diretório na pasta no `Linux Ubuntu`
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/use `F4` to open the terminal with the directory in the folder in `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `shell`
# 
# Um `shell` é uma interface de linha de comando que permite aos usuários interagir com um sistema operacional por meio de comandos de texto. Ele atua como uma camada intermediária entre o usuário e o núcleo do sistema, facilitando a execução de programas, manipulação de arquivos e configuração do sistema. Os _shells_ podem variar em complexidade e funcionalidade, desde simples _shells_ de linha de comando até ambientes de desenvolvimento avançados com recursos de automação e personalização. Os exemplos incluem o `Bash`, `Zsh` e `PowerShell`.
# 
# ### `thunar`
# 
# `Thunar` é um gerenciador de arquivos leve e eficiente projetado para ambientes de desktop baseados no `Xfce`. Ele oferece uma interface intuitiva e fácil de usar, com funcionalidades básicas como navegação por diretórios, visualização de arquivos e operações de gerenciamento, como copiar, mover e excluir. O `Thunar` se destaca pela sua velocidade e simplicidade, tornando-o ideal para usuários que buscam uma experiência de gerenciamento de arquivos sem sobrecarga. Além disso, ele suporta extensões e personalizações, permitindo aos usuários adicionar funcionalidades extras conforme necessário.
# 

# ## 1. Como configurar/instalar/usar o `F4` para abrir o `Terminal Emulator` com o diretório na pasta no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `F4` para abrir o `Terminal Emulator` com o diretório na pasta no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#   

# ### 1.1 Configurar/Instalar/Usar o `F4` para abrir o `Terminal Emulator` com o diretório na pasta no `Linux Ubuntu`
# 
# Para conseguir o comportamento desejado, você precisa realmente criar uma Ação Personalizada dentro do `Thunar`, que é diferente de um atalho de teclado global. Aqui está como você pode fazer isso corretamente:
# 
# 1. Exclua qualquer configuração prévia do `F4` em `Keyboard` na aba `Application Shortcuts`
# 
# 2. Abra o `Thunar` e acesse `"Editar" > "Configure custom actions..."`.
# 
# 3. Clique no ícone de `"+"` para adicionar uma nova ação.
# 
# 4. Preencha os detalhes:
# 
#     4.1 **Nome:** `Open Terminal Here` (`"Abrir Terminal Aqui"`) ou algo similar.
# 
#     4.2 **Descrição:** Opcional, mas útil para lembrar o que a ação faz.
#     
#     4.3 **Comando:** `xfce4-terminal --working-directory=%f`.
# 
# 5. Vá para a aba `"Condições de Aparência"` e marque `"Diretórios"` para garantir que a ação apareça apenas quando um diretório estiver selecionado.
# 
# 6. Agora, você precisa configurar o atalho de teclado para essa ação. Normalmente, há uma área nesta janela onde você pode atribuir uma tecla de atalho. Se isso não estiver disponível, você terá que criar o atalho de teclado de uma maneira alternativa:
# 
#     - Algumas versões do `Thunar` permitem que você configure o atalho de teclado diretamente na janela de Ações Personalizadas. Se você vir um campo de atalho de teclado lá, pressione F4 para atribuí-lo à ação.
# 
# 7. Salve a ação personalizada.
# 
# 8. Feche a janela de configuração e **teste a nova ação personalizada** no `Thunar`. Selecione uma pasta e pressione `F4`. O `Terminal Emulator` deve abrir na pasta que você selecionou.
# 
# Se o atalho `F4` ainda não estiver funcionando como esperado, você pode precisar revisar as etapas ou verificar se há conflitos com outros atalhos que possam estar usando a mesma tecla. Em alguns casos, pode ser necessário reiniciar o `Thunar` ou até mesmo fazer _logout_/_login_ para que as novas configurações tenham efeito.

# ## 2. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `F4` para abrir o terminal com o diretório na pasta no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [3] OPENAI. ***Definindo atalho f4 terminal***. Disponível em: <https://chat.openai.com/c/592706f3-7b05-4cff-859e-c5b1727e4735> (texto adaptado). Acessado em: 21/02/2024 13:47.
# 
# [2] OPENAI. ***Vs code: editor popular***. Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 21/02/2024 13:48.
# 
# 

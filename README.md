# Data Warehousing & Business Intelligence da Ouvidoria do Distrito Federal Brasileiro

# Atenção: Os arquivos da entrega da 3va, estão no link abaixo.

[a link](https://drive.google.com/open?id=1SAcG2MWKiNnBArMFQLRZ8MetwAx-B9mf)

# Apresentação

Todo projeto da disciplina Data Warehousing & Business Intelligence, referente à 3VA está disponível no link abaixo:

	https://drive.google.com/drive/folders/1SAcG2MWKiNnBArMFQLRZ8MetwAx-B9mf?usp=sharing

Todos os dados foram extraídos do Portal Brasileiro de Dados Abertos, referentes à Ouvidoria do Distrito Federal, conforme abaixo:

	http://dados.gov.br/dataset/dados-abertos-do-sistema-de-ouvidoria-ouv-df

Tratam-se de dados de todas as Ouvidorias das secretarias, administrações regionais e entidades do Governo do Distrito Federal para registro das reclamações, denúncias, elogios e sugestões feitas pelos cidadãos.

Realizado download de todos os arquivos do portal no drive informado acima. E para melhor entendimento das informações, está disponível o dicionário dos dados obtidos no arquivo <b>dicionario-de-dados-abertos-sistema-de-ouvidoria---ouv-df.pdf</b>.

Para criação e execução de todos os modelos e scripts descritos a seguir foi utilizado o software <b>MySQL Workbench 6.3</b> numa conexão MySQL em <b>localhost</b>.

Para realizar acesso, extração, limpeza, transformação, validação e carga dos dados foi utilizada a ferramenta de ETL <b>Pentaho Data Integration 8.1</b>.

Para fazer consultas e análises OLAP (On-Line Analytical Processing) utilizamos a ferramenta <b>Saiku Analytics</b>, que antes necessita que seja, instalado o <b>Pentaho Bi Server</b> e realizado um cadastro no <b>meteorite.bi</b> (https://licensing.meteorite.bi/login;jsessionid=82A509BE87787D9275F24EA7810AF748) para obter uma licença de uso do Saiku.

# Modelos dos Bancos Operacional e DW

Os modelos da base operacional (<b>base_ouvidoria.mwb</b>) e base do DW (<b>ouvidoria_dw.mwb</b>) podem ser visualizados no software informado acima.

# Script da Base de Dados Operacional

O script da base operacional encontra-se no arquivo <b>script_base_operacional_povoada.sql</b> e deve ser executado no software informado acima na conexão localhost, para carregamento da base. O esquema do banco está identificado por <b>ouvidoria_df</b>. Todas as informações foram extraídas dos arquivos csv disponíveis no drive.

# Base Operacional Online

A base operacional foi hospedada nos servidores do db4free.net e pode ser acessada utilizando phpMyAdmin através do link abaixo:

	https://www.db4free.net/phpMyAdmin/index.php

	Dados de Acesso:
	Utilizador: alunoufrpe2
	Palavra-passe: ufrpedwbi

A aplicação que gera mapa de calor consumirá os dados dessa base online.

# Scripts de Criação do DW

O script do DW vazio encontra-se no arquivo <b>script_ouv_dw.sql</b>, e script do DW com dados inseridos, no arquivo <b>script_ouv_dw_povoada.sql</b>. É recomendável executá-los no Workbench informado anteriormente, na conexão localhost, para carregamento da base DW. O esquema desse banco está identificado por <b>ouv_dw</b>.

# ETL Dimensões

Para esta etapa de ETL, foi utilizada a ferramenta <b>Pentaho Data Integration 8.1</b>, conforme informado. Os arquivos das dimensões estão disponível no drive com os nomes <b>dim_assunto.ktr</b>, <b>dim_classificacao.ktr</b>, <b>dim_localizacao.ktr</b>, <b>dim_manifestacao.ktr</b>, <b>dim_regiaoadm.ktr</b>, <b>dim_resposta.ktr</b>, <b>dim_sexo.ktr</b>, <b>dim_sitmanifestacao.ktr</b>, <b>dim_tema.ktr</b>, <b>dim_tipounidade.ktr</b> e <b>dim_unidade.ktr</b>. É necessário executar cada uma no Pentaho Data Integration para carregamento dos dados de cada uma.

# ETL Fato

Ainda utilizando a ferramenta <b>Pentaho Data Integration 8.1</b>, e com todas as dimensões carregadas, conforme item anterior, é necessário executar o arquivo <b>fato_resolucoes.ktr</b>, para que seja carregado o cubo do fato resoluções.


# Pré-Requisitos para fazer pesquisas no mapa de calor:

Sistema operacional utilizado para rodar a aplicação com mapas de calor: <b>Windows 7 ou superior</b>. <b>Linguagem: Python 3.6</b>.
    
# Guia de instalação para rodar o servidor onde poderá fazer pesquisas no mapa de calor:

Para baixar o código da aplicação, basta ir no github, no link: “https://github.com/ProjetosDW-2018-2/Ouvidoria_DF”, clicar em “Clone or download”, e copiar o link. Você pode importar o projeto pelo próprio Pycharm ou instalando o GIT em sua máquina, para utilizar o Git Bash. Basta criar uma pasta onde ficará o código do projeto, clica nela com o botão direito em “Git bash here”, e ao abrir o terminal do git, colocar: “git clone https://github.com/ProjetosDW-2018-2/Ouvidoria_DF” e esperar fazer o download do projeto.

Indicamos que para rodar essa aplicação, é melhor utilizar um ambiente virtual disponível na própria pasta principal do projeto, cujo o nome é “venv”. Porém, você pode instalar também as bibliotecas utilizadas diretamente na sua máquina.

<b>Observação:</b> As bibliotecas utilizadas no projeto estão no arquivo “requirements.txt” dentro da pasta principal do projeto (“ouvidoria_df”). Caso queira instalar manualmente em sua máquina, basta localizar a pasta onde o Python foi instalado em seu computador, e dentro da pasta “SCRIPT”, copie e cole dentro dela o arquivo “requirements.txt”. Depois você copia o endereço da pasta, abre o CMD, digita “cd” e cola o endereço para entrar nessa pasta. Depois é só digitar “pip install -r requirements.txt” e esperar a instalação de todas as bibliotecas que estão contidas dentro desse arquivo.

Iniciando o ambiente virtual: copie o endereço da pasta “venv”. Abra o CMD e digite: “cd ” e cole o endereço copiado anteriormente. Agora você está dentro da pasta “venv”. Vamos agora iniciar o ambiente. Digite: “venv\Scripts\activate”. Você verá que vai aparecer no início da linha “(venv)”. Isso indica que o ambiente está pronto para uso.

Agora vamos abrir a pasta do projeto. Vá no diretório onde você clonou a pasta do projeto, copie o endereço, abra o CMD e digite: “cd “ e cole o endereço. Depois digite: “python run.py runserver” e espere rodar. Ao rodar, será mostrado o link do ser servidor local (“http://127.0.0.1:5000/”). Copie isso e jogue em um navegador web para abrir a aplicação.

Para acessar os mapas basta fazer login basta entrar com login: “admin@admin.com”; senha: “12345”, também poderá criar o seu próprio usuário.

# Equipe: 

    • Adailson José
    • João D'Amorim
    • Jadeilson Rocha
    • Bruno Lins
    • Wellington Luiz

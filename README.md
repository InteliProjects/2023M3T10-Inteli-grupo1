# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="documentos/outros/assets/imagens/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# Predicas
# FIDCAS

## :student: Integrantes: 
- <a href="https://www.linkedin.com/in/eduardosbarreto/">Eduardo Barreto</a>
- <a href="https://www.linkedin.com/in/gabriel-farias-alves/">Gabriel Farias</a> 
- <a href="https://www.linkedin.com/in/giovana-katsuki-murata-503a94264/">Giovana Katsuki</a>
- <a href="https://www.linkedin.com/in/isabelle-santos-507067204/">Isabelle Santos</a>
- <a href="https://www.linkedin.com/in/lucas-nogueira-nunes/">Lucas Nogueira</a>
- <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Marques</a> 
- <a href="https://www.linkedin.com/in/vitto-mazeto/">Vitto Mazeto</a>

## :teacher: Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/marcelo-gon%C3%A7alves-phd-a550652/">Marcelo Gonçalves</a>
### Instrutores
- <a href="https://www.linkedin.com/in/egondaxbacher/">Egon Daxbacher</a>
- <a href="https://www.linkedin.com/in/flaviomarquesazevedo/">Flavio Marques Azevedo</a> 
- <a href="https://www.linkedin.com/in/francisco-escobar/">Francisco Escobar</a> 
- <a href="https://www.linkedin.com/in/michele-bazana-de-souza-69b77763/">Michele Bazana de Souza</a>
- <a href="https://www.linkedin.com/in/ricardo-jos%C3%A9-missori/">Ricardo Missori</a>

## 📝 Descrição

O projeto desenvolvido visa apresentar uma abordagem de resolução sobre problemas em fundos de investimento em direitos creditórios (FIDCs) relativos a provisionamento para eventuais perdas, decorrentes sobretudo da inadimplência dos créditos cedidos. Através de tecnologias de *machine learning* e modelos de detecção de anomalias, o grupo FIDCAS tem como intenção auxiliar a Comissão de Valores Mobiliários (CVM) a identificar FIDCs em suas bases de dados que possivelmente estão em situação de risco e/ou enfrentando complicações administrativas.

Para aprofundamento acerca da solução tecnológica construída e seu processo de desenvolvimento, acesse a [documentação](./documentos/documentacao.md).

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>documentos</b>: aqui estarão todos os documentos do projeto. Há também uma pasta denominada <b>outros</b> onde estão presentes documentos complementares.

- <b>notebooks</b>: todos os Jupyter Notebooks criados na plataforma Colab para desenvolvimento do projeto.

- <b>src</b>: todos os arquivos referentes à aplicação web construída para utilização da solução desenvolvida.

A estrutura subsequente é definida da seguinte forma:

```
└── notebooks
│   ├── hipoteses
│   ├── modelos
│   ├── processamento
└── src
│   ├── backend
│   ├── public
│   └── frontend
│       └── src
│       │   ├── assets
│       │   ├── styles
└── documentos
│   └── outros
│       │   └── assets
│       │   │   ├── imagens
```

Nas subpastas presentes no projeto, observa-se:

- <b>hipoteses</b>: Jupyter Notebooks utilizados no teste de hipóteses para desenvolvimento do projeto.

- <b>modelos</b>: modelos desenvolvidos em Jupyter Notebooks e utilizados como comparativos para definição do modelo final.

- <b>processamento</b>: Jupyter Notebooks relativos ao tratamento e exploração dos dados.

- <b>backend</b>: todos os arquivos referentes à estrutura do *backend* da aplicação web construída para utilização da solução desenvolvida.

- <b>frontend</b>: todos os arquivos referentes à estrutura do *frontend* da aplicação web construída para utilização da solução desenvolvida.
  
- <b>src</b>: pasta da estrutura padrão do framework "React.js", contendo os componentes utilizados no *frontend*.

- <b>assets</b>: recursos visuais (imagens e ícones) utilizados no *frontend*.

- <b>styles</b>: estilos globais do *frontend* (arquivos *.css* de configuração de estilos da aplicação web).
  
## 💻 Execução dos projetos

A fim de executar o projeto e utilizar o modelo de detecção de anomalias desenvolvido pelo grupo FIDCAS, não é necessário executar nenhum *notebook* presente na pasta "notebooks" do repositório, porque foi criada uma interface *web* para tornar o processo mais simples, intuitivo e, no geral, *user-friendly*. Por isso, é preciso apenas atender aos seguintes requisitos:

- **Instalação do Python**: caso o usuário não possua o Python instalado, é possível realizar essa etapa através deste *link*: https://www.python.org/downloads/.

- **Clonagem do repositório**: para facilitar a utilização, é recomendável realizar a clonagem deste repositório, conservando a estrutura de pastas e a relação entre os arquivos.

- **Posse dos dados utilizados para treinamento do modelo:** é imprescindível que o usuário tenha os dados utilizados para treinamento do modelo, ou seja, os dados que a CVM enviou ao grupo, arquivo originalmente nomeado como "IM_230626_semNP.csv". Eles não estão contidos no repositório por razões de segurança e armazenamento. O arquivo *.csv* deve ser inserido no diretório "data", de forma que o caminho final para o mesmo seja "data/dados_cvm.csv" (o nome do arquivo deve ser igual ao descrito).

- **Instalação das dependências:** como último passo antes da execução de fato, é preciso instalar as dependências do projeto (bibliotecas e *frameworks* utilizados). Para isso, abre-se um terminal e se executa os seguintes comandos:
``` bash
# Na pasta raiz do projeto
pip install -r ./requirements.txt
```
``` bash
# Na pasta "frontend" (dentro de "src")
npm install
```

- **Execução da aplicação *web***: após certificar-se da complitude dos requisitos anteriores, pode-se prosseguir para a execução do sistema da aplicação *web* da solução. Para isso, é necessário abrir um terminal, direcionar-se ao diretório "frontend/src" (dentro de "src") e executar o seguinte comando:
```
npm start
```

Após essas etapas, caso o navegador não abra a página em execução de forma automática, basta acessar o seguinte endereço: https://localhost:3000. A página da *web* contém instruções para o uso do modelo de forma *online*.

## 🗃 Histórico de lançamentos
* 1.0.0 06/10/2023
    * Testes das hipóteses documentados com o modelo definitivo;
    * Documentação da aplicação *web*;
    * Documentação dos resultados finais obtidos;
    * Implementação definitiva do *backend* e do *frontend*.
* 0.4.1 26/09/2023
    * Refatoração de códigos dos modelos e *notebooks*;
    * Correções das estruturas do *backend* e do *frontend*.
* 0.4.0 19/09/2023
    * Versão inicial do *backend* e do *frontend*;
    * Teste e comparação documentados com outros modelos e algoritmos;
    * Implementação do processamento de novos dados, possibilitando *inputs* do usuário.
* 0.3.1 - 10/09/2023
    * Correção e padronização de dependências do projeto;
    * Correções no tratamento de dados. 
* 0.3.0 - 04/09/2023
    * Seleção de *features* para o modelo;
    * Desenvolvimento do modelo com o algoritmo *Isolation Forest*;
    * Documentação do modelo desenvolvido e da metodologia utilizada.
* 0.2.1 - 02/09/2023
    * Mudanças na preparação dos dados.
* 0.2.0 - 26/08/2023
    * Exploração, tratamento e preparação dos dados para treinamento de modelo;
    * Testes de hipóteses do projeto;
    * Documentação das etapas acima.
* 0.1.0 - 12/08/2023
    * Documentação do entendimento do negócio;
    * Documentação das definições iniciais do projeto (descrição, objetivos e problemática);
    * Documentação relativa à Lei Geral de Proteção de Dados.

## 📋 Licença/License

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M3T10-Inteli/grupo1/tree/main">FIDCAS</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.yggbrasil.com.br/vr">Inteli, <a href="https://www.linkedin.com/in/eduardosbarreto/">Eduardo Barreto</a>, <a href="https://www.linkedin.com/in/gabriel-farias-alves/">Gabriel Farias</a> , <a href="https://www.linkedin.com/in/giovana-katsuki-murata-503a94264/">Giovana Katsuki</a>, <a href="https://www.linkedin.com/in/isabelle-santos-507067204/">Isabelle Santos</a>, <a href="https://www.linkedin.com/in/lucas-nogueira-nunes/">Lucas Nogueira</a>, <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Marques</a> , <a href="https://www.linkedin.com/in/vitto-mazeto/">Vitto Mazeto</a></a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

# Simulador-de-Nuvem

Escopo do desenvolvimento: Neste sistema os usuário irão guardar seus arquivos, podendo
servir como backup ou simplesmente repositório de arquivos. A ideia é emular um servidor
que poderia ser hospedado em nuvem ou em qualquer outro lugar (um servidor central de
arquivos em uma casa, empresa, etc.). Os usuários irão logar e terão acesso ao seu
diretório de depósito de arquivo, este diretório por sua vez terá um limite de dados por
usuário e ficará a par dele gerenciar, retirando aquilo que não é mais útil e adicionando
novos arquivos. O sistema não aceitará novos arquivos caso o usuário tenha estourado sua
cota de arquivos. O sistema também identifica usuários logados, e se os mesmos ficarem
muito tempo em inatividade, eles serão desligados do sistema.


O sistema permitirá o cadastro de usuários. Os usuários quando logarem serão
redirecionados para uma tela de gerenciamento, onde poderão ver seu diretório de acordo
com as funções abaixo:

● Ver os arquivos (nomes, datas de envio e tamanho);

● Adicionar um arquivo;

● Excluir um arquivo;

● Ver como está a sua cota de envios (quantos espaço ainda tem livre pra enviar
arquivos);
Para usuários não padrão, como por exemplo um administrador, as funções abaixo estarão
disponíveis:

● Todas as funções de usuário padrão;

● Ver todos os diretórios de todos os usuários;

● Ver o limite de arquivos de todos os usuários;

● Deletar arquivos de um usuário;

● Configuração da cota de envio dos usuários;

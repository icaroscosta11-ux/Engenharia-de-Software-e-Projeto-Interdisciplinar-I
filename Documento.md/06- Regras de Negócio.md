# Introdução

Este documento descreve as regras de negócio efetivamente implementadas no sistema Avalon, considerando apenas as funcionalidades presentes no código-fonte. As regras refletem as operações de cadastro de usuários, consulta de livros via API externa, registro de vendas e geração simplificada de nota fiscal.

##### RN 01 — Cadastro de Usuários
O sistema deve permitir o cadastro de usuários com nome, e-mail e senha.

##### Compatibilidade com o código:
* Implementado na tabela users
* Campos: name, email, password

##### RN 02 — Armazenamento de Credenciais
As senhas dos usuários são armazenadas diretamente no banco de dados conforme recebidas pelo sistema.

##### Compatibilidade com o código:
* Implementado
* Não há criptografia ou hash (descrição reflete exatamente o código)

##### RN 03 — Identificação Única por E-mail
Cada usuário é identificado unicamente pelo seu endereço de e-mail.

##### Compatibilidade com o código:
* Campo email presente
* Usado como identificador lógico do usuário

##### RN 04 — Consulta de Livros via API Externa
O sistema deve permitir a busca de livros utilizando a API do Google Books.

##### Compatibilidade com o código:
* Implementado na função de consulta à API
* Busca realizada por termo digitado pelo usuário

##### RN 05 — Exibição de Informações Básicas do Livro
Os resultados da busca devem exibir informações básicas do livro, como título, autores e descrição quando disponíveis.

##### Compatibilidade com o código:
* Implementado
* Depende da resposta da API do Google Books

##### RN 06 — Registro de Vendas
O sistema deve registrar vendas de livros no banco de dados.

##### Compatibilidade com o código:
* Implementado na tabela sales
* Campos: usuário, livro, valor e data

##### RN 07 — Associação de Venda ao Usuário
Cada venda deve estar vinculada a um usuário previamente cadastrado.

##### Compatibilidade com o código:
* Implementado por meio de chave de relacionamento lógico (user_id)

##### RN 08 — Cálculo de Valor Total da Venda
O valor total da venda deve ser calculado pelo sistema com base no preço informado.

##### Compatibilidade com o código:
* Implementado em função de cálculo
* Não há impostos ou descontos adicionais

##### RN 09 — Geração de Nota Fiscal Simplificada
O sistema deve gerar uma nota fiscal em formato textual contendo os dados da venda.

##### Compatibilidade com o código:
* Implementado
* Nota fiscal simples (string formatada)
* Não é NF-e oficial

##### RN 10 — Armazenamento de Histórico de Vendas
O sistema deve manter o histórico de vendas registradas no banco de dados.

##### Compatibilidade com o código:
* Implementado
* Persistência em SQLite

##### RN 11 — Persistência Local de Dados
Todas as informações do sistema devem ser armazenadas localmente em um banco de dados SQLite.

##### Compatibilidade com o código:
* Implementado (avalon_library.db)

##### RN 12 — Separação de Responsabilidades
O sistema deve separar a lógica de banco de dados das funções de negócio.

##### Compatibilidade com o código:
* Implementado
* database_avalon.py → banco
* funções_avalon.py → regras e lógica

##### RN 13 — Dependência de Serviços Externos
A disponibilidade da busca de livros depende da disponibilidade da API do Google Books.

##### Compatibilidade com o código:
* Condição real do sistema
* Sem cache local

##### RN 14 — Execução em Ambiente Local
O sistema deve funcionar em ambiente local sem necessidade de servidor web.

##### Compatibilidade com o código:
* Implementado
* Execução direta via Python

##### RN 15 — Escopo Funcional Limitado
O sistema não contempla funcionalidades de aluguel, doação, carrinho, pagamento online ou logística.

##### Compatibilidade com o código:
* Regra reflete fielmente o escopo atual
* Evita inconsistência documental

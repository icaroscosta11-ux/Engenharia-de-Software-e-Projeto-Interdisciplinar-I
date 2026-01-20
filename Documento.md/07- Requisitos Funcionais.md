# Introdução 
Os requisitos funcionais a seguir descrevem as funcionalidades efetivamente implementadas no sistema Biblioteca Avalon. Eles definem o comportamento do sistema do ponto de vista do usuário final, garantindo coerência entre a documentação e a aplicação desenvolvida.


##### RF-01 – Cadastro de Usuário: 
O sistema deve permitir o cadastro de usuários por meio de nome completo, e-mail (gmail), senha e endereço.

##### Prioridade: Alta

##### RF-02 – Autenticação de Usuário: 
O sistema deve permitir que usuários cadastrados realizem login utilizando e-mail e senha.

##### Prioridade: Alta

##### RF-03 – Pesquisa de Livros:
O sistema deve permitir a pesquisa de livros por meio de um campo de busca textual, utilizando uma API externa de livros.

##### Prioridade: Alta

##### RF-04 – Exibição de Catálogo:
O sistema deve exibir um catálogo de livros contendo, no mínimo:

* Título
* Autor(es)
* Capa do livro (quando disponível)
* Preço base gerado dinamicamente

##### Prioridade: Alta

RF-05 – Carrinho de Compras: 
O sistema deve permitir que usuários adicionem livros ao carrinho de compras diretamente a partir do catálogo.

##### Prioridade: Alta

##### RF-06 – Modalidades de Aquisição:
O sistema deve permitir que o usuário escolha entre duas modalidades de aquisição:

* Compra
* Aluguel

##### Prioridade: Alta

##### RF-07 – Definição de Prazo de Aluguel:
Para livros alugados, o sistema deve permitir que o usuário defina a quantidade de dias de locação, entre 1 e 7 dias.

##### Prioridade: Média

##### RF-08 – Cálculo Automático de Valores:
O sistema deve calcular automaticamente o valor total da compra ou aluguel, considerando:

* Preço base do livro
* Modalidade escolhida
* Quantidade de dias de aluguel (quando aplicável)

##### Prioridade: Alta

##### RF-09 – Gerenciamento do Carrinho:
O sistema deve permitir que o usuário:

* Visualize os itens do carrinho
* Selecione ou desmarque itens para pagamento
* Remova itens do carrinho

##### Prioridade: Média

##### RF-10 – Pagamento Simulado:
O sistema deve disponibilizar as seguintes opções de pagamento de forma simulada:

* Pix
* Boleto
* Cartão de crédito

##### Prioridade: Alta

##### RF-11 – Finalização da Compra ou Aluguel:
O sistema deve permitir que o usuário finalize a compra ou aluguel dos livros selecionados, registrando a transação no banco de dados.
##### Prioridade: Alta

##### RF-12 – Registro de Histórico de Vendas:
O sistema deve armazenar no banco de dados o histórico de compras e aluguéis realizados pelo usuário.

##### Prioridade: Média

##### RF-13 – Emissão de Nota Fiscal:
O sistema deve gerar e exibir uma nota fiscal textual contendo:

* Dados do cliente
* Data e hora da transação
* Itens adquiridos
* Modalidade (compra ou aluguel)
* Valor total
* Método de pagamento

##### Prioridade: Alta

##### RF-14 – Interface Gráfica Interativa:
O sistema deve disponibilizar uma interface gráfica interativa desenvolvida em Tkinter, permitindo navegação entre telas de forma intuitiva.

##### Prioridade: Alta

##### RF-15 – Manutenção de Sessão do Usuário:
O sistema deve manter os dados do usuário autenticado durante a navegação, até o encerramento da aplicação.

##### Prioridade: Média

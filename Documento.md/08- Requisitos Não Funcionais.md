# Introdução

Os requisitos não funcionais a seguir definem os critérios de qualidade, desempenho, usabilidade e limitações técnicas do sistema Biblioteca Avalon, considerando que se trata de uma aplicação desktop desenvolvida em Python com Tkinter, utilizando banco de dados SQLite local e integrações externas para consulta de livros.

##### RNF-01 – Plataforma de Execução:
O sistema deve ser executado como uma aplicação desktop, compatível com sistemas operacionais que suportem Python 3 e a biblioteca Tkinter.

##### Prioridade: Alta

##### RNF-02 – Interface Gráfica:
O sistema deve possuir uma interface gráfica simples, intuitiva e de fácil navegação, permitindo o uso por usuários sem conhecimento técnico avançado.

##### Prioridade: Alta

##### RNF-03 – Desempenho Local:
O sistema deve apresentar tempo de resposta rápido nas operações locais (cadastro, login, navegação entre telas e cálculo de valores), considerando execução em ambiente local.

##### Prioridade: Média

##### RNF-04 – Integração com Serviços Externos:
A consulta de livros deve ser realizada por meio de integração com uma API externa de livros, dependendo da disponibilidade de conexão com a internet.

##### Prioridade: Alta

##### RNF-05 – Persistência de Dados:
O sistema deve armazenar os dados de usuários e o histórico de transações em um banco de dados SQLite local.

##### Prioridade: Alta

##### RNF-06 – Segurança Básica de Acesso:
O acesso às funcionalidades do sistema deve ser restrito a usuários autenticados por meio de login com e-mail e senha.

##### Prioridade: Alta

##### RNF-07 – Limitações de Segurança:
As informações de pagamento devem ser tratadas apenas de forma simulada, não sendo armazenados dados reais de cartões ou transações financeiras.

##### Prioridade: Alta

##### RNF-08 – Armazenamento de Histórico:
O sistema deve manter o histórico de compras e aluguéis registrados no banco de dados durante o período de utilização da aplicação.

##### Prioridade: Média

##### RNF-09 – Confiabilidade:
O sistema deve garantir a integridade dos dados armazenados, evitando duplicidade de e-mails e registros inconsistentes no banco de dados.

##### Prioridade: Média

RNF-10 – Manutenibilidade

O código-fonte deve ser organizado em módulos separados (interface, regras de negócio e persistência de dados), facilitando manutenção e evolução do sistema.
Prioridade: Alta

RNF-11 – Portabilidade

O sistema deve poder ser executado em diferentes máquinas, desde que o ambiente Python e as dependências necessárias estejam corretamente instalados.
Prioridade: Média

RNF-12 – Limitações do Sistema

O sistema não deve ser considerado uma plataforma comercial real, sendo destinado a fins educacionais e acadêmicos, com funcionalidades de pagamento e nota fiscal simuladas.
Prioridade: Alta



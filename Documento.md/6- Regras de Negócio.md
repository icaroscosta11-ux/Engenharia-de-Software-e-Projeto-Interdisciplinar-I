# Introdução 

A plataforma de compra,aluguel e doação de livros representa uma solução inovadora que democratiza o acesso ao conhecimento através de um modelo de negócio sustentável e inclusivo.Este documento apresenta as 20 regras de negócio que fundamentam a operação,segurança e escalabilidade desta plataforma.

##### Autenticação por E-mail e Senha 
O sistema deve permitir cadastro via e-mail e senha.

##### Justificativa 
Esta regra e fundamental porque:
* Segurança:E-mail e senha são os mecanismos mais estabelecidos para autenticação,permitindo controle de acesso robusto.
* Rastreabilidade:O e-mail único garante identificação inequívoca e cada usuário para auditoria e suporte.
* Conformidade LGPD:Permite registro de consentimento e controle de dados pessoais.
* Experiencia do usuario: Método familiar e confiavel que reduz dricçao n cadastro.
* Operacional:Facilitar recuperaçao de conta e comunicaçao com usuario.
  
##### Validaçao de E-mail de Cadastro 
Deve ser enviado e-mail de confirmaçao de cadastro.

##### Justificativa 
Esta regra e essencial porque: 

* Verificaçao de proproedade:Confirmar que o ususario realmente possui o e-mail fornecido,envitando cadastro fraudulentos.
* Reduçao de spam:Impede criaçao de contas com e-mail invalidos ou de terceiros.
* Segurança:Primeiro passo de verificaçao em dois fatores.
* Comunicaçao: Garante que notificaçoes futuras chegarao ao usuario correto.

##### Recuperaçao de Senha por E-mail
Deve ser enviado e-mail de recuperaçao de senha.

##### Justificativa 
A regra e critica porque: 

* Segurança:Impede que qualquer pessoa resete a senha de outra sem autorizaçao (link unico com expiraçao).
* Conformidade:Atende requisitos explicidos de envio de e-mail de recuperaçao.
* Experiencia:Permite que usuarios recuperem acessi sem contatar suporte.
* Proteçao de dados:Link com expiraçao de 1 Hora reduz janela de vulnerabilidade.
* Auditoria:Cada tentativa e registrada para investigaçao de abuso.

##### Filtros Avançados do Catalogo
Catalogo prescisa ter filtros por genero,autor,estadfo do livro.preco e disponibilidade.

##### Justificativa 
Esta regra e importante porque:

* Usabilidade:Filtros combinados permitem que usuarios encontrem exatamente o que procuram rapidamente.
* Conversao:Reduz tempo para encontrar livro desejado,aumentando taxa de compra.
* Segmentaçao:Permite diferentes estrategias de preco por estado do livro (novo vs. usado).
* Negocio:Facilita descoberta de livros e aumenta ticket medio.
* Dados:Fornece insights sobre preferencias de usuarios para recomendaçao.
  
##### Status em Tempo Real
Cada livro deve exibir seu status em tempo real: disponivel,reservado ou esgotado.

##### Justificativa
Esta regra e fundamental proque:

* Confiança:Usuarios prescisam saber se podem comprar/alugar antes de investir tempo no checkout.
* Evita frustraçao:Redus casos de checkout falhando por indisponibilidade.
* Operacional:Sincronizaçao em tempo teal evita sobrevenda.
* Experiencia:Atatus claro reduz duvidas e suporte necessario.
* Negocio:Aumenta satisfaçao e reduz taxa de abandono de carrinho.


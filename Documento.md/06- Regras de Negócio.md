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

##### Carrinho de Copras e Lista de Desejos
Usuarios podem adicionar livros ao carrinho ou listas de desejos.

##### Justificativa
Esta regra e importante porque:

* Experiencia:Permite que usuarios planejem compras e alugueis.
* Reserva:Carrinho com 15 minutos de reserva que livro seja vendido enquanto usuario esta no checkout.
* Retençao:Lista de desejos  permite remarketing e notificaçao disponibilidade.
* Conversao:Reduz fricçao ao permitir compra em multiplas etapas.
* Negocio:Aumenta valor medio de pedido ao permitir cpmras combinadas.

##### Multiplas Modalidade de Transaçao
Sistema deve permititr compra,aluguel e doaçao diretamente do catalogo.

##### Justificativa 
A regra e critica porque: 

* Modelo de negocio:Oferece multiplas fontes de receita (compra,aluguel,doaçao).
* Mercado:Atende diferentes segmentos de usuarios (compradores,alugadores,doadores).
* Sustentabilidade:Aluguel gera receita recorrente;doacoes aumentam catalogo sem custo.
* Diferenciaçao:Combinaçao de tres modalidades e diferentes competitivo.
* Impacto social:Doacoes promovem acesso a livros para populaçao de baixa renda.

##### Calculo Automatico de Prazo e Multas
Paralocaçoes,prazo e multas devem ser calculados automaticamente.

* Automatizaçao:Remove necessidade de calculo manual,res=duzindo erros.
* Conformidade:Garante aplicaçao consistente de poloticas de multas.
* Receita:Multas por atraso sao fontes de receita e incentivo para devoluçao no prazo.
* Operacional:Reduz carga de trabalho adminidtrativo.
* Transparencia:Usuarios sabem exatamente  qual sera a multa antes de alugar.

##### Classificaçao de Estado do Livro
Doadores podem informar o estado do livro;novo,usado,muito usado.

##### Justificativa
Esta regra e importante porque:

* Qualidade:Permite que usuarios façam escolha informada baseada em estado.
* Preço:Justificativa diferentes faixas de preço para aluguel (novo = mais caro).
* Expectativa: Define expectativa correta sobre condição do livro
* Redução de devoluções: Usuários sabem o que esperar, reduzindo reclamações
* Negócio: Permite monetizar livros usados a preço menor

##### Rastreamento de Pedidos
Usuários devem acompanhar status de pedidos: em
processamento, enviado, entregue, aguardando devolução.

##### Justificativa
Esta regra é fundamental porque:

* Confiança: Transparência sobre onde está o pedido reduz ansiedade do usuário.
* Suporte: Reduz volume de e-mails “onde está meu pedido?”.
* Operacional: Permite identificar gargalos na entrega.
* Experiência: Notificações automáticas mantêm usuário informado.
* Negócio: Aumenta satisfação e reduz taxa de reclamações.


##### Integração de Múltiplos Métodos de Pagamento
Sistema deve integrar pagamentos por cartão, Pix e boleto.

##### Justificativa
Esta regra é crítica porque:

* Inclusão: Diferentes usuários preferem diferentes métodos (cartão para online,
 Pix para instantâneo, boleto para planejado).
* Conversão: Ofertar múltiplas opções aumenta taxa de conclusão de compra.
* Mercado: Pix é método preferido no Brasil; boleto ainda é usado por população
mais conservadora.
* Fluxo de caixa: Boleto permite venda a prazo; Pix oferece confirmação
instantânea.
* Conformidade: Integração com instituições financeiras garante segurança.

##### Cobrança Automática de Multas
Em caso de atraso, multa deve ser cobrada automaticamente.

##### Justificativa
Esta regra é importante porque:

* Automatização: Remove necessidade de contato manual para cobrar multa.
* Conformidade: Garante aplicação consistente de política.
* Receita: Multas são fonte importante de receita para aluguéis.
* Incentivo: Cobrança automática incentiva devolução no prazo.
* Operacional: Reduz carga administrativa de cobrança.

##### Geração de Etiquetas de Envio
Plataforma deve gerar etiquetas de envio e integrar com
transportadoras.

##### Justificativa
Esta regra é fundamental porque:

* Operacional: Automatiza processo de preparação de envio.
* Integração: Conexão com Correios e transportadoras garante entrega confiável.
* Rastreamento: Etiqueta com código permite acompanhamento.
* Escala: Automação permite processar centenas de pedidos sem aumento de
staff.
* Experiência: Usuário recebe código de rastreio automaticamente.

##### Rastreamento com Código de Rastreio
Usuários podem rastrear pedidos com código de rastreio.

##### Justificativa
Esta regra é importante porque:

* Confiança: Usuário pode verificar localização do pacote em tempo real.
* Redução de suporte: Usuários não precisam contatar para saber onde está
pedido.
* Experiência: Transparência aumenta satisfação mesmo se entrega atrasada.
* Operacional: Integração com transportadora fornece dados automaticamente.
* Negócio: Rastreamento é diferencial de qualidade.

##### Suporte ao Cliente Multicanal
Deve haver suporte por chat, e-mail e telefone.

##### Justificativa
Esta regra é importante porque:

* Acessibilidade: Diferentes usuários preferem diferentes canais (chat para rápido,
e-mail para documentado, telefone para complexo).
* Satisfação: Múltiplos canais aumentam satisfação do cliente.
* Operacional: Chat para problemas simples; e-mail para documentação; telefone
para escalação.
* Cobertura: Ofertar múltiplos canais garante que usuário consegue contato.
* Negócio: Suporte de qualidade reduz churn e aumenta retenção.

Gestão de Estoque e Catálogo
Administradores precisam gerenciar estoque, cadastrar livros e
aprovar doações.

##### Justificativa
Esta regra é crítica porque:

* Operacional: Ferramentas de gestão permitem que admin controle catálogo.
* Qualidade: Aprovação de doações garante que apenas livros de qualidade
entram no catálogo.
* Escalabilidade: Sem ferramentas de gestão, plataforma não consegue escalar.
* Conformidade: Controle de estoque garante não vender mais do que tem.
* Negócio: Gestão eficiente de estoque reduz custo operacional.

##### Relatórios de Desempenho
Sistema deve emitir relatórios de vendas, locações, atrasos e
estoque.

##### Justificativa
Esta regra é importante porque:

* Decisão: Relatórios permitem que gestão tome decisões baseadas em dados.
* Análise: Identifica tendências (quais livros vendem mais, qual taxa de atraso).
* Operacional: Relatório de estoque baixo permite reposição proativa.
* Negócio: Análise de desempenho permite otimizar preços e estratégia.
* Conformidade: Histórico de transações necessário para auditoria.

##### Alertas de Estoque Baixo
Equipe deve ser notificada quando estoque estiver baixo.

##### Justificativa
Esta regra é importante porque:

* Operacional: Notificação automática evita que admin esqueça de reabastecer.
* Negócio: Evita perder vendas por falta de estoque.
* Proatividade: Permite reposição antes de esgotar completamente.
* Eficiência: Reduz necessidade de verificação manual de estoque.
* Satisfação: Mantém livros populares sempre disponíveis.

##### Desempenho e Escalabilidade
Plataforma deve suportar 5 mil usuários simultâneos sem perda
de desempenho,Tempo de carregamento inferior a 3 segundos.

##### Justificativa
Esta regra é fundamental porque:

* Experiência: Páginas lentas aumentam taxa de abandono.
* Negócio: Cada segundo de latência reduz conversão em ~7%.
* Escalabilidade: Sem otimização, plataforma não consegue crescer.
* Confiabilidade: Sistema deve funcionar mesmo em picos de tráfego.
* Competição: Usuários têm alternativas; performance lenta os afasta.

##### Conformidade Legal e Segurança
Dados sensíveis criptografados,
Conformidade LGPPD
NF-e conforme legislação,Histórico por 5 anos

##### Justificativa
Esta regra é crítica porque:

* Conformidade legal: Violação de LGPD resulta em multas de até 2% do
faturamento.
* Segurança: Criptografia protege dados de usuários contra roubo.
* Confiança: Usuários confiam em plataforma que protege seus dados.
* Operacional: Backup diário garante continuidade em caso de falha.
* Auditoria: Histórico de 5 anos permite rastrear qualquer transação.
* Negócio: Conformidade é requisito para operar legalmente no Brasil.

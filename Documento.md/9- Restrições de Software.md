#Introdução

As restrições de software representam os limites e as condições sob as quais um sistema
deve ser desenvolvido e operado. Para um Sistema de Gerenciamento de Biblioteca (SGB),
essas restrições são cruciais, pois influenciam diretamente as escolhas tecnológicas, a
arquitetura do sistema, o cronograma de desenvolvimento e os custos. Ignorar ou
subestimar as restrições pode levar a problemas de desempenho, segurança,
compatibilidade e, em última instância, ao fracasso do projeto. Este documento detalha as
principais restrições de software a serem consideradas no desenvolvimento do SGB,
garantindo que o sistema seja construído de forma realista e sustentável.

##### Restrições de Software
As restrições de software para o Sistema de Gerenciamento de Biblioteca podem ser
categorizadas em técnicas, operacionais, regulatórias e de projeto:

* Restrições Técnicas
Estas restrições referem-se a limitações impostas pela tecnologia ou pela infraestrutura
existente:

* Plataforma de Desenvolvimento: O sistema deve ser desenvolvido utilizando
tecnologias web modernas (ex: Python com Django/Flask, JavaScript com
React/Angular/Vue, Java com Spring Boot) para garantir portabilidade, escalabilidade e
facilidade de manutenção. A escolha específica dependerá da expertise da equipe e da
infraestrutura disponível.

* Banco de Dados: A escolha do sistema de gerenciamento de banco de dados (SGBD)
pode ser restrita a opções específicas (ex: PostgreSQL, MySQL, SQL Server) devido a
licenças existentes, políticas da instituição ou expertise da equipe de TI. O SGBD deve
suportar um grande volume de dados e transações, além de garantir a integridade e a
segurança das informações.

• Infraestrutura de Servidores: O sistema deve ser compatível com a infraestrutura de
servidores existente na instituição (ex: Linux, Windows Server, ambientes de nuvem
como AWS, Azure, Google Cloud). Isso inclui requisitos de hardware (CPU, RAM,
armazenamento) e software (sistema operacional, servidores web).

• Interoperabilidade: O SGB pode precisar se integrar com outros sistemas da
instituição, como sistemas acadêmicos (para cadastro de alunos e professores),
sistemas financeiros (para gestão de multas) ou sistemas de autenticação (LDAP/Active
Directory). Isso impõe restrições sobre os protocolos e formatos de dados a serem
utilizados (ex: APIs RESTful, XML, JSON).
• Compatibilidade com Navegadores: O sistema deve ser totalmente funcional e
apresentar uma experiência consistente nos principais navegadores web (Chrome,
Firefox, Edge, Safari) e em diferentes dispositivos (desktop, tablet, mobile).
. Restrições Operacionais
Estas restrições estão relacionadas ao ambiente em que o sistema será utilizado e mantido:
• Disponibilidade: O sistema deve estar disponível horas por dia,dias por semana,
com um tempo de inatividade mínimo, conforme estabelecido nos requisitos não
funcionais. Isso implica em requisitos de arquitetura para alta disponibilidade e planos
de recuperação de desastres.

• Manutenção e Suporte: O sistema deve ser fácil de manter e suportar pela equipe de TI
da instituição. Isso inclui a necessidade de documentação clara, código bem
estruturado e a utilização de tecnologias que a equipe já possui conhecimento ou que
possam ser facilmente aprendidas.

• Backup e Recuperação: Devem ser implementadas rotinas de backup automático e um
plano de recuperação de desastres para garantir a continuidade dos serviços e a
proteção dos dados em caso de falhas.

##### Restrições Regulatórias e de Conformidade
Estas restrições são impostas por leis, normas ou políticas internas:

• Lei Geral de Proteção de Dados (LGPD - Brasil): O sistema deve estar em total
conformidade com a LGPD, garantindo a privacidade e a proteção dos dados pessoais
dos usuários. Isso inclui a coleta mínima de dados, consentimento explícito, direitos
dos titulares (acesso, correção, exclusão) e medidas de segurança adequadas.
• Políticas de Segurança da Informação da Instituição: O SGB deve aderir às políticas
de segurança da informação da instituição, que podem incluir requisitos específicos de
autenticação, controle de acesso, criptografia e auditoria.
• Acessibilidade: O sistema deve ser acessível a pessoas com deficiência, seguindo
diretrizes de acessibilidade web (ex: WCAG) para garantir que todos os usuários possam
utilizá-lo plenamente.

##### Restrições de Projeto
Estas restrições são impostas pelo próprio projeto, como recursos e prazos:

• Orçamento: O desenvolvimento e a manutenção do SGB devem se enquadrar no
orçamento alocado, o que pode influenciar a escolha de tecnologias (software livre vs.
proprietário) e a extensão das funcionalidades.
• Cronograma: O sistema deve ser entregue dentro de um prazo estabelecido, o que
pode exigir a priorização de funcionalidades e a adoção de metodologias ágeis para
entregas incrementais.
• Recursos Humanos: A disponibilidade e a expertise da equipe de desenvolvimento
podem restringir as escolhas tecnológicas e a complexidade das soluções a serem
implementadas.

# Conclusão
As restrições de software são elementos intrínsecos ao processo de desenvolvimento e
devem ser cuidadosamente consideradas desde as fases iniciais do projeto. Ao identificar e
documentar essas limitações técnicas, operacionais, regulatórias e de projeto, é possível
tomar decisões mais informadas, mitigar riscos e garantir que o Sistema de Gerenciamento
de Biblioteca seja uma solução viável, segura, compatível e sustentável a longo prazo. Um
entendimento claro dessas restrições é fundamental para o sucesso da implementação e
para a satisfação de todos os envolvidos.

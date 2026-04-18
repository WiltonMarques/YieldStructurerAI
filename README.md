🏛️ YieldStructurer Inteligência Artificial (AI): Motor Quantitativo de Mercado de Capitais de Dívida (DCM - Debt Capital Markets) e Gestão de Ativos e Passivos (ALM - Asset Liability Management)
📌 A Assimetria Informacional em Finanças Corporativas
Na estruturação de dívida corporativa (Debêntures, Certificados de Recebíveis Imobiliários - CRIs, Certificados de Depósito Bancário - CDBs), as empresas frequentemente aceitam prêmios de risco (spreads) precificados de forma ineficiente pelas mesas de operações. Este projeto mitiga esse risco através de Engenharia Quantitativa.

💡 A Solução Tecnológica
O YieldStructurer Inteligência Artificial (AI) é um motor de precificação (pricing) e conformidade regulatória (compliance) construído em Python. Ele atua como um assessor fiduciário algorítmico, ingerindo variáveis do mercado secundário e da estrutura de capital para achar o custo exato da dívida.

⚙️ Arquitetura e Engenharia de Dados
Ingestão Dinâmica ("Cata-Tudo"): O motor lê pacotes de dados em Notação de Objetos JavaScript (JSON - JavaScript Object Notation) heterogêneos da bolsa de valores brasileira (Brasil, Bolsa, Balcão - B3), contornando quebras de estrutura de dados (schema) e aninhamentos complexos via extração recursiva.

Interpolação SciPy: Cálculo exato da Taxa Livre de Risco (Risk-Free) cruzando os dias úteis da operação contra os vértices estocásticos da Curva de Depósitos Interfinanceiros (Curva DI).

Matrizes de Governança: Precificação do risco de eventos extremos (tail risk) baseado na Classificação de Risco de Crédito (Rating) e Hierarquia de Garantias (Real, Flutuante, Quirografária, Subordinada).

Conformidade Automatizada: Geração automática de Relatórios de Auditoria (Audit Reports) em formato de texto (.txt) a cada simulação, registrando a memória de cálculo para auditorias independentes e atendimento à Resolução 160 da Comissão de Valores Mobiliários (CVM).

🚀 Estudo de Caso: Emissora MODELO Sociedade Anônima (S.A.)
Simulação real de captura de ineficiência de balcão para uma captação de 100 Milhões de Reais (R$) (Classificação de risco de crédito máxima - Rating AAA, Prazo de 5 anos, Garantia Quirografária).

Resultados do Motor (Terminal):

Taxa de Depósito Interfinanceiro (DI) da bolsa brasileira (B3) Interpolada: 13.295% ao ano (a.a.)

Taxa Ofertada pelo Banco (Spread 1.50%): 14.795% ao ano (a.a.)

Taxa Justa Sugerida pela Inteligência Artificial (IA) (Spread 1.30%): 14.595% ao ano (a.a.)

Economia Real Protegida: 200.000,00 Reais (R$) / ano

Retorno sobre o Investimento (ROI - Return on Investment) da Solução Tecnológica: 66.7%

🛠️ Tecnologias Utilizadas (Stack)
Python 3.10+ | SciPy | NumPy | Notação de Objetos JavaScript (JSON) | Programação Orientada a Objetos (POO)

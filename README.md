# 🏛️ YieldStructurer AI: Motor Quantitativo de DCM e ALM

## 📌 A Assimetria Informacional em Finanças Corporativas
Na estruturação de dívida corporativa (Debêntures, CRIs, CDBs), as empresas frequentemente aceitam prêmios de risco (*spreads*) precificados de forma ineficiente pelas mesas de operações. Este projeto mitiga esse risco através de **Engenharia Quantitativa**.

## 💡 A Solução Tecnológica
O **YieldStructurer AI** é um motor de *pricing* e compliance regulatório construído em Python. Ele atua como um assessor fiduciário algorítmico, ingerindo variáveis do mercado secundário e da estrutura de capital para achar o custo exato da dívida.

### ⚙️ Arquitetura e Engenharia de Dados
* **Ingestão Dinâmica ("Cata-Tudo"):** O motor lê payloads JSON heterogêneos da B3, contornando quebras de schema e aninhamentos complexos via extração recursiva.
* **Interpolação SciPy:** Cálculo exato da Taxa Livre de Risco (Risk-Free) cruzando os dias úteis da operação contra os vértices estocásticos da Curva DI.
* **Matrizes de Governança:** Precificação do risco de cauda (*tail risk*) baseado em Rating de Crédito e Hierarquia de Garantias (Real, Flutuante, Quirografária, Subordinada).
* **Compliance Automatizado:** Geração automática de `Audit Reports` em `.txt` a cada simulação, registrando a memória de cálculo para auditorias independentes e atendimento à Resolução CVM 160.

## 🚀 Estudo de Caso: Emissora MODELO S.A.
Simulação real de captura de ineficiência de balcão para uma captação de R$ 100 Milhões (Rating AAA, Prazo de 5 anos, Garantia Quirografária).

**Output do Motor (Terminal):**
* Taxa DI (B3) Interpolada: 13.295% a.a.
* Taxa Ofertada pelo Banco (Spread 1.50%): 14.795% a.a.
* **Taxa Justa Sugerida pela IA (Spread 1.30%): 14.595% a.a.**
* **Economia Real Protegida:** R$ 200.000,00 / ano
* **ROI da Solução Tecnológica:** 66.7%

## 🛠️ Stack Utilizado
`Python 3.10+` | `SciPy` | `NumPy` | `JSON` | `POO`
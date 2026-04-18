import os
from datetime import datetime

def gerar_relatorio_auditoria(dados_emissao, resultados_pricing):
    """
    Gera a Nota Técnica de Compliance em formato .txt para fins de auditoria.
    Os dados são injetados dinamicamente a cada cálculo do motor principal.
    """
    data_emissao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_emissor = dados_emissao['emissor'].upper()
    
    # Definição do nome do arquivo (rastreável por data e emissor)
    timestamp_arq = datetime.now().strftime("%Y%m%d_%H%M")
    nome_arquivo = f"Audit_Report_{nome_emissor}_{timestamp_arq}.txt"
    caminho_dir = os.path.join(os.getcwd(), 'docs', 'regulatorio')
    
    # Garante que o diretório exista
    if not os.path.exists(caminho_dir):
        os.makedirs(caminho_dir)
    
    caminho_completo = os.path.join(caminho_dir, nome_arquivo)

    conteudo = f"""=====================================================================
NOTA TÉCNICA DE COMPLIANCE: PRECIFICAÇÃO DE DÍVIDA (DCM)
=====================================================================
ID DO RELATÓRIO: {timestamp_arq}
EMISSOR AUDITADO: {nome_emissor}
DATA DE REFERÊNCIA: {data_emissao}
RESPONSÁVEL TÉCNICO: Wilton Marques do Amaral
---------------------------------------------------------------------

1. IDENTIFICAÇÃO DA OPERAÇÃO
----------------------------
Volume Financeiro (Notional): R$ {dados_emissao['volume']:,.2f}
Prazo (Duration): {dados_emissao['prazo']} Anos
Rating Corporativo: {dados_emissao['rating']}
Espécie de Garantia: {dados_emissao['garantia']}
Incentivo Fiscal (Lei 12.431/11): {"Sim" if dados_emissao['incentivada'] else "Não"}
Público-Alvo: {dados_emissao['publico']}

2. FUNDAMENTAÇÃO REGULATÓRIA
----------------------------
- Resolução CVM 160: Adoção de rito conforme perfil de investidor.
- Governança de Crédito: Precificação do risco de cauda baseada na 
  hierarquia de garantias (adicional por ausência de privilégio real).
- Marcação a Mercado: Interpolação linear paramétrica da curva DI1/B3.

3. MEMÓRIA DE CÁLCULO (DINÂMICA)
--------------------------------
Taxa Livre de Risco (Curva DI B3): {resultados_pricing['taxa_di']:.3f}% a.a.
Spread de Crédito (Rating): +{resultados_pricing['spread_base']:.3f}% a.a.
Ajuste por Espécie/Garantia: +{resultados_pricing['ajuste_garantia']:.3f}% a.a.
Benefício Fiscal (Lei 12.431/11): {resultados_pricing['desconto_incentivo']:.3f}% a.a.

>>> TAXA FINAL JUSTA CALCULADA (AI): {resultados_pricing['taxa_ai']:.3f}% a.a.

4. ANÁLISE DE EFICIÊNCIA E ROI
------------------------------
Cotação Banco (Manual): {resultados_pricing['taxa_banco']:.3f}% a.a.
Ineficiência Identificada: {resultados_pricing['spread_manual'] - resultados_pricing['spread_ai']:.3f}% (Basis Points)
ECONOMIA FINANCEIRA DIRETA: R$ {resultados_pricing['economia']:,.2f} / ano
ROI DA SOLUÇÃO TECNOLÓGICA: {resultados_pricing['roi']:.1f}%

5. PARECER CONCLUSIVO
---------------------
Atesto que a precificação calculada reflete com exatidão matemática o 
risco de crédito e o enquadramento jurídico da operação. O modelo eliminou 
a assimetria informacional da tesouraria, garantindo a redução do custo 
do passivo financeiro em conformidade com as normas vigentes.

---------------------------------------------------------------------
Documento gerado eletronicamente para fins de prestação de contas.
====================================================================="""

    with open(caminho_completo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    return caminho_completo
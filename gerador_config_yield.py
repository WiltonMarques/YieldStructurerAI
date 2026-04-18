import json
import os
from datetime import datetime

def verificar_diretorio_compliance():
    """Garante que a estrutura de pastas regulatórias exista no projeto."""
    caminho_docs = os.path.join(os.getcwd(), 'docs', 'regulatorio')
    if not os.path.exists(caminho_docs):
        os.makedirs(caminho_docs)
        print(f"📁 Diretório de compliance criado em: {caminho_docs}")
        print("⚠️ Lembrete: Salve os PDFs normativos nesta pasta para auditoria futura.\n")

def gerar_configuracao_yield():
    """
    Interface interativa para captura de parâmetros de estruturação de dívida.
    Gera o arquivo 'config_yield.json' com mapeamento completo de compliance.
    """
    print("==================================================")
    print("📝 CONFIGURADOR DE EMISSÃO - YIELD STRUCTURER AI")
    print("==================================================")

    # Verifica/Cria a pasta de documentos regulatórios
    verificar_diretorio_compliance()

    try:
        # Captura interativa de dados da Operação
        empresa = input("Nome da Empresa Emissora: ").strip()
        volume = float(input("Volume da Emissão (BRL) [Ex: 100000000]: "))
        prazo = int(input("Prazo da Operação (Anos) [Ex: 5]: "))
        
        print("\n[Ratings Disponíveis: AAA, AA, A, BBB, BB, B]")
        rating = input("Rating Corporativo Atual: ").strip().upper()
        
        print("\n[Espécies de Garantia (FIPECAFI): Real, Flutuante, Quirografaria, Subordinada]")
        garantia = input("Espécie da Garantia: ").strip().capitalize()
        
        resposta_incentivo = input("Debênture Incentivada (Lei 12.431)? (S/N): ").strip().upper()
        incentivada = True if resposta_incentivo == 'S' else False
        
        print("\n[Públicos: Profissional, Qualificado, Varejo]")
        publico = input("Público-Alvo da Oferta: ").strip().capitalize()
        
        spread_banco = float(input("Spread atual proposto pelo banco (ex: 1.5 para 1.5%): "))

        # Montagem do Dicionário de Configuração (Totalmente mapeado com os PDFs)
        config = {
            "metadata": {
                "emissor": empresa,
                "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "projeto": "YieldStructurer AI"
            },
            "parametros_emissao": {
                "volume_brl": volume,
                "prazo_anos": prazo,
                "rating": rating,
                "especie_garantia": garantia,
                "isencao_fiscal": incentivada,
                "publico_alvo": publico
            },
            "benchmarks": {
                "spread_banco_atual": spread_banco,
                "custo_plataforma_anual": 120000.00
            },
            "arquivos_referencia": {
                "normativo_cvm_ofertas": "docs/regulatorio/Resolucao_CVM_160_Ofertas_Publicas.pdf",
                "normativo_cvm_coordenadores": "docs/regulatorio/Resolucao_CVM_161_Coordenadores.pdf",
                "lei_incentivo_fiscal": "docs/regulatorio/Lei_12431_Debentures_Incentivadas.pdf",
                "auditoria_bacen": "docs/regulatorio/Resolucao_BCB_352_Controles_Internos.pdf",
                "base_tecnica_garantias": "docs/regulatorio/Manual_FIPECAFI_Garantias.pdf"
            }
        }

        # Exportação para arquivo JSON local
        caminho_arquivo = 'config_yield.json'
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        print("\n✅ Sucesso! Arquivo de parâmetros ('config_yield.json') gerado.")
        print(f"📁 Local salvo: {os.path.abspath(caminho_arquivo)}")
        print("🚀 O motor 'yield_structurer_engine.py' já pode ser executado!")
        print("==================================================\n")

    except ValueError:
        print("\n❌ Erro de digitação: Certifique-se de digitar apenas números válidos para Volume, Prazo e Spread (use '.' para decimais).")
    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    gerar_configuracao_yield()
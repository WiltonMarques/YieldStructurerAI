import pandas as pd
import json
import pyperclip
from io import StringIO
from datetime import datetime
import numpy as np

class CapturadorCurvaB3:
    """
    Módulo de Ingestão de Dados de Mercado.
    Lê a curva DI via clipboard e persiste em JSON para o motor de estruturação.
    """
    def __init__(self, output='curva_di_b3.json'):
        self.output = output

    def executar(self):
        print("📋 Capturando dados da Área de Transferência...")
        texto = pyperclip.paste()
        
        if not texto or len(texto) < 20:
            print("❌ Erro: Área de transferência vazia ou inválida.")
            return

        try:
            # Parsing dos dados (considerando tabulações comuns em sites financeiros)
            df = pd.read_csv(StringIO(texto), sep='\t', decimal='.', thousands=',')
            df.columns = [str(col).strip().upper() for col in df.columns]
            
            # Localização dinâmica de colunas (Vencimento e Taxa)
            col_venc = next(c for c in df.columns if 'VENCIMENTO' in c)
            col_taxa = next(c for c in df.columns if 'TAXA' in c)
            
            df = df[[col_venc, col_taxa]].dropna()
            hoje = datetime.now().date()
            vertices = []

            for _, row in df.iterrows():
                v_date = datetime.strptime(str(row[col_venc]), "%d/%m/%Y").date()
                du = int(np.busday_count(hoje, v_date))
                if du > 0:
                    vertices.append({
                        "du": du,
                        "taxa": round(float(row[col_taxa]), 4)
                    })

            data_final = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fonte": "B3 / InfoMoney",
                "vertices": sorted(vertices, key=lambda x: x['du'])
            }

            with open(self.output, 'w', encoding='utf-8') as f:
                json.dump(data_final, f, indent=4)
            
            print(f"✅ Arquivo {self.output} gerado com {len(vertices)} pontos da curva.")

        except Exception as e:
            print(f"❌ Falha no processamento: {e}")

if __name__ == "__main__":
    CapturadorCurvaB3().executar()
import json
import os
import numpy as np
from scipy.interpolate import interp1d
from compliance_report_generator import gerar_relatorio_auditoria

class YieldStructurerEngine:
    def __init__(self, config_operacao='config_yield.json', config_curva='curva_di_b3.json'):
        self.config_operacao = config_operacao
        self.config_curva = config_curva
        self.dados = self._carregar_dados_atuais()
        
        self.matriz_rating = {'AAA': 1.000, 'AA': 1.250, 'A': 1.500, 'BBB': 2.500}
        self.matriz_garantia = {
            'REAL': 0.000, 'FLUTUANTE': 0.150, 
            'QUIROGRAFARIA': 0.300, 'SUBORDINADA': 0.600
        }

    def _carregar_dados_atuais(self):
        try:
            with open(self.config_operacao, 'r', encoding='utf-8') as f:
                operacao = json.load(f)
            with open(self.config_curva, 'r', encoding='utf-8') as f:
                curva = json.load(f)
            return {**operacao, "curva_b3": curva}
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Erro: Arquivo {e.filename} não encontrado.")

    def _interpolar_curva_di(self, curva, prazo_anos):
        prazo_dias = float(prazo_anos) * 252.0
        x_list, y_list = [], []

        # Extrator Recursivo: varre qualquer tipo de estrutura JSON
        def extrair_pontos(dados):
            if isinstance(dados, list):
                for item in dados:
                    if isinstance(item, list) and len(item) >= 2:
                        try:
                            x_list.append(float(str(item[0]).replace(',', '.')))
                            y_list.append(float(str(item[1]).replace(',', '.')))
                        except: pass
                    elif isinstance(item, dict):
                        try:
                            nums = [float(str(val).replace(',', '.')) for val in item.values() 
                                    if str(val).replace(',', '.').replace('.', '').replace('-', '').isdigit()]
                            if len(nums) >= 2:
                                x_list.append(max(nums))
                                y_list.append(min(nums))
                        except: pass
            elif isinstance(dados, dict):
                if any(isinstance(v, (list, dict)) for v in dados.values()):
                    for v in dados.values():
                        extrair_pontos(v)
                else:
                    for k, v in dados.items():
                        try:
                            x_list.append(float(str(k).replace(',', '.')))
                            y_list.append(float(str(v).replace(',', '.')))
                        except: pass

        extrair_pontos(curva)

        if not x_list:
            raise ValueError(f"Falha ao ler a curva. Amostra do JSON: {str(curva)[:100]}")

        # Ordena e remove dias duplicados (SciPy trava se houver X repetido)
        pontos = sorted(zip(x_list, y_list))
        pontos_unicos = {p[0]: p[1] for p in pontos}
        
        x = np.array(list(pontos_unicos.keys()))
        y = np.array(list(pontos_unicos.values()))
        
        if len(x) < 2:
            raise ValueError("Não há pontos suficientes para traçar a curva B3.")

        return float(interp1d(x, y, kind='linear', fill_value="extrapolate")(prazo_dias))

    def processar_operacao(self):
        d = self.dados
        
        meta = d.get('metadata', {})
        params = d.get('parametros_emissao', {})
        bench = d.get('benchmarks', {})

        emissor = meta.get('emissor', 'N/D')
        volume = float(params.get('volume_brl', 0))
        prazo = float(params.get('prazo_anos', 5))
        rating = str(params.get('rating', 'A')).upper()
        garantia = str(params.get('especie_garantia', 'QUIROGRAFARIA')).upper()
        isencao = bool(params.get('isencao_fiscal', False))
        
        spread_manual = float(bench.get('spread_banco_atual', 1.5))
        custo_tech = float(bench.get('custo_plataforma_anual', 120000))

        # ====================================================================
        taxa_di_spot = self._interpolar_curva_di(d['curva_b3'], prazo)
        
        spread_base = self.matriz_rating.get(rating, 3.000)
        ajuste_gar = self.matriz_garantia.get(garantia, 0.500)
        desconto_isencao = 0.200 if isencao else 0.000
        
        spread_ai = (spread_base + ajuste_gar) - desconto_isencao
        taxa_final_ai = taxa_di_spot + spread_ai
        taxa_manual_final = taxa_di_spot + spread_manual
        
        economia_anual = volume * ((spread_manual - spread_ai) / 100)
        roi = ((economia_anual - custo_tech) / custo_tech) * 100 if custo_tech > 0 else 0

        # ====================================================================
        dados_reporte = {
            "emissor": emissor, "volume": volume, "prazo": prazo,
            "rating": rating, "garantia": garantia, 
            "incentivada": isencao, "publico": params.get('publico_alvo', 'N/D')
        }
        resultados_pricing = {
            "taxa_di": taxa_di_spot, "spread_base": spread_base, "ajuste_garantia": ajuste_gar,
            "desconto_incentivo": desconto_isencao, "taxa_ai": taxa_final_ai,
            "taxa_banco": taxa_manual_final, "spread_manual": spread_manual,
            "spread_ai": spread_ai, "economia": economia_anual, "roi": roi
        }

        path = gerar_relatorio_auditoria(dados_reporte, resultados_pricing)
        self._exibir_dashboard(emissor, prazo, rating, garantia, taxa_di_spot, spread_ai, taxa_final_ai, taxa_manual_final, economia_anual, roi, path)

    def _exibir_dashboard(self, emissor, prazo, rating, garantia, di, spread, taxa_ai, taxa_b, econ, roi, path):
        print("="*60)
        print(f"🏛️ YIELD STRUCTURER AI - PRECIFICAÇÃO: {emissor.upper()}")
        print("="*60)
        print(f"📊 Rating: {rating} | Garantia: {garantia.title()} | {int(prazo)} Anos")
        print(f"📈 Curva DI (B3):      {di:.3f}% a.a.")
        print(f"🌱 Spread Otimizado:   +{spread:.3f}% a.a.")
        print(f"✅ TAXA SUGERIDA AI:   {taxa_ai:.3f}% a.a.")
        print(f"🏦 Taxa Banco/Manual:  {taxa_b:.3f}% a.a.")
        print("-" * 60)
        print(f"💰 Economia Real:      R$ {econ:,.2f} / ano".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print(f"🚀 ROI da Solução:     {roi:.1f}%")
        print("-" * 60)
        print(f"📄 Audit Report vinculado salvo em:\n   {path}")
        print("="*60)

if __name__ == "__main__":
    YieldStructurerEngine().processar_operacao()
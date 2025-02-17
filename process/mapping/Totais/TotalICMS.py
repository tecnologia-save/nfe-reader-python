from process.util import extract_value

class TotalICMS:
    def __init__(self, item):

        self.base_calculo_icms = extract_value(item, "./vBC") if extract_value(item, "./vBC") else 0
        self.valor_total_icms = extract_value(item, "./vICMS")
        self.valor_total_icms_desonerado = extract_value(item, "./vICMSDeson")
        self.valor_total_icms_relativo_fundo_combate_pobreza = extract_value(item, "./vFCPUFDest")
        self.valor_total_icms_partilha_uf_destinatario = extract_value(item, "./vICMSUFDest")
        self.valor_total_icms_partilha_uf_remetente = extract_value(item, "./vICMSUFRemet")
        self.valor_total_fcp_fundo_combate_pobreza = extract_value(item, "./vFCP")
        self.base_calculo_icms_st = extract_value(item, "./vBCST")
        self.valor_total_icms_st = extract_value(item, "./vST")
        self.valor_total_fcp_fundo_combate_pobreza_retido_substituicao_tributaria = extract_value(item, "./vFCPST")
        self.valor_total_fcp_fundo_combate_pobreza_retido_anteriormente_substituicao_tributaria = extract_value(item, "./vFCPSTRet")
        self.valor_total_quantidade_tributada_icms_monofasico_proprio = extract_value(item, "./qBCMon")
        self.valor_total_icms_monofasico_proprio = extract_value(item, "./vICMSMon")
        self.valor_total_quantidade_tributada_icms_monofasico_sujeito_retencao = extract_value(item, "./qBCMonReten")
        self.valor_total_icms_monofasico_sujeito_retencao = extract_value(item, "./vICMSMonReten")
        self.valor_total_quantidade_tributada_icms_monofasico_retido_anteriormente = extract_value(item, "./qBCMonRet")
        self.valor_total_icms_monofasico_retido_anteriormente = extract_value(item, "./vICMSMonRet")
        self.valor_total_produtos_servicos = extract_value(item, "./vProd")
        self.valor_total_frete = extract_value(item, "./vFrete")
        self.valor_total_seguro = extract_value(item, "./vSeg")
        self.valor_total_desconto = extract_value(item, "./vDesc")
        self.valor_total_ii = extract_value(item, "./vII")
        self.valor_total_ipi = extract_value(item, "./vIPI")
        self.valor_total_ipi_devolvido = extract_value(item, "./vIPIDevol")
        self.valor_total_pis = extract_value(item, "./vPIS")
        self.valor_total_cofins = extract_value(item, "./vCOFINS")
        self.outras_despesas_acessorias = extract_value(item, "./vOutro")
        self.valor_total_nfe = extract_value(item, "./vNF")
        self.valor_estimado_total_impostos_federais_estaduais_municipais = extract_value(item, "vTotTrib")

    def to_dict(self):
        return self.__dict__
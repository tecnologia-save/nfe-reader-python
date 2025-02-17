from process.util import extract_value

class ICMS:
    def __init__(self, item, grupo):
        """
        Inicializa a classe ICMS extraindo valores do XML.

        Args:
            item: Elemento XML contendo os dados do ICMS.
            grupo: Grupo do ICMS.
            produto: ID do produto associado.
            nota_fiscal: ID da nota fiscal associada.
            cliente: ID do cliente associado.
            created_by: ID do usuário que criou o registro.
        """
        self.grupo = grupo
        
        self.origem_mercadoria = extract_value(item, f"./{grupo}/orig")
        if not self.origem_mercadoria:
            self.origem_mercadoria = extract_value(item, f"./{grupo}/Orig")
        
        self.tributacao_icms = extract_value(item, f"./{grupo}/CST")
        self.tributacao_icms_simples_nacional = extract_value(item, f"./{grupo}/CSOSN")
        self.modalidade_de_determinacao_da_bc_do_icms = extract_value(item, f"./{grupo}/modBC")
        self.valor_da_bc_do_icms = extract_value(item, f"./{grupo}/vBC")
        self.aliquota_do_icms = extract_value(item, f"./{grupo}/pICMS")
        self.valor_do_icms = extract_value(item, f"./{grupo}/vICMS")
        self.modalidade_de_determinacao_da_bc_do_icms_st = extract_value(item, f"./{grupo}/modBCST")
        self.percentual_de_margem_de_valor_adicionado_icms_st = extract_value(item, f"./{grupo}/pMVAST")
        self.percentual_da_reducao_de_base_de_calculo_icms_st = extract_value(item, f"./{grupo}/pRedBCST")
        self.valor_da_bc_do_icms_st = extract_value(item, f"./{grupo}/vBCST")
        self.aliquota_do_icms_st = extract_value(item, f"./{grupo}/pICMSST")
        self.valor_do_icms_st = extract_value(item, f"./{grupo}/vICMSST")
        self.valor_do_icms_st_retido = extract_value(item, f"./{grupo}/vICMSSTRet")
        self.percentual_da_reducao_de_base_de_calculo = extract_value(item, f"./{grupo}/pRedBC")
        self.motivo_da_desoneracao_do_icms = extract_value(item, f"./{grupo}/motDesICMS")
        self.valor_do_icms_desonerado = extract_value(item, f"./{grupo}/vICMSDeson")
        self.valor_icms_da_operacao = extract_value(item, f"./{grupo}/vICMSOp")
        self.percentual_do_diferimento = extract_value(item, f"./{grupo}/pDif")
        self.valor_do_icms_diferido = extract_value(item, f"./{grupo}/vICMSDif")
        self.percentual_da_bc_operacao_propria = extract_value(item, f"./{grupo}/pBCOp")
        self.uf_para_quem_e_devido_o_icms_st = extract_value(item, f"./{grupo}/UFST")
        self.valor_da_bc_do_icms_st_da_uf_de_destino = extract_value(item, f"./{grupo}/vBCSTDest")
        self.aliquota_aplicavel_de_calculo_do_credito = extract_value(item, f"./{grupo}/pCredSN")
        self.valor_credito_icms_que_pode_ser_aproveitado = extract_value(item, f"./{grupo}/vCredICMSSN")
        self.percentual_do_fundo_de_combate_a_pobreza = extract_value(item, f"./{grupo}/pFCP")
        self.valor_bc_do_fcp = extract_value(item, f"./{grupo}/vFCP")
        self.valor_bc_do_fcp_st = extract_value(item, f"./{grupo}/vBCFCPST")
        self.percentual_fcp_retido_por_st = extract_value(item, f"./{grupo}/pFCPST")
        self.valor_do_fcp_retido_por_st = extract_value(item, f"./{grupo}/vFCPST")
        self.aliquota_suportada_pelo_consumidor_final = extract_value(item, f"./{grupo}/pSTs")
        self.valor_icms_proprio_do_substituto = extract_value(item, f"./{grupo}/vICMSSubstituto")
        self.valor_bc_do_fco_retido_anteriormente_por_st = extract_value(item, f"./{grupo}/vBCFCPSTRet")
        self.percentual_fcp_retido_anteriormente_por_st = extract_value(item, f"./{grupo}/pFCPSTRet")
        self.valor_fcb_retido_por_st = extract_value(item, f"./{grupo}/vFCPSTRet")
        self.gerar_icms_st = extract_value(item, f"./{grupo}/gerarICMSST")
        self.percentual_da_reducao_da_bc_efetiva = extract_value(item, f"./{grupo}/pRedBCEfet")
        self.valor_bc_efetiva = extract_value(item, f"./{grupo}/vBCEfet")
        self.aliquota_icms_efetiva = extract_value(item, f"./{grupo}/pICMSEfet")
        self.valor_icms_efetivo = extract_value(item, f"./{grupo}/vICMSEfet")
        self.desconto_icms_desonerado_total_nota = extract_value(item, f"./{grupo}/digitacaoDescICMSDeson")
        self.valor_icms_st_desonerado = extract_value(item, f"./{grupo}/vICMSSTDeson")
        self.motivo_desoneracao_icms_st = extract_value(item, f"./{grupo}/motDesICMSST")
        self.percentual_difereminto_icms_relatiovo_ao_fcb = extract_value(item, f"./{grupo}/pFCPDif")
        self.valor_icms_relativo_ao_fcb_diferido = extract_value(item, f"./{grupo}/vFCPDif")
        self.valor_icms_relativo_ao_fcb_realmente_devido = extract_value(item, f"./{grupo}/vFCPEfet")
        self.quantidade_tributada = extract_value(item, f"./{grupo}/qBCMono")
        self.aliquota_ad_rem_do_imposto = extract_value(item, f"./{grupo}/adRemICMS")
        self.valor_do_icms_proprio = extract_value(item, f"./{grupo}/vICMSMono")
        self.quantidade_tributada_sugeita_a_retencao = extract_value(item, f"./{grupo}/qBCMonoReten")
        self.aliquota_ad_rem_do_imposto_com_retencao = extract_value(item, f"./{grupo}/adRemICMSReten")
        self.valor_do_icms_com_retencao = extract_value(item, f"./{grupo}/vICMSMonoReten")
        self.percentual_de_reducao_valor_aliquota_adren_do_icms = extract_value(item, f"./{grupo}/pRedAdRem")
        self.motivo_reducao_adrem = extract_value(item, f"./{grupo}/motRedAdRem")
        self.quantidade_tributada_diferida = extract_value(item, f"./{grupo}/qBMonoDif")
        self.aliquota_ad_rem_do_imposto_diferida = extract_value(item, f"./{grupo}/adRemICMSDif")
        self.valor_do_icms_diferido_multiplicacao = extract_value(item, f"./{grupo}/vICMSMonoDif")
        self.quantidade_tributada_retida_anteriormente = extract_value(item, f"./{grupo}/qBCMonoRet")
        self.aliquota_ad_rem_do_imposto_retida_anteriormente = extract_value(item, f"./{grupo}/adRemICMSRet")
        self.valor_do_icms_retido_anteriormente = extract_value(item, f"./{grupo}/vICMSMonoRet")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__

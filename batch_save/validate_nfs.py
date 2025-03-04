from batch_save.exceptions.invalid_json_exception import InvalidJsonException

class ValidateNFs:

    def __init__(self, notas_fiscais):
        self.notas_fiscais = notas_fiscais

    def validate(self):
        notas_validas = []
        notas_invalidas = []

        for nf in self.notas_fiscais:
            try:
                self.realiza_validacoes(nf)
                notas_validas.append(nf)
            except InvalidJsonException as ex:
                notas_invalidas.append({
                    "nota_fiscal": nf,
                    "mensagem": str(ex)
                })
            
        return notas_validas, notas_invalidas
    
    

    def realiza_validacoes(self,nf):

        self._verifica_campos_obrigatorios(['chave'], nf)

        if 'emitente' in nf:
            self.validar_entidade(nf['emitente'])

        if 'destinatario' in nf:
            self.validar_entidade(nf['destinatario'])

        if 'produtos' in nf:
            for produto in nf['produtos']:
                self.validar_produto(produto)

                if 'imposto' in produto:

                    if 'cofins_prnotas_invalidasoduto' in produto['imposto']:
                        self.validar_cofins_produto(produto['imposto']['cofins_produto'])
                    
                    if 'icms_produto' in produto['imposto']:
                        self.validar_icms_produto(produto['imposto']['icms_produto'])
                                
                    if 'pis_produto'  in produto['imposto']:
                        self.validar_pis_produto(produto['imposto']['pis_produto'])
                    
                    if 'issqn_produto' in produto['imposto']:
                        self.validar_issqn_produto(produto['imposto']['issqn_produto'])

                    if 'cofins_st_produto' in produto['imposto']:
                        self.validar_cofinsst_produto(produto['imposto']['cofins_st_produto'])

                    if 'ipi_produto' in produto['imposto']:
                        self.validar_ipi_produto(produto['imposto']['ipi_produto'])

                    if 'imposto_importacao_produto' in produto['imposto']:
                        self.validar_ii_produto(produto['imposto']['imposto_importacao_produto'])

                    if 'imposto_devolucao_produto' in produto['imposto']:
                        self.validar_imposto_devol_produto(produto['imposto']['imposto_devolucao_produto'])

        if 'totais' in nf:
            if 'total_icms' in nf['totais']:
                self.validar_total_icms(nf['totais']['total_icms'])
            if 'total_issqn' in nf['totais']:
                self.validar_total_issq(nf['totais']['total_issqn'])
            if 'total_retencao_tributos_federais' in nf['totais']:
                self.validar_total_retencao_tributos_federais(nf['totais']['total_retencao_tributos_federais'])


        if 'fatura' in nf:
            self.validar_fatura(nf['fatura'])

            if 'duplicatas' in nf['fatura']:
                for duplicata in nf['fatura']['duplicatas']:
                    self.validar_duplicatas(duplicata)

        if 'informacoes_resp_tecnico' in nf:
            self.validar_reponsavel_tecnico(nf['informacoes_resp_tecnico'])

        if 'transp' in nf:
            self.validar_transporte_nfe(nf['transp'])

    def _verifica_campos_obrigatorios(self, campos_obrigatorios, dicionario):
        for campo in campos_obrigatorios:
            if campo not in dicionario:
                raise InvalidJsonException(f'O campo {campo} é obrigatório')
            elif len(dicionario[campo]) < 1:
                raise InvalidJsonException(f'O campo {campo} está vazio')

    #####################################

    def validar_entidade(self, entidade):
        campos_obrigatorios = []

    def validar_nota_fiscal(self, nota_fiscal):
        campos_obrigatorios = ['numero_nfe', 'serie', 'chave', 'natureza_operacao', 'data_emissao']
        self._verifica_campos_obrigatorios(campos_obrigatorios, nota_fiscal)
    
    def validar_produto(self, produto):
        campos_obrigatorios = ['codigo_produto', 'descricao_produto', 'unidade_tributavel']
        self._verifica_campos_obrigatorios(campos_obrigatorios, produto)
    
    def validar_cofins_produto(self, item):
        campos_obrigatorios = ['codigo_situacao_tributaria', 'grupo']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)
    
    def validar_pis_produto(self, item):
        campos_obrigatorios = ['codigo_situacao_tributaria', 'grupo']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_issqn_produto(self, item):
        campos_obrigatorios = ['valor_da_base_de_calculo', 'valor_aliquota_do_isssqn', 'indicador_de_iss_retido', 'codigo_municipio_gerador_do_issqn']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_cofinsst_produto(self, item):
        campos_obrigatorios = ['grupo', 'codigo_situacao_tributaria']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_icms_produto(self, item):
        campos_obrigatorios = ['grupo', 'origem_mercadoria']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_ipi_produto(self, item):
        campos_obrigatorios = ['codigo_de_enquadramento_legal', 'ipi_tributado', 'codigo_situacao_tributaria']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_ii_produto(self, item):
        campos_obrigatorios = ['valor_base_imposto_importacao', 'valor_das_despesas_aduaneiras', 'valor_imposto_importacao', 'valor_iof']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_imposto_devol_produto(self, item):
        campos_obrigatorios = []
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_total_icms(self, item):
        campos_obrigatorios = ['base_calculo_icms', 'valor_total_icms']
        self._verifica_campos_obrigatorios(campos_obrigatorios, item)

    def validar_total_issq(self, total_issq):
        campos_obrigatorios = ['data_prestacao_servico']
        self._verifica_campos_obrigatorios(campos_obrigatorios, total_issq)

    def validar_total_retencao_tributos_federais(self, total_retencao_tributos_federais):
        campos_obrigatorios = ['valor_total_retencao_tributos_federais']
        self._verifica_campos_obrigatorios(campos_obrigatorios, total_retencao_tributos_federais)
    
    def validar_fatura(self, fatura):
        campos_obrigatorios = ['numero_fatura', 'valor_original', 'valor_desconto', 'valor_liquido']
        self._verifica_campos_obrigatorios(campos_obrigatorios, fatura)
        
    def validar_duplicatas(self, duplicatas):
        campos_obrigatorios = ['valor_duplicata', 'data_vencimento', 'numero_duplicata']    
        self._verifica_campos_obrigatorios(campos_obrigatorios, duplicatas)

    def validar_reponsavel_tecnico(self, responsavel_tecnico):
        campos_obrigatorios = []
        self._verifica_campos_obrigatorios(campos_obrigatorios, responsavel_tecnico)

    def validar_transporte_nfe(self, transporte_nfe):
        campos_obrigatorios = ['modo_de_frete', 'descricao_modo_de_frete']    
        self._verifica_campos_obrigatorios(campos_obrigatorios, transporte_nfe)


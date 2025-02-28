from process.util import extract_value

class TotalRetencaoTributosFederais:
    def __init__(self, item):
        self.valor_retido_pis = extract_value(item, "./vRetPIS")
        self.valor_retido_cofins = extract_value(item, "./vRetCOFINS")
        self.valor_retido_csll = extract_value(item, "./vRetCSLL")
        self.base_do_calculo_irrf = extract_value(item, "./vBCIRRF")
        self.valor_retido_irrf = extract_value(item, "./vIRRF")
        self.base_do_calculo_ret_prev = extract_value(item, "./vBCRetPrev")
        self.valor_retido_prev = extract_value(item, "./vRetPrev")

    def to_dict(self):
        return self.__dict__

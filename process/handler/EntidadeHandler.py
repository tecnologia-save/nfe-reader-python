from process.mapping.Entidade import Entidade

class EntidadeHandler:
    def __init__(self, root):
        self.root = root

    def process(self):

        emit_element = self.root.xpath(".//emit")
        final_dict = {}

        if emit_element:
            emit_element = emit_element[0]
            emitente = Entidade(emit_element)
            final_dict.update({'emitente': emitente.to_dict()})

        dest_element = self.root.xpath(".//dest")
        if dest_element:
            dest_element = dest_element[0]
            destinatario = Entidade(dest_element)
            final_dict.update({'destinatario': destinatario.to_dict()})

        exped_element = self.root.xpath(".//exped")
        if exped_element:
            exped_element = exped_element[0]
            expedidor = Entidade(exped_element)
            final_dict.update({'expedidor': expedidor.to_dict()})


        return final_dict



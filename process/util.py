def extract_value(xml_element, xpath):
    result = xml_element.xpath(xpath)
    return result[0].text if result else None



def remove_namespaces(tree):
    """
    Remove os namespaces do XML para simplificar o acesso aos elementos.
    """
    for elem in tree.getiterator():
        if elem.tag.startswith("{"):
            elem.tag = elem.tag.split("}", 1)[1]  # Remove o namespace
    return tree
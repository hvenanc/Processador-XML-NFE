def elements_text(nfe,tag):

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data
    
    return element

def elements_number(nfe,tag):

    elements = []

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data
    elements.append(float(element))

    return elements

def elements_date(nfe,tag):

    elements = []

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data
    elements.append(formatar_data(element))

    return elements

def formatar_data(data):

    return data[8:10] + '/' + data[5:7] + '/' +data[0:4]
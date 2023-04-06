def elements_text(nfe,tag):

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data
    
    return element

def elements_number(nfe,tag):

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data

    return float(element)

def elements_date(nfe,tag):

    element = nfe.getElementsByTagName(tag)
    element = element[0].firstChild.data

    return formatar_data(element)

def formatar_data(data):

    return data[8:10] + '/' + data[5:7] + '/' +data[0:4]
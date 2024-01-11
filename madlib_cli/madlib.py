def read_template(txt):  

    file = open(txt)

    contents = file.read()

    file.close()

    return(contents)
    

def parse_template(template):
    
    new_template = template

    split_template = new_template.split()

    removed_terms = []

    for i in split_template:
        if i == '{Adjective}':
            removed_terms.append('Adjective')
            new_template = new_template.replace( '{Adjective}', '{}')
        
        if i == '{Noun}.':
            removed_terms.append('Noun')
            new_template = new_template.replace('{Noun}.', '{}.')

    terms = tuple(removed_terms)

    return new_template, terms

def merge(template, terms):

    words_to_replace = terms

    new_template = template

    for i in words_to_replace:
        new_template = new_template.replace('{}', f'{i}', 1)
    
    return new_template




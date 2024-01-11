def read_template(txt):
    if txt == 'assets/dark_and_stormy_night_template.txt':

        file = open('./assets/dark_and_stormy_night_template.txt')

        contents = file.read()

        file.close()

        return(contents)
    
    else:
        return None

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


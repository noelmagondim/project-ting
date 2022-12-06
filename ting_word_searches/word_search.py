def exists_word(word, instance):
    occurrencies = []
    for index in range(len(instance)):
        file = instance.search(index)

        data = [
            {'linha': (index + 1)}
            for index, line in enumerate(file['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        new_occurrencies = {
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': data,
        }

        if len(new_occurrencies['ocorrencias']) <= 0:
            return []
        else:
            occurrencies.append(new_occurrencies)
        return occurrencies


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

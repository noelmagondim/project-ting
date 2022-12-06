import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data = txt_importer(path_file)
    new_dict = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    }
    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None
    instance.enqueue(new_dict)
    print(new_dict)


def remove(instance):
    if not len(instance):
        return sys.stdout.write('Não há elementos\n')
    else:
        del_queue = instance.dequeue()
        sys.stdout.write(
            f'Arquivo {del_queue["nome_do_arquivo"]} removido com sucesso\n'
        )


def file_metadata(instance, position):
    try:
        info = instance.search(position)
        sys.stdout.write(str(info))
    except IndexError:
        sys.stderr.write('Posição inválida\n')

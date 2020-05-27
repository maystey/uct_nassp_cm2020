import sys
import os
import os.path as op

from jupyter_pdfbook.build import _MasterTexDocument
from ruamel.yaml import safe_load

def update_sty(path_pdf_out):
    #Making the sty files
    os.system(('cp ~/Projects/JupyterBooks/PDF\ Book/jupyter_pdfbook/templates/jupyterpdfbook.sty'
                f' {path_pdf_out}'))

    nbsty = _MasterTexDocument._prepare_nb_sty()

    with open(op.join(path_pdf_out,'nbconvert.sty'), 'w') as f:
        f.write(nbsty)

def load_yaml():
    with open('_data/toc.yml', 'r') as f:
        toc = safe_load(f)
    with open('_config.yml', 'r') as f:
        config = safe_load(f)
    return config, toc

def get_suffix():
    suff = ''
    if len(sys.argv) > 1:
        suff = sys.argv[1]
    return suff

def old_main():
    update_sty('./pdf')
    #Making the tex file
    suff = get_suffix()

    config, toc = load_yaml()

    preamble = '\n\\renewcommand{\\includepdf}[1]{File: #1}\n'

    master_tex = _MasterTexDocument(toc = toc, site_yaml=config,
                                    custom_preamble= preamble)
    
    filename = f'pdf/book{suff}.tex' 
    print('Writing', filename)
    with open(filename, 'w') as f:
        f.write(master_tex.get_tex())

def main():
    suff = get_suffix()
    folder = f'./pdf/book{suff}'

    config, toc = load_yaml()
    master_tex = _MasterTexDocument(toc = toc, site_yaml=config,
                                    pdf_path=folder)

    #Making a page
    # master_tex._make_tex_contents_dir()
    # master_tex._add_page_to_contents('/intro')
    
    filename = op.join(folder, 'book.tex')
    print('Writing', filename)
    with open(filename, 'w') as f:
        f.write(master_tex.get_tex())

    update_sty(folder)

def make_page():
    suff = get_suffix()
    folder = f'./pdf/book{suff}'

    config, toc = load_yaml()
    master_tex = _MasterTexDocument(site_yaml=config,
                                    pdf_path=folder)

    master_tex._make_tex_contents_dir()
    master_tex._add_page_to_contents('/intro', 'Intro')

if __name__ == '__main__':
    main()
    # make_page()
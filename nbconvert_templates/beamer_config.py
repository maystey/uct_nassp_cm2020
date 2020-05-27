import os
import os.path as op

from traitlets.config import Config

from nbconvert.preprocessors import Preprocessor

import nbformat as nbf

from .preprocessors.html_to_latex import HTMLToLatexTablePreprocessor


FILE_PATH = op.relpath(op.abspath(__file__), os.getcwd())
MODULE_PATH = '.'.join(FILE_PATH.strip('.py').split('/'))
# MODULE_PARENT_PATH = '.'.join(FILE_PATH.split('/')[:-1])

class BeamerPrepareSlidesPreprocessor(Preprocessor):
    """
    Adds raw cells with begin and end frame commands.
    Removes cells with the 'skip' slide type.

    TODO notes, fragment
    """

    CELL_BEGIN_FRAME = nbf.v4.new_raw_cell('\\begin{frame}[fragile]\n')
    CELL_END_FRAME = nbf.v4.new_raw_cell('\\end{frame}\n\n')

    def preprocess(self, nb, resources):
        new_cells = []
        is_slide_open = False

        for cell in nb.cells:
            if not cell['metadata'].get('slideshow'):
                new_cells.append(cell)
                continue
            
            slide_type = cell['metadata']['slideshow'].get('slide_type')
            
            if slide_type in ['slide', 'subslide']:
                if is_slide_open:
                    new_cells.append(self.CELL_END_FRAME)

                new_cells.append(self.CELL_BEGIN_FRAME)
                new_cells.append(cell)
                is_slide_open = True
            # elif slide_type == 'skip':
            #implicitly ignoring other slide types for now

        if is_slide_open:
            new_cells.append(self.CELL_END_FRAME)                  

        nb.cells = new_cells

        return nb, resources
    

def get_beamer_config():
    c = Config()

    c.RegexRemovePreprocessor.patterns = ['\\s*\\Z']

    c.LatexExporter.preprocessors = [
        'nbconvert.preprocessors.RegexRemovePreprocessor',
        f'{MODULE_PATH}.BeamerPrepareSlidesPreprocessor',
        f'{MODULE_PATH}.HTMLToLatexTablePreprocessor'
        ]

    c.LatexExporter.template_path = ['.' , op.dirname(op.abspath(__file__))]
    c.LatexExporter.template_file = 'beamer.tplx'

    return c

if __name__ == '__main__':
    c = get_beamer_config()
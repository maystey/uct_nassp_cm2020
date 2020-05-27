from nbconvert_templates.beamer_config import get_beamer_config

import os.path as op
import os

import re

from datetime import datetime

from traitlets.config import Config
from traitlets import List, Unicode

from nbconvert.exporters import LatexExporter, PDFExporter
from nbconvert.writers import FilesWriter
from nbconvert.preprocessors import Preprocessor

import nbformat as nbf

# Pre-pre processors                

class LatexEquationUnnestPreprocessor(Preprocessor):
    """

    Values in equation environment to be used in a regex pattern,
    format accordingly
    """
    equation_environments = List(trait = Unicode(), default_value = [],
                                help = 'The equation environments not to be nested'
                                ).tag(config = True)

    RE_FLAGS = re.MULTILINE+re.DOTALL

    def preprocess(self, nb, resources):
        if len(self.equation_environments) == 0:
            return nb, resources
        
        for env in self.equation_environments:
            pattern = (r'\$\$\n*(\\begin\{'
                        f'{env}'
                        r'\}.*'
                        r'\\end\{'
                        f'{env}'
                        r'\})\n*\$\$')

            new_cells = []

            for cell in nb.cells:
                if cell.get('cell_type') == 'markdown':
                    match = re.search(pattern, cell.get('source', ''),
                                        flags= self.RE_FLAGS)
                    
                    while match:
                        #source before equation
                        new_cell = dict(cell)
                        new_cell['source'] = new_cell['source'][:match.start()]
                        new_cells.append(new_cell)

                        #Store equation in a raw cell
                        #TODO give this a text/latex mime/type?
                        eqn_cell = nbf.v4.new_raw_cell(match.groups()[0])
                        new_cells.append(eqn_cell)

                        #source after equation
                        new_cell = dict(cell)
                        new_cell['source'] = new_cell['source'][match.end():]
                        new_cells.append(new_cell)

                        #Next match
                        cell['source'] = cell['source'][match.end():]
                        match = re.search(pattern, cell['source'],
                                            flags = self.RE_FLAGS)

                #     new_cells.append(cell)
                # else:
                new_cells.append(cell)
            
            nb.cells = new_cells
        
        return nb, resources


# Helper functions
def _make_dir(path):
    if not op.isdir(path):
        os.makedirs(path)

def _is_newer(file_path1, file_path2):
    if not op.isfile(file_path1):
        return False
    
    if not op.isfile(file_path2):
        return True
    
    return op.getmtime(file_path1) > op.getmtime(file_path2)

def _export(doc_name, nb_name, nb_path, file_writer, pdf_exporter = None, 
            latex_exporter = None, export_log = {}, export_subdir = None):
    """
    Export the document to PDF format or, failing that, placing the LaTeX files
    in the 'manual' directory.
    """
    if not (nb_name.startswith(doc_name) 
            and nb_name.endswith('.ipynb')):
        return
    nb_name = nb_name.strip('.ipynb')
    if export_subdir:
        export_path = op.join('.', 'exports', export_subdir, nb_name)
    else:
        export_path = op.join('.', 'exports', f'{doc_name}s', nb_name)

    #check if the file in the export location is newer than 
    # the notebook before exporting
    is_export_exists = op.isdir(export_path)
    
    print(export_path)
    # nb_export = pdf_exporter.from_file(nb_path)
    # file_writer.write(*nb_export, notebook_name=export_path)
    try:
        nb_export = pdf_exporter.from_file(nb_path)
        file_writer.write(*nb_export, notebook_name=export_path)

        if is_export_exists:
            export_log.get('updated', []).append(nb_name)
        else:
            export_log.get('new', []).append(nb_name)
    except FileNotFoundError:
        print('Either one or both of the files not found:', nb_path, export_path)

	# Add latex file to manual exports if it failed to write the pdf
    export_path = op.join('.', 'exports', 'manual', f'{doc_name}s', nb_name)
    _make_dir(export_path)
    export_path = op.join(export_path, nb_name)

    nb_latex = latex_exporter.from_file(nb_path)
    file_writer.write(*nb_latex, notebook_name=export_path)


def _log_list(file_object, log_list, title = ''):
    """
    For adding a list to the log file
    """
    
    file_object.write(title)

    for log in log_list:
        file_object.write(log)
        file_object.write('\n')

def _doc_config():
    c = Config()

    # Remove any cells that are *only* whitespace
    c.RegexRemovePreprocessor.patterns = ["\\s*\\Z"]

    c.TemplateExporter.preprocessors = [
        'nbconvert.preprocessors.RegexRemovePreprocessor'
    ]

    c.LatexEquationUnnestPreprocessor.equation_environments = [r'align\*']

    c.LatexExporter.preprocessors = [
        'batch_export.LatexEquationUnnestPreprocessor'
    ]

    # print(op.abspath(op.join('.', 'nbconvert_templates')))
    c.LatexExporter.template_path = ['.' , op.abspath(op.join('.', 'nbconvert_templates'))]
    c.LatexExporter.template_file = 'no_section_numbers.tplx' #'no_section_numbers'
    
    return c

def main():
    doc_config = _doc_config()
    doc_pdf_exporter = PDFExporter(config = doc_config)
    doc_latex_exporter = LatexExporter(config = doc_config)

    doc_writer = FilesWriter()

    #Writing out projects
    nb_name = 'comparison.ipynb'
    nb_path = op.join('.', 'content', 'root-finding', nb_name)

    _export('comparison', nb_name, nb_path,
            file_writer= doc_writer,
            pdf_exporter= doc_pdf_exporter,
            latex_exporter= doc_latex_exporter,
            export_subdir = '')


if __name__ == "__main__":
    main()

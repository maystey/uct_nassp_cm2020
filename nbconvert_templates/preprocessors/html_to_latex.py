from nbconvert.preprocessors import Preprocessor
import nbformat as nbf

import re
#TODO The regex turned into a bit of a mess, maybe I should replace it with BeautifulSoup

from .utils import iterative_match, SplitCellBase


def convert_code_tags(text):
    #TODO make more robust to deal with attributes
    text = text.replace('<code>', '\\texttt{')
    text = text.replace('</code>', '}')
    return text

#TODO convert tag attributes

class _TableSplitCell(SplitCellBase):

    def _format_match(self, match):
        table_begin = r'\begin{longtable}{@{}'
        
        # rows = re.findall(r'<tr>(.*)</tr>', match.groups()[0], 
        #                 flags = re.DOTALL+re.MULTILINE)

        rows = match.groups()[0].split('</tr>')
        rows = rows[:-1]

        ncols = 0

        is_header_open = True

        table_body = '\\toprule\n'


        for row in rows:
            row = row.lstrip()
            row = row.lstrip('<tr>')
            # print('-', row)
            #iterate through columns
            #record information about whether the column
            # is a header or not
            #rows of only headers becomes a header row,
            # other formatting needs to be considered for
            # other cases

            #Also determine how many columns there are from this,
            # a second pass might have to be applied for padding
            
            parse_row = _ParseRow()
            iterative_match(_ParseRow.RE_PATTERN, row, parse_row,
                            flags = re.MULTILINE)
            
            table_body += parse_row.get_row_tex()

            if parse_row.is_header and is_header_open:
                table_body += '\\midrule\n\\endhead\n'
            
            if len(parse_row.columns) > 0:
                ncols = len(parse_row.columns)
        
        table_begin += 'l'*ncols +'@{}}\n'

        table_end = '\\bottomrule\n\\end{longtable}\n\n'

        table_cell = nbf.v4.new_raw_cell(
                    table_begin + table_body + table_end
                )
        self.new_cells.append(table_cell)


class _ParseRow:
    """
    Use to match columns and header columns
    """

    #first group tells you if it's a heading or column
    #second group is content
    RE_PATTERN = r'<t([dh])[^>]*>(.*)</t[dh]>'


    def __init__(self, table_body = None):
        if table_body:
            self.table = table_body
        else:
            self.table = ''
        
        self.columns = []

        self.is_header = False
    

    def __call__(self, text, match):
        # print(match.groups())
        self.is_header =  match.groups()[0] == 'h'
        
        row_content = match.groups()[1]
        row_content = convert_code_tags(row_content)
        
        self.columns.append(row_content)

        return text[match.end():]


    def get_row_tex(self):
        return (self.table + '&'.join(self.columns)
                + '\\tabularnewline\n')

class HTMLToLatexTablePreprocessor(Preprocessor):
    """
    Converts HTML tables directly to raw LaTeX. Pandoc does not handle this well.

    Cells are split up wherever the table is found.
    """

    RE_PATTERN = r'\<table\>(.*)\<\/table\>'

    RE_FLAGS = re.DOTALL+re.MULTILINE

    def preprocess(self, nb, resources):
        new_cells = []

        for cell in nb.cells:
            table_split = _TableSplitCell(cell, new_cells)
            iterative_match(self.RE_PATTERN, cell.get('source', ''),
                            table_split, self.RE_FLAGS)
            # match = re.search(self.RE_PATTERN, cell.get('source', ''), self.RE_FLAGS)

            # while match:
            #     pre_cell = dict(cell)
            #     pre_cell['source'] = pre_cell['source'][:match.start()]
            #     new_cells.append(pre_cell)

            #     table_cell = nbf.v4.new_raw_cell(
            #         cell['source'][match.start():match.end()]
            #     )
            #     new_cells.append(table_cell)

            #     cell['source'] = cell['source'][match.end():]

            #     match = re.search(self.RE_PATTERN, cell.get('source', ''), self.RE_FLAGS)
            
            new_cells = table_split.new_cells #TODO: this might not be necessary
            new_cells.append(table_split.cell) #TODO: ditto
        
        nb.cells = new_cells
        return nb, resources
    
    @staticmethod
    def parse_table_row(row):
        pass
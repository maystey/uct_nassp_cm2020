import re

def iterative_match(pattern, text, method, flags):
    """
    method - callable, returns updated text
    """

    match = re.search(pattern, text, flags)

    while match:
        text = method(text, match)
        match = re.search(pattern, text, flags)


class SplitCellBase:
    """
    To be used as the method in iterative match,
    how do I make that more explicit?
    """

    def __init__(self, cell, new_cells = None):
        
        self.cell = cell
        
        if new_cells:
            self.new_cells = new_cells
        else:
            self.new_cells = []
    
    def __call__(self, text, match):
        pre_cell = dict(self.cell)
        pre_cell['source'] = pre_cell['source'][:match.start()]
        self.new_cells.append(pre_cell)

        self._format_match(match)

        self.cell['source'] = self.cell['source'][match.end():]

        return self.cell['source']

    def _format_match(self, match):
        raise NotImplementedError
import argparse
import itertools


class custom_parser(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(custom_parser, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if namespace.file is not None:
            self.finalize(namespace)
        namespace.file = values

    @staticmethod
    def finalize(namespace):
        if not hasattr(namespace, "files"):
            namespace.files = []
        chained_lines = namespace.lines
        chained_lines_in_between = namespace.linesInBetween
        if chained_lines is not None:
            chained_lines = list(itertools.chain(*namespace.lines))
            chained_lines.sort()
            # TODO: remove duplicates
        if chained_lines_in_between is not None:
            chained_lines_in_between = list(itertools.chain(*namespace.linesInBetween))
            chained_lines_in_between.sort(key=lambda x: int(x.split('-')[0]))
            # TODO: remove duplicates and normalize the lines
        namespace.files.append(
            {"fileName": namespace.file,
             "lines": chained_lines,
             "linesInBetween": chained_lines_in_between})
        namespace.lines = None
        namespace.linesInBetween = None

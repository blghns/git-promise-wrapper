import argparse
import itertools


class customParser(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(customParser, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if namespace.file is not None:
            self.finalize(namespace)
        namespace.file = values

    @staticmethod
    def finalize(namespace):
        if not hasattr(namespace, "files"):
            namespace.files = []
        chainedLines = namespace.lines
        chainedLinesInBetween = namespace.linesInBetween
        if chainedLines is not None:
            chainedLines = list(itertools.chain(*namespace.lines))
            chainedLines.sort()
            # TODO: remove duplicates
        if chainedLinesInBetween is not None:
            chainedLinesInBetween = list(itertools.chain(*namespace.linesInBetween))
            chainedLinesInBetween.sort(key=lambda x: int(x.split('-')[0]))
            # TODO: remove duplicates and normalize the lines
        namespace.files.append(
            {"fileName": namespace.file,
             "lines": chainedLines,
             "linesInBetween": chainedLinesInBetween})
        namespace.lines = None
        namespace.linesInBetween = None

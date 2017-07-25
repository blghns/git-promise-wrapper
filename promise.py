def promise_parser(custom_args=None):
    import argparse
    from helpers import parseFileArgs
    parser = argparse.ArgumentParser(description='Promise lines in git. GitVow backbone.')
    parser.add_argument('newBranchName', metavar='branch',
                        help='Name of the promise branch, if promise branch exist, append new promise lines.\n')

    group = parser.add_argument_group('optional line selection')
    group.add_argument('-f', '--file', metavar='name', dest='file', required=True, nargs='+',
                       action=parseFileArgs.custom_parser,
                       help='Name of the file to be promised. This file will be editable in the promised branch, '
                            'but will not be editable in the parent branch.\n')
    group.add_argument('-l', '--lines', metavar='N', dest='lines', nargs='+', type=int, action='append',
                       help='Lines in the specified file to be promised. If not specified, all file will be promised.\n')
    group.add_argument('-b', '--between', metavar='N-N', dest='linesInBetween', nargs='+', action='append',
                       help='Specify the range of lines to be promised in the selected file.\n')
    if custom_args is None:
        parsed_args = parser.parse_args()
    else:
        parsed_args = parser.parse_args(custom_args)
    parseFileArgs.custom_parser.finalize(parsed_args)
    return parsed_args


def promise_creator(parsed_args):
    import helpers.git as git
    if not git.branch_exists(parsed_args.newBranchName):
        import helpers.promise as promise
        promise.write_promise(parsed_args)
        git.add(".promise")
        git.commit("New promise for branch: " + parsed_args.newBranchName + " is created")
        git.branch(parsed_args.newBranchName)
        print "New promise for branch: " + parsed_args.newBranchName + " is created"
    else:
        # TODO: add a parser option to append to the promised branch
        print "Promised branch already exists!"


if __name__ == "__main__":
    args = promise_parser()
    promise_creator(args)

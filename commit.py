from helpers import git
import sys


def check_promise(promise, is_parent):
    promised_files = promise[u'files']
    promise_commit_hash = promise[u'hash']
    error_message = ''
    for file in promised_files:
        file_name = file[u'fileName']
        promised_lines = file[u'lines']
        promised_lines_between = file[u'linesInBetween']
        if promised_lines is None and promised_lines_between is None and is_parent:
            status, error_message = check_parent_promise(file_name)
        elif promised_lines is None and promised_lines_between is None:
            continue
        else:
            status, error_message = check_file(file_name, promised_lines, promised_lines_between, promise_commit_hash)
            if not status:
                return status, error_message
    return True, error_message


def check_parent_promise(file_name):
    if git.is_staged(file_name):
        return False, "%s is promised by a child branch. You cannot commit any changes to it." % file_name
    return True, ''


def check_file(file_name, promised_lines, promised_lines_between, promise_commit_hash):
    error_message = ''
    lines_edited = git.get_lines_edited(promise_commit_hash, file_name)
    # print file_name
    # print promised_lines
    # print promised_lines_between
    # print "Edited Lines: %s" % str(lines_edited)
    if lines_edited == []:
        return True, ''
    if promised_lines == None and promised_lines_between == None:
        return False, "Lines %s in %s are not promised." % (str(promised_lines), str(promised_lines_between))

    for line_edited in lines_edited:

        if "," in line_edited:
            line_edited = line_edited.split(',')
            if int(line_edited[1]) == 0:
                status, error_message = check_line(line_edited[0], promised_lines, file_name)
                if not status:
                    status, error_message = check_promised_range(line_edited[0], promised_lines_between, file_name)
                    if not status:
                        return False, error_message
            elif not promised_lines_between is None:
                line_edited = line_edited[0] + '-' + line_edited[1]
                for promisedRange in promised_lines_between:
                    if not check_ranges(line_edited, promisedRange, file_name)[0]:
                        return False, error_message
            else:
                line_edited = line_edited[0] + '-' + str(int(line_edited[0]) + int(line_edited[1]))
                return False, "Range %s in %s is not promised." % (line_edited, file_name)

        else:
            status, error_message = check_line(line_edited, promised_lines, file_name)
            if not status:
                return False, error_message

    return True, error_message


def check_line(line_edited, promised_lines, file_name):
    if not int(line_edited) in promised_lines:
        return False, "Line %s in %s is not promised." % (line_edited, file_name)
    return True, 'Line %s in %s is promised by a child branch.' % (line_edited, file_name)


def check_promised_range(line_edited, promised_ranges, file_name):
    if promised_ranges == None:
        return False, "Line %s in %s is not promised." % (line_edited, file_name)
    for promised_range in promised_ranges:
        line_edited = int(line_edited)
        promised_start = int(promised_range.split("-")[0])
        promised_end = int(promised_range.split("-")[1])
        if promised_start - line_edited > 0 or promised_end - line_edited < 0:
            return False, "Line %s in %s is not promised." % (line_edited, file_name)
    return True, "Line %s in %s is promised by a child branch." % (line_edited, file_name)


def check_ranges(edited_range, promised_range, file_name):
    promised_start = int(promised_range.split("-")[0])
    promised_end = int(promised_range.split("-")[1])
    edited_start = int(edited_range.split("-")[0])
    edited_end = int(edited_range.split("-")[1])
    if promised_start - edited_start <= 0 <= promised_end - edited_end:
        return True, "Line range %s in %s are promised in a child branch." % (edited_range, file_name)
    return False, "Line range %s in %s are not promised." % (edited_range, file_name)


def broken_promise(error_message):
    print "\nPromise not kept. Changes will not be committed."
    print "Error Message: %s" % error_message


def kept_promise(args):
    print "\nPromise was kept. Committing changes."
    git.commit_with_args(args)


def checking_and_committing(args=sys.argv[1:]):
    from helpers import promise
    print "Checking if promise was kept..."
    promises = promise.read_promise()
    promise_kept = True
    error_message = None
    current_branch = git.current_branch()
    for promise in promises:
        if promise_kept:

            if promise[u'child'] == current_branch:
                promise_kept, error_message = check_promise(promise, False)
            elif promise[u'parent'] == current_branch:
                promise_kept, error_message = check_promise(promise, True)
                promise_kept = not promise_kept
        else:
            broken_promise(error_message)

    if promise_kept:
        kept_promise(args)
        return True
    else:
        broken_promise(error_message)
        return False


if __name__ == '__main__':
    checking_and_committing()

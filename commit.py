from helpers import promise
from helpers import git

### Todo: Currently this function will only give error messages if the child branch is breaking its promise.
### This should be improvied to include parent branch errors.
def check_promise(promise, is_parent):
    promised_files = promise[u'files']
    promise_commit_hash = promise[u'hash']
    error_message = None
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

def check_parent_promise(file_name):
    if git.is_staged(file_name):
        return False, "%s is promised by a child branch. You cannot commit any changes to it." % file_name
    return True, None

def check_file(file_name, promised_lines, promised_lines_between, promise_commit_hash):
    lines_edited = git.get_lines_edited(promise_commit_hash, file_name)

    for line_edited in lines_edited:
        if "," in line_edited:
            line_edited = line_edited.split(',')
            if line_edited[1] == 0:
                if not check_line(line_edited[0]):
                    return False, error_message
            else:
                line_edited = line_edited[0] + '-' + line_edited[1]
                for promisedRange in promised_lines_between:
                    if not check_ranges(line_edited, promisedRange):
                        return False, error_message
        elif not check_line(line_edited, promised_lines) and not check_promised_range(line_edited, promised_lines_between):
            return False, error_message
    return True, None


def check_line(line_edited, promised_lines, file_name):
    if not int(line_edited) in promised_lines:
        return False, "Line %l in %s is not promised." % (line_edited, file_name)
    return True, None


def check_promised_range(line_edited, promised_range, file_name):
    for promised_range in promised_range:
        lined_edited = int(line_edited)
        promised_start = int(promised_range.split("-")[0])
        promised_end = int(promised_range.split("-")[1])
        if not promised_start - lined_edited <= 0 and promised_end - lined_edited >= 0:
            return False, "Line %s in %s is not promised." % (line_edited, file_name)
    return True, None


def check_ranges(edited_range, promised_range, file_name):
    promised_start = int(promised_range.split("-")[0])
    promised_end = int(promised_range.split("-")[1])
    edited_start = int(edited_range.split("-")[0])
    edited_end = int(edited_range.split("-")[1])
    if promised_start - edited_start <= 0 <= promised_end - edited_end:
        return True, None
    return False, "Line range %s in %s are not promised." % (edited_range, file_name)


print "Checking if promise was kept..."

promises = promise.read_promise()
promise_kept = True
error_message = None

for promise in promises:
    current_branch = git.current_branch()
    if promise[u'child'] ==  current_branch:
        promise_kept, error_message = check_promise(promise, False)
    elif promise[u'parent'] == current_branch:
        promise_kept, error_message == check_promise(promise, True)


if promise_kept:
    print "\nPromise was kept. Committing changes."
else:
    print "\nPromise not kept. Changes will not be committed."

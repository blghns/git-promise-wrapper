import json
import os
import helpers.__subprocess as sb
import helpers.git as git


# check if any promise exists,
#     if exists
#         check whether any of the promised lines overlap with the previous promises
#             if it exists
#                 return an error message
#              else
#                 append the promise to the previous promises
#     else
#         create promise file
# commit the new file

# check if the branch name exists, if it does, return an error message. (maybe git branch has a feature for this?)


def check_promise_overlaps(promises, promise):
    # TODO: implement this function - Steal check-promise from commit
    pass


def read_promise():
    with open('.promise') as promise_file:
        return json.load(promise_file)


def promise_exists():
    if os.path.isfile(".promise"):
        return True
    else:
        return False


def create_promise(args):
    hash_str = git.current_hash()
    parent = git.current_branch()
    if parent == "":
        raise Exception("Creating promise failed. Current branch has no name."
                        " If repo is just initialized, create an initial commit.")
    # TODO: check if promise is allowed if in a promise branch (promise in a promsie)
    promise = {"hash": hash_str,
               "parent": parent,
               "child": args.newBranchName,
               "files": args.files}
    return promise


def write_promise(args):
    promise = create_promise(args)
    if promise_exists():
        promises = read_promise()
        if check_promise_overlaps(promises, promise):
            raise Exception("Some lines are already promised to another branch")
        else:
            promises.append(promise)
    else:
        promises = [promise]
    write_promises(promises)


def write_promises(promises):
    with open('.promise', 'w') as promise_file:
        json.dump(promises, promise_file)

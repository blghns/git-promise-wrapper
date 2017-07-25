import json
import os
import helpers.__subprocess as sb


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
    # TODO: implement this function
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
    hash_command = "git rev-parse HEAD"
    hash_str = sb.make_call(hash_command).split("\n")[0]
    promise = {"hash": hash_str,
               "branch": args.newBranchName,
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
    with open('.promise', 'w') as promise_file:
        json.dump(promises, promise_file)



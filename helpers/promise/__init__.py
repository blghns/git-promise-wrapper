import os
import subprocess
import json


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
    pass


def read_promise():
    with open('data.json') as promise_file:
        return json.loads(promise_file)


def promise_exists():
    if os.path.isfile(".promise"):
        return True
    else:
        return False


def create_promise(args):
    hash_command = "git rev-parse HEAD"
    hash_process = subprocess.Popen(hash_command.split(),
                                    cwd=os.getcwd(),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    hash_str, error = hash_process.communicate()
    if error:
        raise error
    promise = {"hash": hash_str,
               "branch": args.newBranchName,
               "files": args.files}
    return promise


def write_promise(args):
    promise = create_promise(args)
    if promise_exists():
        promises = read_promise()
        if check_promise_overlaps(promises, promise):
            raise Exception("Promise already exists")
        else:
            promises.append(promise)
    else:
        promises = [promise]
    with open('.promise', 'w') as promise_file:
        json.dump(promises, promise_file)



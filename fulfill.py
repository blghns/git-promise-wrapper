# get current branch name
# get promise to be fulfilled name
# check if promise exists
# merge the branch
# remove the promise branch if option is specified
import argparse
import helpers.git as git
import helpers.promise as promise


def fulfill():
    parser = argparse.ArgumentParser(description='Fulfill a promise, merge it back to its parent.')
    parser.add_argument('branch', metavar="branch",
                        help='Name of the promise branch, if promise branch exist, merge the branch.\n')
    parser.add_argument('-d', dest="delete", action="store_const", const=True, default=False,
                        help='Delete the branch if this option is given after merge.\n')
    parsed_args = parser.parse_args()
    git.merge(parsed_args.branch)
    if parsed_args.delete:
        git.delete_branch(parsed_args.branch)
        all_promises = promise.read_promise()
        new_promises = []
        for the_promise in all_promises:
            if the_promise["child"] != parsed_args.branch:
                new_promises.append(the_promise)
        if len(new_promises) == 0:
            import os
            os.remove(".promise")
        else:
            promise.write_promises(new_promises)
        git.add(".promise")
        git.commit("Promise updated, removed branch " + parsed_args.branch)

    print "Promise fulfilled."

if __name__ == "__main__":
    fulfill()

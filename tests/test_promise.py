import unittest
import os
import promise
import helpers.git as git
import clear


class PromiseTester(unittest.TestCase):
    def test_1(self):
        clear.remove_test_dir()
        os.makedirs("promiseTest")
        os.chdir("promiseTest")
        git.init()
        with open("first", "w") as text:
            text.write("first")
        git.add("first")
        git.commit("first commit")
        current_hash = git.current_hash()
        args = promise.promise_parser("newBranch -f first -f second -l 1 -b 5-23".split())
        promise.promise_creator(args)
        self.assertTrue(git.branch_exists("newBranch"))
        with open(".promise") as promise_file:
            self.assertEqual(promise_file.read(), '[{"files": [{"lines": null, "linesInBetween": null, "fileName": '
                                                  '"first"}, {"lines": [1], "linesInBetween": ["5-23"], "fileName": '
                                                  '"second"}], "hash": "' + current_hash + '", "parent": "master", '
                                                                                           '"child": "newBranch"}]'
                             )


if __name__ == '__main__':
    unittest.main()

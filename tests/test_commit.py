import unittest
import os
import promise
import commit
import helpers.git as git
import clear


class PromiseTester(unittest.TestCase):
    def test_1(self):
        clear.remove_test_dir("commitTest/")
        os.makedirs("commitTest")
        os.chdir("commitTest")
        git.init()
        with open("first", "w") as text:
            text.write("1\n2\n3\n4\n5\n6\n")
        git.add("first")
        with open("second", "w") as text:
            text.write("1\n2\n3\n4\n5\n6\n")
        git.add("second")
        git.commit("first commit")
        args = promise.promise_parser("newBranch -f first -l 2 -b 4-6".split())
        promise.promise_creator(args)

        # Edit the parent branch with the child's promised line
        with open("first", "w") as text:
            text.write("1\n2-edited\n3\n4\n5\n6\n")
        current_hash = git.current_hash()
        result = commit.checking_and_commiting("-m 'this commit should not work'".split())
        new_hash = git.current_hash()

        self.assertEqual(False, result, "Parent shouldn't be able to commit.")
        self.assertEqual(current_hash, new_hash, "Parent shouldn't commit when a promised line is edited.")

        # Edit the child branch
        # Reset the


if __name__ == '__main__':
    unittest.main()

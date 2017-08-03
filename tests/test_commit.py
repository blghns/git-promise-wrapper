import unittest
import os
import promise
import commit
import helpers.git as git
import clear


class PromiseTester(unittest.TestCase):

    @staticmethod
    def create_promise_repo():
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

    def test_parent(self):
        self.create_promise_repo()
        # Edit the parent branch with the child's promised line
        with open("first", "w") as text:
            text.write("1\n2-edited\n3\n4\n5\n6\n")
        current_hash = git.current_hash()
        git.add("first")
        result = commit.checking_and_committing(["-m", "\"this commit should not work\""])
        new_hash = git.current_hash()

        self.assertEqual(False, result, "Parent shouldn't be able to commit.")
        self.assertEqual(current_hash, new_hash, "Parent shouldn't commit, hashes should be the same.")

        # Edit the child branch
        # Reset the

    def test_child(self):
        self.create_promise_repo()

        git.checkout("newBranch")

        with open("first", "w") as text:
            text.write("1\n2-edited\n3\n4\n5\n6\n")
        current_hash = git.current_hash()
        git.add("first")
        result = commit.checking_and_committing(["-m", "\"this commit should work\""])
        new_hash = git.current_hash()

        self.assertEqual(True, result, "Child should be able to commit.")
        self.assertNotEqual(current_hash, new_hash, "Child should be able to commit, hashes should be different.")

    def test_child2(self):
        self.create_promise_repo()
        git.checkout("newBranch")
        with open("first", "w") as text:
            text.write("1\n2-edited\n3\n4\n5-edited\n6\n")
        current_hash = git.current_hash()
        git.add("first")
        result = commit.checking_and_committing(["-m", "\"this commit should work\""])
        new_hash = git.current_hash()

        self.assertEqual(True, result, "Child should be able to commit.")
        self.assertNotEqual(current_hash, new_hash, "Child should be able to commit, hashes should be different.")


if __name__ == '__main__':
    unittest.main()

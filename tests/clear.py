import os
import stat
import shutil


def remove_test_dir():
    directory = "promiseTest/"
    if os.path.exists(directory):
        def remove_readonly(func, path, _):
            # Clear the readonly bit and reattempt the removal
            os.chmod(path, stat.S_IWRITE)
            func(path)

        shutil.rmtree(directory, onerror=remove_readonly)


if __name__ == "main":
    remove_test_dir()

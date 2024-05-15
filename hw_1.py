import subprocess
import string


if __name__ == '__main__':
    def test_function(command: str, text: str, split_for_words: bool = False) -> bool:
        """
        This function take a string command and check for including text in result or not.
        Then return result like True or False
        :param command: main command to use
        :param text: text for check
        :param split_for_words: True or False for splitting text in result or not
        :return:
        """
        result = subprocess.run(command, shell=True,
                                stdout=subprocess.PIPE, encoding='utf-8')
        out = result.stdout
        if split_for_words:
            for i in string.punctuation:
                if i in out:
                    out = out.replace(i, ' ')
        if text in out and result.returncode == 0:
            print(out)
            return True
        else:
            print(out)
            return False

    print(test_function('cat /etc/os-release', 'Jammy', True))

from sshcheckers import ssh_checkout, ssh_getout, upload_or_download_files, data


class TestPositiveSsh:

    @staticmethod
    def save_log(starttime, name):
        """
        fixture for making stats log in log file, which announced in config.yaml
        :return:
        """
        with open(name, "w", encoding="utf-8") as f:
            f.write(ssh_getout(data['host'], data['user'], data['passwd'], f"journalctl --since '{starttime}'", ""))

    def test_step1(self, start_time):
        """
        uploading files and installing program with check for successful deployment
        :return:
        """
        res = []
        upload_or_download_files(data['host'], data['user'], data['passwd'], f"/home/danielfalcony/Downloads/{data['pocket_name']}.deb",
                                 f"/home/user2/{data['pocket_name']}.deb")
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'],
                                f"echo {data['passwd']} | sudo -S dpkg -i /home/{data['user']}/{data['pocket_name']}.deb",
                                f"Setting up {data['pocket_name']}"))
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'], f"echo {data['passwd']} | sudo -S dpkg -s {data['pocket_name']}",
                                "Status: install ok installed"))
        self.save_log(start_time, data['log_txt'])
        assert all(res), "test1 FAIL"

    def test_step2(self, start_time):
        """
        uploading files and installing program with check for successful deployment
        :return:
        """
        res = []
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'],
                                f"echo {data['passwd']} | sudo -S dpkg -r {data['pocket_name']}", "Removing",))
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'], f"echo {data['passwd']} | sudo -S dpkg -s {data['pocket_name']}",
                                "Status: deinstall ok"))
        self.save_log(start_time, data['log_txt'])
        assert all(res), "test2 FAIL"
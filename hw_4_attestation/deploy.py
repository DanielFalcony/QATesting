from sshcheckers import ssh_checkout, ssh_getout, upload_or_download_files, data, checkout, take_data


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

    def test_step2(self, start_time, make_folders, clear_folders, make_files, stat_log):
        """

        :param start_time:
        :param make_folders:
        :param clear_folders:
        :param make_files:
        :param stat_log:
        :return:
        """
        res = []
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'], f"cd {data['folder_in']}; 7z a -t{data['arx_type']} {data['folder_out']}/arx2", "Everything is Ok"))
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'], f"ls {data['folder_out']}", f"arx2.{data['arx_type']}"))
        print(res)
        assert all(res), "test3 FAIL"

    def test_step3(self, start_time, clear_folders):
        """
        uploading files and uninstalling program with check for successful deployment
        :return:
        """
        res = []
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'],
                                f"echo {data['passwd']} | sudo -S dpkg -r {data['pocket_name']}", "Removing",))
        res.append(ssh_checkout(data['host'], data['user'], data['passwd'], f"echo {data['passwd']} | sudo -S dpkg -s {data['pocket_name']}",
                                "Status: deinstall ok"))
        self.save_log(start_time, data['log_txt'])
        assert all(res), "test2 FAIL"



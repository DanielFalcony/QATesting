from hw_3_checkers import checkout_negative, take_data
from conftest import data


class TestNegative:
    def test_negative_step1(self, make_folders, make_broke_file):
        # test neg 1
        assert checkout_negative(f"cd {data['folder_out']}; 7z e {data['arx_name']}.7z -o{data['folder_ext']} -y",
                                 "ERROR"), "test1 FAIL"

    def test_negative_step2(self, make_folders, make_broke_file):
        # test neg 1
        assert checkout_negative(f"cd {data['folder_out']}; 7z x {data['arx_name']}.7z -o{data['folder_ext']} -y",
                                 "ERROR"), "test1 FAIL"

    def test_negative_step3(self, make_folders, make_broke_file):
        # test neg 2
        assert checkout_negative(f"cd {data['folder_out']}; 7z t {data['arx_name']}.7z", "ERROR"), "test3 FAIL"

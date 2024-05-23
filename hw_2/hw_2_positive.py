from hw_2_checkers import checkout,take_data, folder_in, folder_out, folder_ext


def test_step1():
    # test Add files to archive
    res1 = checkout(f"cd {folder_in}; 7z a ../out/arx2 test1 test2", "Everything is Ok")
    res2 = checkout(f"ls {folder_out}", "arx2")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    # test check hash sum with CRC32 and 7z h
    hash_date_crc32 = str(take_data(f"cd {folder_out}; crc32 arx2.7z")).upper()
    hash_date_7z_check = checkout(f"cd {folder_out}; 7z h arx2.7z", hash_date_crc32)
    assert hash_date_7z_check, "test2 FAIL"


def test_step3():
    # test List contents of archive
    assert checkout(f"cd {folder_out}; 7z l arx2.7z", "Listing archive: arx2.7z")


def test_step4():
    # test Extract files from archive (without using directory names)
    res1 = checkout(f"cd {folder_out}; 7z e arx2.7z -o{folder_ext} -y", "Everything is Ok")
    res2 = checkout(f"ls {folder_ext}", "test1")
    res3 = checkout(f"ls {folder_ext}", "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step5():
    # test eXtract files with full paths
    res1 = checkout(f"cd {folder_out}; 7z x arx2.7z -o{folder_ext} -y", "Everything is Ok")
    res2 = checkout(f"ls {folder_ext}", "test1")
    res3 = checkout(f"ls {folder_ext}", "test2")
    assert res1 and res2 and res3, "test2 FAIL"


def test_step6():
    # Test integrity of archive
    assert checkout(f"cd {folder_out}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"


def test_step7():
    # test Update files to archive
    assert checkout(f"cd {folder_in}; 7z u arx2.7z", "Everything is Ok"), "test4 FAIL"


def test_step8():
    # test Delete files from archive
    assert checkout(f"cd {folder_out}; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"

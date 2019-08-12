def who_login(who):
    login = {
        'Dam': '../YAML/user_for_test/user_dir1_for_dam.yaml',
        'bayMax': '../YAML/user_for_test/user_dir1.yaml',
        'Beiruan': '../YAML/user_for_test/user_dir1_for_beiruan.yaml',
        'Cab': '../YAML/user_for_test/user_dir1.yaml',
        'Cad': '../YAML/user_for_test/user_dir1.yaml',
        'YinPao': '../YAML/user_for_test/user_dir1_for_beiruan.yaml',
        'ShuBo': '../YAML/user_for_test/user_dir1.yaml'
    }
    return login[who]

if __name__ == "__main__":
    who_login('bayMax')
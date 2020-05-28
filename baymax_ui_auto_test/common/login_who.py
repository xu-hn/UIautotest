def who_login(who):
    login = {
        #'Dam': '../YAML/user_for_test/user_dir1_for_dam.yaml',
        'THDax': '../YAML/user_for_test/user_dir1_for_THDax'
    }
    return login[who]

if __name__ == "__main__":
    who_login('THDax')
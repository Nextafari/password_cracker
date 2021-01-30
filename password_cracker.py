import crypt


def test_pass(crypt_pass):
    # getting the first two values of the encrypted password
    salt = crypt_pass[0:2]
    # dict_file = open('/usr/share/dict/words', 'r')
    dict_file = open('dictionary.txt', 'r')
    for word in dict_file.readlines():
        # word = word.strip("\n")
        crypted_word = crypt.crypt(word, salt)
        print("Crypted word", crypted_word, crypt_pass)
        if crypted_word == crypt_pass:
            print("found password: {}".format(word))
        else:
            print("Password not found: ")


# test_pass("HXeztZhQqnh2Q")

def main():
    password_file = open("password.txt", "r")
    for line in password_file.readlines():
        if ":" in line:
            user = line.split(":")[0]
            crypt_pass = line.split(":").strip(" ")
            print(f"cracking password for {user}")
            test_pass(crypt_pass)
        else:
            password_file = open("password.txt", "r")
            for line in password_file.readlines():
                print("LIne", line)
                crypt_pass = crypt.crypt(line, "HD")
                test_pass(crypt_pass)


main()

def isValidEmail(email):
    is_include_beginning_mark = email[0] == "@"
    is_not_include_mark = email.find("@") == -1
    is_include_space = " " in email
    is_duplication_mark = email.count("@") >= 2
    is_not_contain_dot_after_mark = not("." in email[email.find("@"):])

    return not (is_include_beginning_mark or is_not_include_mark or is_include_space or is_duplication_mark or is_not_contain_dot_after_mark)


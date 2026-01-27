def solution(id_pw, db):
    db_dict = {i[0]:i[1] for i in db}
    if id_pw[0] in db_dict:
        if db_dict[id_pw[0]] == id_pw[1]:
            return 	"login"
        return "wrong pw"
    return "fail"
import json
path = r"F:\DRC Practical Round\test.json"
path_o = r"F:\DRC Practical Round\output.json"
def rec():
    with open(path, 'r') as f:
        body = f.read()
    if body=="":
        return 0
    else:
        with open(path_o, 'w') as f:
            f.write(str(body).replace("+type", "+size@5+type"))
    rec()

rec()
import hashlib

exam_name = 'examen in vaste stof fysica'
exam_id = '134546'

def generate_exam_token2():
    hasher = hashlib.sha384()
    string = exam_name + exam_id
    hasher.update(string.encode('utf-8'))
    

    return hasher.hexdigest()[0:12]

token = generate_exam_token2()

print(token)

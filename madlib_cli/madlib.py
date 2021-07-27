import re  


def welocme_message():

    print ('welcome to madlib game ')

    welocme_message()

def game_rules ():

   print ("""guess the answer after u finish u will see the result """) 

   game_rules()

def read_template(txt_path:str)->str:
    try:

     with open (txt_path , "r") as file :
        file_cont = file.read()
        return file_cont.strip()
    except FileNotFoundError:
        return 'file not found '

def parse_template(file_cont):

    analizing = re.findall(r'\{(.*?)\}' , file_cont)
    for i in analizing :
        file_cont = file_cont.replace(i,'',1)
    return file_cont,tuple(analizing)



def ask_user (q):

    the_user_answer = [] 

    for i in q :
        answer = input (f"can i ask {i} ? ")
        the_user_answer.append(answer)
    return the_user_answer

def merge (after_do_stripped , the_user_answer):

    print (the_user_answer)

    new_answer = after_do_stripped.format(*the_user_answer)
    print (new_answer)
    return (new_answer)

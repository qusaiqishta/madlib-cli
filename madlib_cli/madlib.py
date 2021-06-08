import re


print("""
   Hello , and welcome to my funny and enjoyable game 
   all you need to do is to answer the questions that will appear to you
""")


"""
 read_template function will get the content of a specified file

"""

def  read_template(path):
    with open(path,'r') as file:
        print(file.read())


"""
parse_template function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.

"""

def parse_template(txt):
    target_words=re.findall(r'\{(.*?)\}',txt) # it will giv me an array
    replaced_txt=re.sub(r'\{(.*?)\}','$',txt)
    return target_words , replaced_txt

#print(parse_template("I the {qusai} and {qusai} {A First Name} have {Past Tense Verb}{A First Name}")) # nice it works   

"""
merge function will take the user input and merge it with the text
"""
def merge(txt,anwers):
    for answer in anwers:
        txt=txt.replace('$',answer,1)
    return txt    

if __name__=='__main__':
    print('im here')
    txt=read_template('assets/template.txt')
    words=parse_template(txt)
    target_words=words[0]
    replaced_txt=words[1]
    

    print('The game is about to start , stay tuned!!')
    anwers=[]  

    for word in target_words:
        anwers.append(input(f'Enter {word}'))
    result=merge(replaced_txt,anwers)
    file=open('assets/result.txt','w')
    file.write(result)
    print(result)


from random import choice
from string import ascii_lowercase as Letters

domain = ["gmail","ymail","outlook"]
quotes = ["I hate to be with you","I will be happy with you","It sucks to hate you","I miss you"]

def ge_quote(quotes):
    return choice(quotes)

def get_domain(domain):
    return choice(domain)

def generate_name(num):
    return "".join(choice(Letters) for i in range(num))

def generate_word(generate_name,get_domain,ge_quote,num,max_line,domain,quotes):
    with open("HashFile.txt",'w') as write_as:
        for i in range(max_line):
            key = generate_name(num)+'@'+get_domain(domain)
            value = ge_quote(quotes)
            record = key+":"+value+"\n"
            write_as.write(record)
        write_as.write("Karthick@gmail:I am fine")
        write_as.write("help@gmail:clarify")


generate_word(generate_name,get_domain,ge_quote,10,10000,domain,quotes)
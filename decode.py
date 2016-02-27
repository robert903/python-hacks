'''takes encoded string input from user and decodes it'''
input= raw_input("GIVE ME SUPER SECRET CODE TO DECODE >>> ")
def main(input):
    undecoded="%s" %input [1:]
    if "%s" %input =='':
        return ''
    else:
        answer=chr(((ord("%s" %input [0]))-3)) + main(undecoded)
    return answer

if __name__ == "__main__":
    print main(input)

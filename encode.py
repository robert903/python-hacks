'''takes input from user and encodes it'''
input= raw_input("GIVE ME SUPER SECRET MESSAGE TO ENCODE >>> ")
def main(input):
    unencoded="%s" %input [1:]
    if "%s" %input =='':
        return ''
    else:
        answer=chr((ord("%s" %input [0])+3)) + main(unencoded)
    return answer

if __name__ == "__main__":
    print main(input)

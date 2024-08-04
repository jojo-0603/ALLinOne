import hashlib


def determine_hash_type(hash_value):
    if len(hash_value) == 32:
        return "MD5"
    elif len(hash_value) == 40:
        return "SHA-1"
    elif len(hash_value) == 64:
        return "SHA-256"
    else:
        return "Unknown"
    
def encrypt(data,shift):
   encrypted=""
   for i in range(len(data)):
      char = data[i]
      if (char.isupper()):
        encrypted+=chr((ord(char)+shift-65) % 26 +65)
      elif(char.islower()):
        encrypted+=chr((ord(char)+shift-97) % 26 +97)
      elif(char.isdigit()):
         number = int(char) + shift %10
         encrypted +=str(number)
      else:
         encrypted+=char
         
   return encrypted

def decrypt(data,shift):
   decrypted=""
   for i in range(len(data)):
      char = data[i]
      if (char.isupper()):
        decrypted+=chr((ord(char)-shift-65) % 26 +65)
      elif(char.islower()):
        decrypted+=chr((ord(char)-shift-97) % 26 +97)
      elif(char.isdigit()):
         number = int(char) - shift %10
         decrypted +=str(number)
      else:
         decrypted+=char
         
   return decrypted

def pass_cracker():
    comman_pass=[]
    while True:
        input_hash=input("""(Our password cracker only supports MD5,SHA1 and SHA256)
    Enter the sha256 digest of the password to be cracked :  """)
        hash_value=determine_hash_type(input_hash)
        with open ('comman_pass.txt','r') as f:
         comman_pass=f.read().splitlines()
        # print(comman_pass)

        for passwd in comman_pass:
            if hash_value=='SHA-256':
                hash_passwd = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
            elif hash_value=='SHA-1':
                hash_passwd = hashlib.sha1(passwd.encode('utf-8')).hexdigest()
            elif hash_value=='MD5':
                hash_passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
            else:
                print("Enter the known hash value")
            if hash_passwd==input_hash:
                print (f"Password found : {passwd}")
                print (f"Password hash type : {hash_value}")
                quit()

#pass_cracker()

def pass_manager():
    shift =2   
    while True:
        count=0
        menu = input ("""Would you like to save a new password or view the old password?
    1. Input the new password
    2. View the old password
    3. Exit
    """)
        if menu=="1":
            website=input("Enter the website where the password is used :")
            user=input("Enter the USERNAME  :")
            passwd=input("Enter the PASSWORD  :")
            with open ('securePass.txt','a') as f:
                f.write(encrypt(website,shift)+";|"+encrypt(user,shift)+";|"+encrypt(passwd,shift)+"\n")
                f.close()
        elif menu =="2":
            print("Password Displayed")
            print("   Website \t Username \t \tPassword")
            with open ('securePass.txt','r') as f:
                for i in f:
                    data = i.split(";|")
                    #print(data)
                    
                    count = count+1
                    print(f'{count}. {decrypt(data[0],shift)}\t {decrypt(data[1],shift)}\t\t {decrypt(data[2],shift)}')
        elif menu=="3":
            quit()

#pass_manager()
def passwords():
    resp = input("""
    Enter the Scan option for the IP.
    1. Password Cracker
    2. Password Manager
   \n""")
    if resp =='1':
       pass_cracker()
    elif resp =='2':
       pass_manager()
    else:
       print("Enter a valid number")
"""
   Note please change the path at the line of code  21 and 33 as per your current folder location/directory
   on running on default fil path directory it throughs an error as the existing path is used as per the author file location/directory
"""

# """Using getter and setter method in oop write a program  set the 3employee email ids\
#     1) Ananth shetty 
#     1) Ramesh kumar 
#     1) Dhan raj             with email id @codeisfun.com   """

# #this class program sets the email ids 
class Employee():
    first_name = "FirstName" 
    last_name = "LastName"
    # mail_id = " "
    mail_type = "codeisfun"
    mail_domain = "com"

    @property       #getter method; getting the method name of a function such a way the method name also used as class attribut
    def mail_id(self):
        if self.first_name == None or self.last_name == None or self.mail_type == None or self.mail_domain == None:
            return "Your email id is not set, please set mail id using setter method"
        else:
            with open("C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\4_email_id_project\email_id_setter\\emailstorage","a+") as a:
                a.write(f"\n{self.first_name}.{self.last_name}@{self.mail_type}.{self.mail_domain}")
            return f"{self.first_name}.{self.last_name}@{self.mail_type}.{self.mail_domain}"

    @mail_id.setter     #setter method setting the mail_id attribute if class object
    def mail_id(self,email):
        self.email_list = email.split("@")
        self.first_name = ((self.email_list[0]).split("."))[0]
        self.last_name = ((self.email_list[0]).split("."))[1]
        self.mail_type = ((self.email_list[1]).split("."))[0]
        self.mail_domain = ((self.email_list[1]).split("."))[1]

        with open("C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\4_email_id_project\email_id_setter\\emailstorage","a+") as a:
            a.write(f"{self.first_name}.{self.last_name}@{self.mail_type}.{self.mail_domain}")
    @mail_id.deleter
    def mail_id(self):
        self.first_name = None
        self.last_name  = None
        self.mail_type = None
        self.mail_domain    = None

def call():
    
    while 1:
        try:    
            i1 = int(input("""
Want to create an email id with mail type codeisfun.com, then enter '1'
Already Have an email id and want to set it in mail DataBase, then enter '2'
Enter '3' to exit()\n>> """))
        except ValueError as ve:
            print(f"Invalid input")
            call()
        
        if i1 == 3:
            print("Thank you for your valuable time\n\tHave a nice day")
            break
        elif i1 == 1:
            guest = Employee()
            guest.first_name = (input("Enter first name\n_")).lower()
            guest.last_name = (input("Enter last name\n_")).lower()
            print(f"Mail id is ready: {guest.mail_id}")
        elif i1 == 2:
            try:
                guest = Employee()
                guest.mail_id = input("Enter you mail id in fomrat 'fname.lname@mailtype.domain'\n>> ")
                print(f"\nYou mail details stored as below:\nFirst Name: {guest.first_name}   Last Name: {guest.last_name}    Mail Type: {guest.mail_type}  Domain: {guest.mail_domain}\n")
            except Exception as ve:
                print("Invalid input, try correct format")
                call()
call()

"""________________________________________________THE_END________________________________________________"""

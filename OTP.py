
from tkinter import *
from tkinter import messagebox
import random
import smtplib
otp=''.join([str(random.randint(0,9)) for i in range(6)])

root = Tk()
root.title('OTP Verification')
Label(root,text="Enter Your Email",font=("Helvetica 20 bold")).pack(pady=10)
e1=Entry(root,width=20)
e1.pack()
Label(root,text="Enter Verification Code",font=("Helvetica 20 bold"),).pack(pady=10)
e2=Entry(root,width=20)
e2.pack()
root.geometry("500x350")

def otpsend():
   email=e1.get()
   #otp=''.join([str(random.randint(0,9)) for i in range(6)])

   server=smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login('passreset111@gmail.com','jqpmshkebszebdgg')

   msg='Hello your OTP is '+ str(otp)
   server.sendmail('passreset111@gmail.com',email,msg)
   server.quit()
   
Button(root, text="Send OTP", font=("Helvetica 15"),command= otpsend).pack(pady=20)

def otpverify():
 otpvalue=e2.get()
 if otpvalue == str(otp):
   messagebox.showinfo("OTP","Verificatin succsessful!") 
   print("verified")
 else:
   messagebox.showerror("OTP","Verification not succsessful! Try again")
   print("not verified")

Button(root, text="Verify OTP", font=("Helvetica 15"),command= otpverify).pack(pady=20)
root.mainloop()
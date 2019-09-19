import re
import os
print("1. Ít nhất 1 chữ cái nằm trong [a-z]")
print("2. Ít nhất 1 số nằm trong [0-9]")
print("3. Ít nhất 1 kí tự nằm trong [A-Z]")
print("4. Ít nhất 1 ký tự nằm trong [$ # @]")
print("5. Độ dài mật khẩu tối thiểu: 6")

danhsach_seller = []
class create_password():
  def __init__(self,password = None,nameuser = None):
    self.password = password
    self.nameuser = nameuser
  def check(self):
    count = 5
    self.ok = False
    if len(self.password)>6 or len(self.password)<12:
        count -= 1
    if re.search("[a-z]",self.password):
      count -= 1
    if re.search("[0-9]",self.password):
      count -= 1
    if re.search("[A-Z]",self.password):
      count -= 1
    if re.search("[$#@]",self.password):
      count -= 1
    if count == 0:
      self.ok =True
    #print(self.ok)
    return self.ok
    
def ham_create_password():
  name_seller = input("Ten dang nhap: ")
  password = input("Create Password: ")
  
  kt = create_password(password)
  print(1)
  print(kt.check())
  while kt.check() is False:
    password = input("Create Password: ")
    kt = create_password(password)

  str_to_save = name_seller + "#" + password + "\n"
  with open('danhmuc/password.csv', 'a') as f:
    f.write(str_to_save)
    
def load_password_luckhoidong():
  files = os.listdir('danhmuc')
  if "password.csv" not in files:
    return
  with open('danhmuc/password.csv','r') as f:
    line = f.readline()
    while line:
      str_to_read = line.split("#")
      if len(str_to_read) > 1:
        dangnhap = {}
        dangnhap["name_seller"] = str_to_read[0]
        mat_khau = str_to_read[1]
        if mat_khau.endswith("\n"):
          mat_khau = mat_khau[0 : len(mat_khau) - 1]
        dangnhap["password"] =mat_khau
        danhsach_seller.append(dangnhap)
    line = f.readline()
  print("Danh sach nguoi dung: ",danhsach_seller)

load_password_luckhoidong()

def login(name = None):
  if password == name:
    pass

def view_account(name = None):

  ok = False
  if name is None:
    print("Chua ton tai tai khoan nay!")
    print("Nhan Y de tao tai khoan")
    print("Nhan T de dang nhap lai")
    print("Nhan E de thoat")
    choose = input("=> Chon chuc nang: ")
    if choose.upper() == "Y":
      ham_create_password()
    if choose.upper() == "T":
      name = input("Ten dang nhap: ")
      for test in danhsach_seller:
        if test["name_seller"] == name:
          input_password = input("Password: ")
          if test["password"] == input_password:
            ok = True
    if choose.upper() == "E":
      return
  return ok

print("+--------Account-------------+")
print("|chon C | de tao tai khoan   |")
print("|chon D | de dang nhap       |")
print("|chon E | de thoat           |")
print("+----------------------------+")
select = input("=> Chon chuc nang: ")
while select.upper() != "E":
  if select.upper() == "C":
    ham_create_password()
  if select.upper() == "D":
    name = input("Ten dang nhap: ")
    view_account(name)
  if select.upper() == "E":
    print("Bye Bye! Hen gap lai!")
    break
  select = input("=> Chon chuc nang: ")
create_password()
name = input("Ten dang nhap: ")
view_account(name)
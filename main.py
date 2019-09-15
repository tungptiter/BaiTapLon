import os
import json

print("+-----------------------------MENU-----------------------------+")
print("|Chon THH | de xem hang hoa                                      |")
print("|Chon TLH | de tao loai hang hoa                                 |")
print("|Chon XLH | de xem loai hang hoa                                 |")
print("|Chon C   | de tao hoa don                                       |")
print("|Chon R   | de xem thong tin hoa don                             |")
print("|Chon T   | de tinh tong doanh thu                               |")
print("|chon G   | de xem hang hoa ban CHAY nhat va IT nhat trong thang |")
print("|chon M   | de xem AI mua nhieu tien nhat thang                  |")
print("|chon N   | de xem Tong so va Doanh thu cua tung hang hoa        |")
print("|chon D   | de xem NGAY mua nhieu tien nhat thang                  |")
print("|Chon E   | de thoat                                             |")
print("+--------------------------------------------------------------+")

danhsachhanghoa = []
danhsachloaihanghoa = []
danhsachhoadon=[]
# danhsachhoadon = [
#     {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS01', 'tongtientruocthue': 25000},
#     {'thue': 0.1, 'tongtien': 27500.0, 'danhsachhanghoa': [{'ten': 'Coca', 'dongia': 5000, 'thanhtien': 10000, 'stt': '1', 'soluong': 2}, {'ten': 'Pepsi', 'dongia': 3000, 'thanhtien': 15000, 'stt': '2', 'soluong': 5}], 'nguoimua': 'Cuong', 'ngayhoadon': '1', 'sohoadon': 'MS02', 'tongtientruocthue': 25000}
# ]

# hanghoaban = {c
#     # "Coca": {
#     #     "tongso": 0,
#     #     "doanhthu": 0
#     # }
# }
# check = os.listdir('danhmuc/')
# print(check)
def load_loaihanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "loaihanghoa.csv" not in files:
     return
  
  with open('danhmuc/loaihanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        #print("str_to_reads:", str_to_reads)
        if len(str_to_reads) > 1:
            loaihanghoa = {}
            loaihanghoa["id"] = str_to_reads[0]
            tenloai = str_to_reads[1]
            if tenloai.endswith('\n'):
                tenloai = tenloai[0:len(tenloai)-1]
            loaihanghoa["ten"] = tenloai
            danhsachloaihanghoa.append(loaihanghoa)
        line = f.readline()
  print("danhsachloaihanghoa:", danhsachloaihanghoa)
  

	
def tao_loaihanghoa():
  data = {}
  id = input("xin moi nhap id loai hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chu nang khac")
     return

  data["id"] = id
  data["ten"] = input("xin moi nhap ten loai hang hoa:")
  danhsachloaihanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '\n'
  with open('danhmuc/loaihanghoa.csv', 'a') as f:
	    data = f.write(str_to_save)



def xem_loaihanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id loai hang hoa:")
  for loai in danhsachloaihanghoa:
    if loai["id"] == id:
      print("loai hang hoa: ", loai)
      return loai


def sua_loaihanghoa(id, data):
  pass

def xoa_loaihanghoa(id):
  pass

def danhsach_loaihanghoa():
  return danhsachloaihanghoa

'''HANG HOA'''

def load_hanghoa_luckhoidong():
  files = os.listdir("danhmuc")
  if "hanghoa.csv" not in files:
     return

  with open('danhmuc/hanghoa.csv', 'r') as f:
    line = f.readline()
    while line:
        str_to_reads = line.split("#")
        #print("str_to_reads:", str_to_reads)
        if len(str_to_reads) > 1:
            hanghoa = {}
            hanghoa["id"] = str_to_reads[0]
            hanghoa["ten"] = str_to_reads[1]
            hanghoa["giaban"] = str_to_reads[2]
            hanghoa["loaihanghoa_id"] = str_to_reads[3]
            
            if hanghoa["loaihanghoa_id"].endswith('\n'):1
            hanghoa["loaihanghoa_id"] = hanghoa["loaihanghoa_id"][0:len(hanghoa["loaihanghoa_id"])-1]
            danhsachhanghoa.append(hanghoa)
        line = f.readline()
  print("danhsachhanghoa:", danhsachhanghoa)
	
load_hanghoa_luckhoidong()
def tao_hanghoa():
  data = {}
  id = input("xin moi nhap id hang hoa:")
  tim_id_daco = xem_loaihanghoa(id)
  if tim_id_daco is not None:
     print("Da ton tai Ma loai hang hoa nay. Xin moi ban thu hien chuc nang khac")
     return
  data["id"] = id
  data["ten"] = input("xin moi nhap ten hang hoa:")
  data["giaban"] = input("xin moi nhap gia ban:")
  loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
	
 # co_hienthi_danhsachloai = False
  tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)
  
  while tim_idloai_daco is None:
    print("Danh sach loai hang hoa:")
    for loaihanghoa in danhsachloaihanghoa:
        print(loaihanghoa["id"] + "  " + loaihanghoa["ten"])
    chon = input("Ban muon nhap tiep nhan 'Y', chon chuc nang khac nhan 'E': ")
    if chon.upper() == "E":
      return      
    loaihanghoa_id = input("xin moi nhap ma loai hang hoa:")
    tim_idloai_daco = xem_loaihanghoa(loaihanghoa_id)
	
  
  data["loaihanghoa_id"] = loaihanghoa_id
  danhsachhanghoa.append(data)
  str_to_save = data["id"] + "#" + data["ten"] + '#' + data["giaban"] + "#" +  data["loaihanghoa_id"] + '\n'
  with open('danhmuc/hanghoa.csv', 'a') as f:
      data = f.write(str_to_save)
  


def xem_hanghoa(id = None):
  if id is None:
      id = input("xin moi nhap id hang hoa:")
  for hanghoa in danhsachhanghoa:
    if hanghoa["id"] == id:
      print(hanghoa)
      return hanghoa
    
'''END OF HANG HOA'''

'''Khi nhập hóa đơn mua hàng, nhân viên kiểm tra xem mã hóa đơn đã tồn tại hay chưa? Nếu đã tồn tại thì xin mời nhập lại đến khi nào hợp lệ thì thôi.
Nhập mã hàng hóa cần mua, nếu mã đó không tồn tại trong danh sách hàng hóa thì hỏi và nhập lại đến khi nào có thì thôi.
Người dùng gõ mã sản phẩm cần tính tiền --> hệ thống tự tìm ra tên sản phẩm và giá tiền sản phẩm.
Lưu từng hóa đơn thành file có đuôi .json dưới dạng: HD_Ngày(dd).json '''


'''load hang hoa ban va /khach hang luc khoi dong may 
trong file hanghoaban va khachhangthanthiet ban dau khi moi su dung thi se khoi tao cac gia tri la 0 va string'''

def load_hanghoaban_and_khachhang():
  global hanghoaban 
  global khachhang 
  global ngaybanhang
  with open('danhmuc/hanghoaban.json','r') as f1:
    hanghoaban = json.load(f1)
  with open('danhmuc/khachhangthanthiet.json','r') as f2:
    khachhang = json.load(f2)
  with open('danhmuc/ngaybanhang.json','r') as f3:
    ngaybanhang = json.load(f3)
    
load_hanghoaban_and_khachhang()

'''end of load hang hoa ban va khach hang luc khoi dong may '''

'''HOA DON'''
def tao_hoadon():
  hoadon = {}
  
  sohoadon = input("Xin moi nhap vao so hoa don: ")
  xem_hoadon(sohoadon)
                  
  hoadon["sohoadon"] = sohoadon
  hoadon["nguoimua"] = input("Nhap nguoi mua: ")
  hoadon["ngaymua"] = input("Nhap ngay mua: ")
  hoadon["tongtientruocthue"] = 0
  hoadon["thue"] = 0.1
  hoadon["tongtien"] = 0
  hoadon["danhsachhanghoa"] = []
  
  nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
  while nhaphanghoa.upper() == 'Y':
      hanghoa = {}
      
      hanghoa_id = input("nhap ID hang hoa: ")
      tim_id_daco = xem_hanghoa(hanghoa_id)
      while tim_id_daco is None:
          chon_ma_hanghoa = input("Ma hang hoa nay Chua ton tai, Xin moi chon ma khac nhan 'Y' ,chon chuc nang khac nhan 'E': ")
          for loai in danhsachhanghoa:
              print( loai["id"] + " " + loai["ten"])
          if chon_ma_hanghoa.upper() =="E":
              return 
          if chon_ma_hanghoa.upper() == "Y":
              hanghoa_id = input("nhap ID hang hoa: ")
              tim_id_daco = xem_hanghoa(hanghoa_id)   
      hanghoa["id"] = hanghoa_id               
      soluong = input("nhap so luong: ")
      hanghoa["soluong"] = int(soluong)
      for loai in danhsachhanghoa:
        if hanghoa["id"] == loai["id"]:
            hanghoa["ten"] = loai["ten"]
            hanghoa["giaban"] = loai["giaban"] 
            hanghoa["thanhtien"] = int(hanghoa["soluong"]) * int(hanghoa["giaban"])
            
            if hanghoa["ten"] in hanghoaban:
                hanghoaban[hanghoa["ten"]]["tongso"] = hanghoaban[hanghoa["ten"]]["tongso"] + hanghoa["soluong"]
                hanghoaban[hanghoa["ten"]]["doanhthu"] = hanghoaban[hanghoa["ten"]]["doanhthu"] + hanghoa["thanhtien"]
            else:
                hanghoaban[hanghoa["ten"]] = {
                "tongso": hanghoa["soluong"],
                "doanhthu": hanghoa["thanhtien"]
                }
            print(hanghoaban)
            break
      hoadon["danhsachhanghoa"].append(hanghoa)
      
      hoadon["tongtientruocthue"] += int(hanghoa["thanhtien"])
      
      nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
      
  hoadon["tongtien"] = hoadon["tongtientruocthue"]*hoadon["thue"] + hoadon["tongtientruocthue"]

  if hoadon["nguoimua"] in khachhang:
    khachhang["tongtien"] +=  hoadon["tongtien"]

  else:
    
    if hoadon["tongtien"] > khachhang["tongtien"]:
      khachhang["tongtien"] = hoadon["tongtien"]
      khachhang["ten"] = hoadon["nguoimua"]
    if hoadon["tongtien"] == khachhang["tongtien"]:
      pass
  
  if ngaybanhang["ngaymua"] in ngaybanhang:
    ngaybanhang["tongtien"] += hoadon["tongtien"]
  else:
    if hoadon["tongtien"] > ngaybanhang["tongtien"]:
      ngaybanhang["ngaymua"] = hoadon["ngaymua"]
      ngaybanhang["tongtien"] = hoadon["tongtien"]
  print(ngaybanhang)    
  print(khachhang)
  danhsachhoadon.append(hoadon)   

  filename = hoadon["sohoadon"] +".json"
  with open('hoadon/' + filename, 'w') as f1:
    json.dump(hoadon, f1)
  with open('danhmuc/hanghoaban.json','w') as f2:
    json.dump(hanghoaban,f2)    
  with open('danhmuc/khachhangthanthiet.json','w') as f3:
    json.dump(khachhang,f3)
  with open('danhmuc/ngaybanhang.json','w') as f4:
    json.dump(ngaybanhang,f4)
  
def xem_hoadon( sohoadon = None):
  file_sohoadon = sohoadon + ".json"
  files = os.listdir("hoadon")
  while file_sohoadon in files:
      chon_sohoadon = input("Da ton tai so hoa don nay! Xin moi chon nhap ma khac nhan 'Y' ,chon Chuc nang khac nhan 'E': ")
      if chon_sohoadon.upper() == "E":
          return 
      elif  chon_sohoadon.upper() == "Y":
          sohoadon = input("Xin moi nhap vao so hoa don: ")
          file_sohoadon = sohoadon + ".json"
    
def kiemtrahoadon():
  sohoadon = input("Nhap so hoa don can kiem tra: ")
  file_sohoadon = sohoadon + ".json"
  files = os.listdir("hoadon")
  while file_sohoadon not in files:
      chon_sohoadon = input("CHUA ton tai so hoa don nay! Xin moi chon nhap ma khac nhan 'Y' ,chon Chuc nang khac nhan 'E': ")
      if chon_sohoadon.upper() == "E":
          return 
      elif  chon_sohoadon.upper() == "Y":
          sohoadon = input("Xin moi nhap vao so hoa don: ")
          file_sohoadon = sohoadon + ".json"
  with open('hoadon/' + file_sohoadon, 'r') as infile:
      hoadon = json.load(infile)

      print("\n--------------------VIETNAME LIFE-------------------")
      print("So hoa don: ",hoadon["sohoadon"])
      print("nguoi mua: ",hoadon["nguoimua"])
      print("ngay mua: ",hoadon["ngaymua"])
      print("+----------+----------+----------+----------+----------+")
      print("| STT      |TenHangHoa| Soluong  | DonGia   | ThanhTien|")
      print("+----------+----------+----------+----------+----------+")
      stt = 0
      for hanghoa in hoadon["danhsachhanghoa"]:
        stt += 1
        print("|" + str(stt).rjust(10,' ') + "|" +  str(hanghoa["ten"]).rjust(10,' ') + "|" + str(hanghoa["soluong"]).rjust(10,' ') + "|" + str(hanghoa["giaban"]).rjust(10,' ') + "|" +str(hanghoa["thanhtien"]).rjust(10,' ') + "|")
        print("+----------+----------+----------+----------+----------+")
      print("|                                 Tong tien |" + str(hoadon["tongtien"]).rjust(10,' ') + "|")
      print("+----------+----------+----------+----------+----------+")
'''end of HOADON'''

'''TINH TOAN'''
def hanghoa_banchay_va_itnhat_nhatthang():
  max = 0
  min = 1000
#'''min = 0 thì khi chạy sẽ là nhỏ nhất nên min se luôn = 0'''

  for hanghoa in danhsachhanghoa:
    if hanghoa["ten"] in  hanghoaban:
        if(max < hanghoaban[hanghoa["ten"]]["tongso"]):
          max = hanghoaban[hanghoa["ten"]]["tongso"]
          
        if min > hanghoaban[hanghoa["ten"]]["tongso"]:
          min = hanghoaban[hanghoa["ten"]]["tongso"]
        print(max,min)
  print("Hang hoa ban chay nhat va it nhat")
  print("+-----------+-----------+")
  print("| Hanghoa   |  Tongso   |")
  print("+-----------+-----------+")
  for hanghoa in danhsachhanghoa:
    if hanghoa["ten"] in  hanghoaban:

      if max == hanghoaban[hanghoa["ten"]]["tongso"]:
        print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(max).rjust(11,' ') + "|")
        print("+-----------+-----------+")
        
      if min == hanghoaban[hanghoa["ten"]]["tongso"]:
        print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(min).rjust(11,' ') + "|")
        print("+-----------+-----------+")
        

def tongso_doanhthu_daban():
  tongso_hanghoa = 0
  tong_doanhthu = 0
  print("+-----------+-----------+-----------+")
  print("| Hanghoa   |  Tongso   | Doanhthu  |")
  print("+-----------+-----------+-----------+")
  for hanghoa in danhsachhanghoa:
    if hanghoa["ten"] in hanghoaban:
      print("|" + str(hanghoa["ten"]).rjust(11,' ') + "|" + str(hanghoaban[hanghoa["ten"]]["tongso"]).rjust(11,' ') + "|" + str(hanghoaban[hanghoa["ten"]]["doanhthu"]).rjust(11,' ') + "|")
      print("+-----------+-----------+-----------+")
      tongso_hanghoa += hanghoaban[hanghoa["ten"]]["tongso"]
      tong_doanhthu += hanghoaban[hanghoa["ten"]]["doanhthu"]
  print("+-----------+-----------+-----------+")    
  print("| Tong cong |" + str(tongso_hanghoa).rjust(11,' ') + "|" +  str(tong_doanhthu).rjust(11, ' ') + "|")
  print("+-----------+-----------+-----------+")

def khachhang_muanhieunhat_thang():
  print("+--------------------+---------------------+")
  print("|     Khachhang      |      Tongtien       |")
  print("+--------------------+---------------------+")
  print("|" + str(khachhang["ten"]).center(20,' ') + "|" + str(khachhang["tongtien"]).center(21,' ') + "|")
  print("+--------------------+---------------------+")

def ngaybanhang_nhieunhat():
  print("+--------------------+---------------------+")
  print("|      Ngayban       |      Tongtien       |")
  print("+--------------------+---------------------+")
  print("|"+ str(ngaybanhang["ngaymua"]).rjust(20,' ')+ "|" + str(ngaybanhang["tongtien"]).rjust(21,' ') +"|" )
  print("+--------------------+---------------------+")  
def tongdoanhthu():
  tong_doanhthu = 0
  for hanghoa in danhsachhanghoa:
    if hanghoa["ten"] in hanghoaban:
      tong_doanhthu += hanghoaban[hanghoa["ten"]]["doanhthu"]
  print("Tong doanh thu la: ", tong_doanhthu) 
  
'''END OF TINH TOAN'''

print("hang hoa ban: ", hanghoaban)
print("khach hang:", khachhang)
while True:
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'TLH':
      tao_loaihanghoa()
    if x.upper() == 'XLH':
      xem_loaihanghoa()
    if x.upper() == 'THH':
      tao_hanghoa()
    if x.upper() == 'XHH':
      xem_hanghoa()
    if x.upper() == 'C':
      print("moi ban tao hoa don")
      tao_hoadon()
    if x.upper() == 'R':
      kiemtrahoadon()

    if x.upper() == 'T':
      tongdoanhthu()
    if x.upper() == 'G':
      hanghoa_banchay_va_itnhat_nhatthang()
    if x.upper() == "M":
      khachhang_muanhieunhat_thang()
    if x.upper() == 'N':
      tongso_doanhthu_daban()
    if x.upper() == "D":
      ngaybanhang_nhieunhat()
    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break

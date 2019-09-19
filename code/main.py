import os
import password
import hoadon
import hanghoa_real
import loaihanghoa
import nhap_kho
import xuat_kho

print("+-----------------------------MENU-----------------------------+")
print("|Chon THH | de xem hang hoa                                      |")
print("|Chon TLH | de Tao loai hang hoa                                 |")
print("|Chon XLH | de Xem loai hang hoa                                 |")
print("|Chon SLH | de Sua loai hang hoa                                 |")
print("|Chon DLH | de Xoa loai hang hoa                                 |")
print("|Chon C   | de tao hoa don                                       |")
print("|Chon R   | de xem thong tin hoa don                             |")
print("|Chon T   | de tinh tong doanh thu                               |")
print("|chon G   | de xem hang hoa ban Chay nhat va It nhat trong thang |") # sai ttoan
print("|chon M   | de xem Ai mua nhieu tien nhat thang                  |")
print("|chon N   | de xem Tong so va Doanh thu cua tung hang hoa        |")
print("|chon D   | de xem Ngay mua nhieu tien nhat thang                |")
print("|Chon E   | de thoat                                             |")
print("+--------------------------------------------------------------+")

while True:
    
    x=input("=> chon chuc nang:")
    print("=> ban da chon chuc nang:",x)
    if x.upper() == 'TLH':
      loaihanghoa.tao_loaihanghoa()
    if x.upper() == 'XLH':
      loaihanghoa.xem_loaihanghoa()

    if x.upper() == 'SLH':
      loaihanghoa.sua_loaihanghoa()
    if x.upper() == 'DLH':
      loaihanghoa.xoa_loaihanghoa()    
    if x.upper() == 'THH':
      hanghoa_real.tao_hanghoa()
    if x.upper() == 'XHH':
      hanghoa_real.xem_hanghoa()
    if x.upper() == 'C':
      print("moi ban tao hoa don")
      hoadon.tao_hoadon()
    if x.upper() == 'R':
      hoadon.kiemtrahoadon()

    if x.upper() == 'T':
      hoadon.tongdoanhthu()
    if x.upper() == 'G':
      hoadon.hanghoa_banchay_va_itnhat_nhatthang()
    if x.upper() == "M":
      hoadon.khachhang_muanhieunhat_thang()
    if x.upper() == 'N':
      hoadon.tongso_doanhthu_daban()
    if x.upper() == "D":
      hoadon.ngaybanhang_nhieunhat()
    if x.upper() == 'E':
        print("Tam biet! Hen gap lai")
        break
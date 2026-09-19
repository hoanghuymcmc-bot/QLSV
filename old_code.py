danhsach=[]
sinhvien1={
    "tên" : "hoàng",
    "tuổi" : 20,
    "sdt" : 123,
    "gmail" : "hoang@gmail.com",
    "cccd" : 12345678,
    "trường" : "Bách Khoa",
    "ngành" : "tự động hóa"
}
sinhvien2={
    "tên" : "bảo",
    "tuổi" : 18,
    "sdt" : 234,
    "gmail" : "bao@gmail.com",
    "cccd" : 123456789,
    "trường" :"đại học công nghiệp",
    "ngành" : "lập trình máy tính"
}
danhsach.append(sinhvien1)
danhsach.append(sinhvien2)
while True:
    sinhvien={

      }
    ten=str(input("tên sinh viên:"))
    sinhvien["tên"]=ten
    tuoi=int(input("tuổi:"))
    sinhvien["tuổi"]=tuoi
    sdt=int(input("sdt:"))
    sinhvien["sdt"]=sdt
    gmail=str(input("gmail:"))
    sinhvien["gmail"]=gmail
    cccd=int(input("cccd:"))
    sinhvien["cccd"]=cccd
    truong=str(input("trường:"))
    sinhvien["trường"]=truong
    nganh=str(input("nghành:"))
    sinhvien["nghành"]=nganh
    danhsach.append(sinhvien)
ten_can_tim=str(input("nhập tên sinh viên:"))

for sinhvien in danhsach:

  if sinhvien["tên"]==ten_can_tim:

    print(sinhvien)

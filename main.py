# ===== khơi tạo danh sách sinh viên =====

danhsach = []
sinhvien1 = {
    "tên": "hoàng",
    "tuổi": 20,
    "sdt": 123,
    "gmail": "hoang@gmail.com",
    "cccd": 12345678,
    "trường": "Bách Khoa",
    "ngành": "tự động hóa"
}
sinhvien2 = {
    "tên": "bảo",
    "tuổi": 18,
    "sdt": 234,
    "gmail": "bao@gmail.com",
    "cccd": 123456789,
    "trường": "đại học công nghiệp",
    "ngành": "lập trình máy tính"
} 
danhsach.append(sinhvien1)
danhsach.append(sinhvien2)

# ===== in thông tin sinh viên =====

def in_thong_tin_sinh_vien(danhsach):
    for i in danhsach:
        print("tên: ", i["tên"])
        print("tuổi: ", i["tuổi"])
        print("sdt: ", i["sdt"])
        print("gmail: ", i["gmail"])
        print("cccd: ", i["cccd"])
        print("trường: ", i["trường"])
        print("ngành: ", i["ngành"])
        print("=====================================")

# ===== tìm kiếm sinh viên theo tên =====        

def tim_sinh_vien(danhsach, ten):
    timthay = False
    for i in danhsach:
        if i["tên"] == ten:
            timthay = True
            print("tên: ", i["tên"])
            print("tuổi: ", i["tuổi"])
            print("sdt: ", i["sdt"])
            print("gmail: ", i["gmail"])
            print("cccd: ", i["cccd"])
            print("trường: ", i["trường"])
            print("ngành: ", i["ngành"])
    if not timthay:
        print("không tìm thấy sinh viên")   

# ===== thêm sinh viên =====        

def them_sinh_vien(danhsach):
    sv = {}
    sv["tên"] = str(input("nhập tên: "))
    sv["tuổi"] = int(input("nhập tuổi: "))
    sv["sdt"] = int(input("nhập số điện thoại: "))
    sv["gmail"] = str(input("nhập gmail: "))
    sv["cccd"] = int(input("nhập cccd: "))
    sv["trường"] = str(input("nhập trường: "))
    sv["ngành"] = str(input("nhập ngành: "))
    danhsach.append(sv)             

# ===== sửa thông tin sinh viên theo tên =====

def sua_sinh_vien(danhsach, n):
    timthay=False
    for i in danhsach:
        if i["tên"] == n:
            timthay=True
            i["tên"]=str(input("nhập tên mới: "))
            i["tuổi"]=int(input("nhập tuổi mới: "))
            i["sdt"]=int(input("nhập số điện thoại mới: "))
            i["gmail"]=str(input("nhập gmail mới: "))
            i["cccd"]=int(input("nhập cccd mới: "))
            i["trường"]=str(input("nhập trường mới: "))
            i["ngành"]=str(input("nhập ngành mới: "))
    if timthay==False:
        print("không tìm thấy sinh viên")    

# ===== xóa sinh viên theo tên =====

def xoa_sinh_vien(danhsach, ten):
    timthay = False
    for i in danhsach:
        if i["tên"] == ten:
            timthay = True
            danhsach.remove(i)
            break  
    if not timthay:
        print("không tìm thấy sinh viên")        

# ===== thống kê thông tin sinh viên =====

def thong_ke_sinh_vien(danhsach):
    dem=0
    for i in danhsach:
        dem+=1    
    print("tổng số sinh viên: ", dem)
    tuoitb=0
    for i in danhsach:
        tuoitb += i["tuổi"]
    print("tuổi trung bình: ", tuoitb/dem)
    tuoilonnhat=0
    tuoinhonhat=100
    for i in danhsach:
        if i["tuổi"]>tuoilonnhat:
            tuoilonnhat=i["tuổi"]
        if i["tuổi"]<tuoinhonhat:
            tuoinhonhat=i["tuổi"]
    print("tuổi lớn nhất: ", tuoilonnhat)
    print("tuổi nhỏ nhất: ", tuoinhonhat)

while True:
    print("===== QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị sinh viên")
    print("3. Tìm sinh viên")
    print("4. Sửa sinh viên")
    print("5. Xóa sinh viên")
    print("6. Thống kê")
    print("7. Thoát")

    lua_chon = input("Chọn chức năng: ")

    if lua_chon == "1":
        them_sinh_vien(danhsach)
    elif lua_chon == "2":
        in_thong_tin_sinh_vien(danhsach)
    elif lua_chon == "3":
        ten = input("nhập tên sinh viên cần tìm: ")
        tim_sinh_vien(danhsach, ten)
    elif lua_chon == "4":
        ten = input("nhập tên sinh viên cần sửa: ")
        sua_sinh_vien(danhsach, ten)
    elif lua_chon == "5":
        ten = input("nhập tên sinh viên cần xóa: ")
        xoa_sinh_vien(danhsach, ten)
    if lua_chon == "6":
        thong_ke_sinh_vien(danhsach)
    elif lua_chon == "7":
        break                            

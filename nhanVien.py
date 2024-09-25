        # for in (1,3): => Chi lap 2 lan tai 1 va 3
        # for i in range(1,3): => Chay tu 1 den 2
nhanvien_list = []
stt = 1
for i in range(1,2):  
    print("NHAN VIEN SO"+" "+str(stt))
    name = str(input("Nhap ten nhan vien ne: "))
    namsinh = int(input("Nhap nam sinh nhan vien ne: "))
    maNV = str(input("Nhap ma nhan vien ne: "))
    quequan = str(input("Nhap que quan nhan vien ne: "))
    # LOI 1
        # loi do co gang noi chuoi str + int
        # print(name+" "+namsinh+" "+maNV+" "+quequan)
    # LOI 2
        # for i in range(1,3):
        #    print(name+" "+str(namsinh)+" "+maNV+" "+quequan)
        # nhân viên cuối cùng nhập vào biến name, namsinh, maNV, và quequan bị ghi đè
        # nen ket qua la: Huu Luan 2004 2256st TV
        #                 Huu Luan 2004 2256st TV
    nhanvien_list.append((name, namsinh, maNV, quequan))
    stt += 1 
print("DANH SACH NHAN VIEN CO TRONG LIST: ")
i = 1
for nv in nhanvien_list:
    print(str(i)+ "  " + nv[0] + " " + str(nv[1]) + " " + nv[2] + " " + nv[3])
    i+=1
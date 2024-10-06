print("*************************************************************")
print("Chào mừng bạn đến với Phần mềm tính điểm trung bình!")
print("*************************************************************")
ten = input("Mời nhập Họ và Tên: ")
diemToan = float(input("Nhập điểm môn Toán: "))
diemVan = float(input("Nhập điểm môn Văn: "))
diemAnh = float(input("Nhập điểm môn Anh: "))
diemTB = (diemToan + diemVan + diemAnh) / 3
print (f"Điểm trung bình 3 môn Toán, Văn, Anh của học sinh {ten} là: {diemTB:.2f}")
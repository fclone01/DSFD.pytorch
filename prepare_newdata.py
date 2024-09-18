import os


# Hàm xử lý từng dòng trong file txt
def process_line(line):
    parts = line.split()  # Tách dòng thành các phần tử
    if len(parts) >= 6:  # Đảm bảo có đủ dữ liệu
        coords = [float(coord) for coord in parts[2:]]  # Chuyển đổi các giá trị tọa độ
        rounded_coords = [round(coord) for coord in coords]  # Làm tròn tọa độ
        return (
            " ".join(map(str, rounded_coords)) + " 1 "
        )  # Trả về tọa độ đã làm tròn dưới dạng chuỗi
    return None


# Thư mục chứa các file txt
folder_path_labels = "E:/MY/DATA_FACE_NEW/labels2"  # Thay 'your_folder_path_labels' bằng đường dẫn thư mục chứa các file txt
folder_path_train = "E:/MY/DATA_FACE_NEW/images/train"  # Thay 'your_folder_path_labels' bằng đường dẫn thư mục chứa các file txt
output_file_train = "./data/face_train.txt"
output_file_val = "./data/face_val.txt"

# Mở file rs.txt để ghi
with open(output_file_train, "w") as output_train:
    with open(output_file_val, "w") as output_val:
        # Duyệt qua các file trong thư mục
        print(len(os.listdir(folder_path_labels)))
        for filename in os.listdir(folder_path_labels):
            #             print(filename)
            if filename.endswith(".txt"):
                txt_path = os.path.join(folder_path_labels, filename)
                # Đọc nội dung của file txt
                with open(txt_path, "r") as file:
                    lines = file.readlines()
                    # print(file)
                    jpg_filename = filename.replace(".txt", ".jpg")
                    text_file = f"{jpg_filename} {len(lines)} "
                    for line in lines:
                        text_file += process_line(line)
                        # if processed_line:
                        # Tạo tên file .jpg tương ứng và ghi vào rs.txt
                    if os.path.exists(folder_path_train + "/" + jpg_filename):
                        output_train.write(f"{text_file}\n")
                    else:
                        output_val.write(f"{text_file}\n")

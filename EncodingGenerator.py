
import face_recognition

import cv2
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-c187c-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-c187c.appspot.com"
})
 
data_folder = 'dataset'  # Thư mục chứa dữ liệu
encode_file = 'EncodeFile.pkl'  # Tên tệp chứa mã hóa khuôn mặt

img_list = []
student_ids = []
encode_list_known=[]

print("Encoding Started ...")
for root, dirs, files in os.walk(data_folder):
    for dir_name in dirs:
        # Lấy id học sinh từ tên thư mục
        student_id = dir_name
        student_folder = os.path.join(root, dir_name)
        # Duyệt qua các tệp hình ảnh trong thư mục học sinh
        i=0
        j=0
        for file_name in os.listdir(student_folder):
            file_path = os.path.join(student_folder, file_name)
            # Đọc hình ảnh và thêm vào danh sách
            img = cv2.imread(file_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(img_rgb)
            if len(face_encodings) > 0:
                encode = face_encodings[0]
                encode_list_known.append(encode)
                student_ids.append(student_id)
                i+=1
            else:
                j+=1
                print('anh khong hop le',j)
            print('da ma hoa duoc hinh anh ',i)


# Mã hóa danh sách hình ảnh
print("Encoding Started ...")

encode_list_known_with_ids = [encode_list_known, student_ids]
print("Encoding Complete")

# Lưu danh sách mã hóa vào tệp
with open(encode_file, 'wb') as file:
    pickle.dump(encode_list_known_with_ids, file)
file.close()
print("File Saved")


'''
 

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    print(cv2.imread(os.path.join(folderPath, path)))
    print('khanh')
    print(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
 
 
    # print(path)
    # print(os.path.splitext(path)[0])
print(studentIds)
 
 
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
 
    return encodeList
 
 
print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")
 
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

 '''
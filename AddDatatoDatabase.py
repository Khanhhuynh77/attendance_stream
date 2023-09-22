
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage
import os

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-c187c-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-c187c.appspot.com"
})
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []

#Lưu hình ảnh đại diện trên database 
for path in pathList:

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

ref = db.reference('Students')

data = {
    "0":
        {
            "name": "Unknow"
        },

    "1910001":
        {
            "name": "Lionel Messi",
            "major": "Football player",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
    "1910002":
        {
            "name": "Morgan Freeman",
            "major": "Actor",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
    "1910003":
        {
            "name": "Cristiano Ronaldo",
            "major": "Football player",
            "starting_year": 2019,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910004":
        {
            "name": "Bill Gates",
            "major": "Entrepreneur",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910005":
        {
            "name": "Anne Hathaway",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910006":
        {
            "name": "Brie Larson",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910007":
        {
            "name": "Chris Evans",
            "major": "Actor",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910008":
        {
            "name": "Danielle Panabaker",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910009":
        {
            "name": "Dwayne Johnson",
            "major": "Actor",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910010":
        {
            "name": "Eliza Taylor",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910011":
        {
            "name": "Elizabeth Lail",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910012":
        {
            "name": "Molena Baccarin",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
        "1910013":
        {
            "name": "Emma Watson",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-19 00:54:34"
        },
    "1910014":
        {
            "name": "Leonardo DiCaprio",
            "major": "Actor",
            "starting_year": 2019,
            "total_attendance": 21,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-18 00:54:34"
        },
    "1910015":
        {
            "name": "Jessica Barden",
            "major": "Actress",
            "starting_year": 2019,
            "total_attendance": 21,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-18 00:54:34"
        },       
    "1913719":
        {
            "name": "Huynh Buu Khanh",
            "major": "electronic",
            "starting_year": 2019,
            "total_attendance": 56,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-16 00:54:34"
        }
    }

for key, value in data.items():
    ref.child(key).set(value)
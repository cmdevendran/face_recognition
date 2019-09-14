import face_recognition



image_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')
bill_face_encodings = face_recognition.face_encodings(image_of_bill)[0]


image_of_unknown = face_recognition.load_image_file('./img/unknown/bill-gates-4.jpg')
unknown_face_encodings = face_recognition.face_encodings(image_of_unknown)[0]

# Compare faces

results = face_recognition.compare_faces([bill_face_encodings],unknown_face_encodings)

if results[0]:
    print('Face Matches')
else:
    print('Face doesn\'t match ')



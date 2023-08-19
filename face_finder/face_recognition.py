from deepface import DeepFace

from face_finder import find_faces

def face_verify(user_id) -> dict:
    image_path_database = find_faces(user_id)
    new_image_path = "./123.jpg" 
    verify_result = DeepFace.verify(img1_path=image_path_database, img2_path=new_image_path)
    print(verify_result)


face_verify("123")
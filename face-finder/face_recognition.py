from deepface import DeepFace

from face_finder import find_faces

def face_verify(user_id) -> dict:
    image_path_database = "foto.jpg"
    new_image_path = "./123.jpg" 
    verify_result = DeepFace.verify(img1_path="./face-finder/foto.jpg", img2_path="./face-finder/123.jpg")
    print(verify_result)


face_verify("123")
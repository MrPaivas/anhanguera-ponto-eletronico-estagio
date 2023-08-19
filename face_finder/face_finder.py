import os


def find_faces(id_user):
    image_path = f"./face_finder/faces_database/{id_user}.jpg"
    
    if os.path.exists(image_path):
        return image_path
    else:
        raise Exception("Usuário sem imagem cadastrada")
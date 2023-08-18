import os


def find_faces(id_user):
    image_path = f"./faces_database/"
    image = id_user + ".jpg"
    if os.path.exists("./faces_database/123.jpg"):
        return image_path
    else:
        raise Exception("Usuário sem imagem cadastrada")
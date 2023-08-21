from deepface import DeepFace


def face_verify(img_path1, img_path2 ) -> dict:
    verify_result = DeepFace.verify(img1_path=img_path1, img2_path=img_path2)
    return verify_result
import os
import asyncio

async def make_dir_estagiario(matricula: str):
    dir_path = f"./face_finder/faces_database/{matricula}"
    
    if os.path.exists(dir_path):
        return dir_path
    
    os.makedirs(dir_path)
    return dir_path
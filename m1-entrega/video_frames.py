from pathlib import Path
import cv2

# Caminhos globais dos diretórios pra evitar erros
base_dir = Path(__file__).resolve().parent
video_path = base_dir / 'video' / '2D_test_animation.mp4'
output_dir = base_dir / 'frame_output'
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / 'frame_do_meio.jpg'

video = cv2.VideoCapture(str(video_path))

if not video.isOpened():
    raise FileNotFoundError(f"Vídeo não foi encontrado no caminho: {video_path}")

total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

frame_do_meio = total_frames // 2

# Não estava conseguindo acessar o vídeo devido ao alto consumo da RAM (array)
# então utilizei o método disponibilizado pela própria lib
video.set(cv2.CAP_PROP_POS_FRAMES, frame_do_meio)
success, frame = video.read()

if not success or frame is None:
    raise RuntimeError(f"Falha ao ler o frame de índice {frame_do_meio}.")

cv2.imwrite(str(output_path), frame)
video.release()

print(f'Total de frames do vídeo: {total_frames}')
print(f'Frame do meio ({frame_do_meio}) salvo em: {output_path}')

# COMENTÁRIO EXPLICATIVO SOBRE O VÍDEO:
"""
O vídeo é representado por uma série de frames exibidos em sequência, em uma
taxa de FPS. Cada imagem é representada por uma grade de pixels. E cada pixel
é representado por canais de 3 cores RGB ou BGR de 0 a 255.
"""

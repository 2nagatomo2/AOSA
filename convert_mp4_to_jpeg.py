import os
import subprocess  # ターミナルで実行するコマンドを実行できる


# 動画が保存されたフォルダにある、クラスの種類とパスを取得
dir_path = 'data/revised-data/left-handed'
class_list = os.listdir(path=dir_path)
print(class_list)

# 各クラスの動画ファイルを画像ファイルに変換する
for class_list_i in (class_list):  # クラスごとのループ

    # クラスのフォルダへのパスを取得
    class_path = os.path.join(dir_path, class_list_i)

    # 各クラスのフォルダ内の動画ファイルをひとつずつ処理するループ
    for file_name in os.listdir(class_path):

        # ファイル名と拡張子に分割
        name, ext = os.path.splitext(file_name)

        # mp4ファイルでない、フォルダなどは処理しない
        if ext != '.mp4':
            continue

        # 動画ファイルを画像に分割して保存するフォルダ名を取得
        dst_directory_path = os.path.join(class_path, name)

        # 上記の画像保存フォルダがなければ作成
        if not os.path.exists(dst_directory_path):
            os.mkdir(dst_directory_path)

        # 動画ファイルへのパスを取得
        video_file_path = os.path.join(class_path, file_name)

        # ffmpegを実行させ、動画ファイルをjpgにする （高さは256ピクセルで幅はアスペクト比を変えない）
        # kineticsの動画の場合10秒になっており、大体300ファイルになる（30 frames /sec）
        cmd = 'ffmpeg -i \"{}\" -vf scale=-1:256 \"{}/image_%05d.jpg\"'.format(
            video_file_path, dst_directory_path)
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')

print("動画ファイルを画像ファイルに変換しました。")
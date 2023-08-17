import os
import subprocess


def convert_flv_to_mkv(input_folder1, output_folder2):
    for root, dirs, files in os.walk(input_folder1):
        for file in files:
            if file.endswith(".Flv"):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_folder2, file.replace(".Flv", ".mkv"))
                ffmpeg_cmd = f"E:/ffmpeg-2021-11-07-git-45dc668aea-essentials_build/bin/ffmpeg.exe -i \"{input_file_path}\" -c:v h264_nvenc \"{output_file_path}\""

                try:
                    subprocess.run(ffmpeg_cmd, shell=True, check=True)
                    print(f"Converted {input_file_path} to {output_file_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Conversion of {input_file_path} failed: {e}")


if __name__ == "__main__":
    input_folder = "floder"  # 替换为包含FLV文件的文件夹路径
    output_folder = "floder"  # 替换为输出MKV文件的文件夹路径

    convert_flv_to_mkv(input_folder, output_folder)
    print('1')

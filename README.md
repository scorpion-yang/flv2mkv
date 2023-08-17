# flv2mkv

## 简介

使用Python和ffmpeg批量转换flv格式文件到mkv

## 使用方法

可自己修改main文件中

修改ffmpeg的安装位置

若电脑不支持独立显卡硬件加速，可以删除 -c:v h264_nvenc 

```python3
input_folder = "floder"  	# 替换为包含FLV文件的文件夹路径
output_folder = "floder" 	 # 替换为输出MKV文件的文件夹路径
ffmpeg_cmd = f"E:/ffmpeg-2021-11-07-git-45dc668aea-essentials_build/bin/ffmpeg.exe -i \"{input_file_path}\" -c:v h264_nvenc \"{output_file_path}\""
```


<font color=red>注意自己的文件格式是Flv还是flv，按实际修改文件中的大小写，否则无法完成转换</font>

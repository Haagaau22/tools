#!/bin/bash

# 视频目录（包含视频文件的文件夹路径）
VIDEO_DIR=$1

# MP3目录（输出MP3文件的文件夹路径）
MP3_DIR=$2

# 检查是否提供了足够的参数
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <video_dir> <mp3_dir>"
  exit 1
fi

# 检查视频目录是否存在
if [ ! -d "$VIDEO_DIR" ]; then
  echo "Video directory not found: $VIDEO_DIR"
  exit 1
fi

# 创建MP3目录（如果它不存在）
mkdir -p "$MP3_DIR"

# 转换所有视频
for file in "$VIDEO_DIR"/*; do
  # 获取不带路径的文件名
  filename=$(basename -- "$file")
  # 获取不带扩展名的文件名
  base=${filename%.*}
  # 定义输出文件的路径
  output="$MP3_DIR/$base.mp3"

  # 转换视频文件到MP3
  # ffmpeg -i "$file" -vn -ar 44100 -ac 2 -ab 192k "$output"

  # 检查MP3文件是否已存在
  if [ ! -f "$output" ]; then
    # MP3文件不存在，执行转换
    ffmpeg -i "$file" -vn -ar 44100 -ac 2 -ab 192k "$output"
  else
    # MP3文件已存在，跳过转换
    echo "Skipping $filename, MP3 already exists."
  fi
done

echo "Conversion complete!"


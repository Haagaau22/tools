URL=$1


# 检查是否提供了足够的参数
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# youtube-dl -x --audio-format mp3 "$URL"
yt-dlp -N 16 -x --audio-format mp3 "$URL"

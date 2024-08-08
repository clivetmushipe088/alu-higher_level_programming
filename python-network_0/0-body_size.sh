#!/bin/bash
" n "
heck if a URL was provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to send a request to the URL and get the size of the body in bytes
size=$(curl -s -o /dev/null -w '%{size_download}' "$1")

# Display the size in bytes
echo "Size of the response body: $size bytes"


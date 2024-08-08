#!/bin/bash
# Script to get the size of the response body in bytes
echo "Size of the response body: $(curl -s -o /dev/null -w '%{size_download}' "$1") bytes"


#!/bin/bash
# Displaying all HTTP methods the server will accept
curl -I -X OPTIONS -s "$1" | grep Allow | cut -d' ' -f2-

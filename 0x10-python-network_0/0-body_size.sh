#!/bin/bash
# get the size of the header
curl -size_download "$1" | grep "Content-Length:" | cut -d " " -f 2

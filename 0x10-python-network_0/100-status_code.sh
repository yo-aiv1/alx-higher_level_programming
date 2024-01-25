#!/bin/bash
# displays only the status code of the response after sending a request to a URL passed as an argument
curl -so /dev/null -w "%{http_code}" "$1"

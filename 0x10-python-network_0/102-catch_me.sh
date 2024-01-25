#!/bin/bash
# display the "You got me!" message by sending a request
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:School"

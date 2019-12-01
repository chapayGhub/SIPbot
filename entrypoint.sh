#!/bin/sh

cat <<EOF >/sipbot.config
reg_info = $REG_INFO
reg_host = $REG_HOST
reg_user = $REG_USER
reg_pass = $REG_PASS
reg_timeout = $REG_TIMEOUT
program_name = /sipbot.py
max_concurrent_calls = 1
EOF

env | grep ^AUTHORISED_ | cut -d= -f2- >/authorised.txt

exec /sipbot -c /sipbot.config

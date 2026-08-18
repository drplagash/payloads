# Annotated Strings

Extracted strings grouped for human triage. URLs/domains are defanged where practical.

## Network URLs

- No clear URLs found.


## IP addresses

- `Mozilla/5[.]0 (Windows NT 10[.]0; Win64; x64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/120[.]0[.]0[.]0 Safari/537[.]36`
- `Mozilla/5[.]0 (X11; Linux x86_64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/119[.]0[.]0[.]0 Safari/537[.]36`
- `Mozilla/5[.]0 (Windows NT 10[.]0; Win64; x64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/120[.]0[.]0[.]0 Safari/537[.]36 Edg/120[.]0[.]0[.]0`


## Shell commands or command fragments

- `User-Agent: curl/8.0`
- `/system/bin/sh`
- `/apex/com.android.runtime/bin/sh`
- `/vendor/bin/sh`
- `/usr/bin/sh`


## Filesystem paths

- `C/0$Q/0$`
- `4$Q/ $`
- `GET %s HTTP/1.1`
- `Accept: */*`
- `HEAD %s HTTP/1.1`
- `POST %s HTTP/1.1`
- `Content-Type: application/x-www-form-urlencoded`
- `POST /client HTTP/1.1`
- `User-Agent: CitizenFX/1`
- `GET /info.json HTTP/1.1`
- `User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0`
- `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0`
- `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15`
- `POST %s HTTP/1.0`
- `Accept: application/json`
- `Content-Type: application/json`
- `HTTP/1.`
- `/proc/self/comm`
- `%s%s/comm`
- `%s%s/cmdline`
- `%s%s/oom_score_adj`
- `/usr/`
- `/bin/`
- `/sbin/`
- `/system/`
- `%s%s/maps`
- `/proc`
- `/proc/`
- `/lib/`
- `/proc/net/route`
- `/etc/resolv.conf`
- `/system/bin/toybox`
- `/proc/sys/kernel/hostname`
- `/dev/ptmx`
- `/sbin:/system/sbin:/system/bin:/system/xbin:/vendor/bin:/bin:/usr/bin:/usr/local/bin`
- `/usr/bin/bash`
- `/data/local/tmp/sh`
- `/sbin/sh`
- `/system/build.prop`
- `/vendor/build.prop`
- `/product/build.prop`
- `/odm/build.prop`
- `/system/bin/getprop`
- `/vendor/bin/getprop`
- `/bin/getprop`
- `local/tmp`
- `/data/local/tmp`
- `%s/local/tmp`
- `/proc/mounts`
- `%s/%s`
- `/dev/urandom`
- `%)+/5;=CGIOSYaegkmq`
- `/etc/passwd`
- `Input/output error`
- `Remote I/O error`
- `/dev/pts/`
- `/dev/null`
- `/etc/config/resolv.conf`
- `RPC: Program/version mismatch`
- `/etc/hosts`
- `/etc/config/hosts`


## Runtime/process hints

- `Connection: keep-alive`
- `execcmdshere`
- `Connection: close`
- `noexec`
- `Exec format error`
- `Cannot exec a shared library directly`
- `Socket operation on non-socket`
- `Protocol wrong type for socket`
- `Socket type not supported`
- `Network dropped connection on reset`
- `Software caused connection abort`
- `Connection reset by peer`
- `Transport endpoint is already connected`
- `Transport endpoint is not connected`
- `Connection timed out`
- `Connection refused`
- `__get_myaddress: socket`


## Suspicious keywords

- `bot-tx-v1`
- `bot-rx-v1`
- `bot-auth-v1`
- `mips64`
- `mipsel`
- `armv7`
- `armv5`
- `armv8`
- `x86_64`


## Other interesting strings

- `79SH4BSL`
- `CBf$UBf$`
- `CBf$TBf$`
- `?v=%u&r=`
- `Host: %s`
- `User-Agent: %s`
- `Accept-Encoding: gzip, deflate`
- `Content-Length: %d`
- `method=getEndpoints&token=`
- `method=getConfiguration`
- `localhost`
- `token=%s&sid=%s&nonce=%u&seq=%u`
- `token=%s&sid=%s&x=%u`
- `0123456789abcdef`
- `token=%s&guid=%s`
- `getinfo xxx`
- `{"jsonrpc":"2.0","method":"eth_call","params":[{"to":"0x%s","data":"%s"},"latest"],"id":1}`
- `"jsonrpc"`
- `Transfer-Encoding:`
- `"result"`
- `Content-Length: %zu`
- `%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x`
- `reason=var_run`
- `reason=var_tmp`
- `reason=tmp`
- `reason=root`
- `reason=dev`
- `reason=blocklist`
- `behavior`
- `[unknown]`
- `MemTotal: %lu kB`
- `Mem: %lu`
- `.in-addr.arpa`
- `%*s %x %x %x`
- `nameserver`
- `%d.%d.%d.%d`
- `xterm-256color`
- `HOSTNAME`
- `ro.product.model`
- `ro.product.device`
- `ro.product.name`
- `ro.product.brand`
- `net.hostname`
- `ANDROID_DATA`
- `Content-Length:`
- `EXTERNAL_STORAGE`
- `devtmpfs`
- `configfs`
- `binfmt_misc`
- `securityfs`
- `hugetlbfs`
- `rpc_pipefs`
- `squashfs`
- `AES-128-ECB`
- `AES-192-ECB`
- `AES-256-ECB`
- `AES-128-CBC`
- `AES-192-CBC`
- `AES-256-CBC`
- `AES-128-GCM`
- `AES-192-GCM`
- `AES-256-GCM`
- `secp256r1`
- `O?Y^eG_r`
- `hmacSHA256`
- `HMAC-SHA-256`
- `id-sha256`
- `des-ede3-cbc`
- `DES-EDE3-CBC`
- `aes128-cbc`
- `AES128-CBC`
- `aes192-cbc`
- `AES192-CBC`
- `aes256-cbc`
- `AES256-CBC`
- `rsaEncryption`
- `id-ecPublicKey`
- `Generic EC key`
- `EC key for ECDH`
- `sha256WithRSAEncryption`


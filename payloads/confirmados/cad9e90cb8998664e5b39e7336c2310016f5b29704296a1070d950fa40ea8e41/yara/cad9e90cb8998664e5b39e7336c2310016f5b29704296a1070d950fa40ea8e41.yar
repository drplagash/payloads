rule Oraculo_payload_cad9e90cb8998664
{
  meta:
    author = "Oraculo SOC"
    purpose = "defensive detection and hunting"
    sha256 = "cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41"
    sha1 = "5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3"
    md5 = "620c007093f64dfe672252c0bd483f25"
    size = "448624"
  strings:
    $s0 = "C/0$Q/0$" ascii wide
    $s1 = "GET %s HTTP/1.1" ascii wide
    $s2 = "Accept: */*" ascii wide
    $s3 = "HEAD %s HTTP/1.1" ascii wide
    $s4 = "POST %s HTTP/1.1" ascii wide
    $s5 = "Content-Type: application/x-www-form-urlencoded" ascii wide
    $s6 = "POST /client HTTP/1.1" ascii wide
    $s7 = "User-Agent: CitizenFX/1" ascii wide
    $s8 = "GET /info.json HTTP/1.1" ascii wide
    $s9 = "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0" ascii wide
    $s10 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0" ascii wide
    $s11 = "POST %s HTTP/1.0" ascii wide
  condition:
    uint32(0) == 0x464c457f and 2 of them
}

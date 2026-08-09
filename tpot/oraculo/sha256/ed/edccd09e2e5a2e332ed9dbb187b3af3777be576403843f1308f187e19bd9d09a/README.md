# 🧬 Payload Analysis

`edccd09e2e5a2e332ed9dbb187b3af3777be576403843f1308f187e19bd9d09a`

## 📌 Resumen

Botnet registrado por Oráculo SOC. 77 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `edccd09e2e5a2e332ed9dbb187b3af3777be576403843f1308f187e19bd9d09a`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 4095 |
| Entropía | 5.28 |

## 🧬 Detecciones

- YARA: `Suspicious_BusyBox_Mirai`
- YARA: `Suspicious_Shell_Script`
- YARA: `0x12c:$wget1:`
- YARA: `0xcc4:$chmod:`
- YARA: `0x124:$busy1:`
- YARA: `0x179:$chmod:`
- YARA: `0x1c5:$wget1:`
- YARA: `0x261:$wget1:`
- YARA: `0x2fd:$wget1:`
- YARA: `0x399:$wget1:`
- YARA: `0x435:$wget1:`
- YARA: `0x4d1:$wget1:`
- YARA: `0x56d:$wget1:`
- YARA: `0x606:$wget1:`
- YARA: `0x69f:$wget1:`
- YARA: `0x738:$wget1:`
- YARA: `0x7d1:$wget1:`
- YARA: `0x995:$curl1:`
- YARA: `0xa26:$curl1:`
- YARA: `0xaba:$curl1:`
- YARA: `0xb4e:$curl1:`
- YARA: `0xbe2:$curl1:`
- YARA: `0xc76:$curl1:`
- YARA: `0xd0a:$curl1:`
- YARA: `0xd9e:$curl1:`
- YARA: `0xe2f:$curl1:`
- YARA: `0xec0:$curl1:`
- YARA: `0xf51:$curl1:`
- YARA: `0xfe2:$curl1:`
- YARA: `0x213:$chmod:`
- YARA: `0x2af:$chmod:`
- YARA: `0x34b:$chmod:`
- YARA: `0x3e7:$chmod:`
- YARA: `0x483:$chmod:`
- YARA: `0x51f:$chmod:`
- YARA: `0x5ba:$chmod:`
- YARA: `0x653:$chmod:`
- YARA: `0x6ec:$chmod:`
- YARA: `0x785:$chmod:`
- YARA: `0x821:$chmod:`
- YARA: `0x9e2:$chmod:`
- YARA: `0xa74:$chmod:`
- YARA: `0xb08:$chmod:`
- YARA: `0xb9c:$chmod:`
- YARA: `0xc30:$chmod:`
- YARA: `0xd58:$chmod:`
- YARA: `0xdeb:$chmod:`
- YARA: `0xe7c:$chmod:`
- YARA: `0xf0d:$chmod:`
- YARA: `0xf9e:$chmod:`
- YARA: `0x1bd:$busy1:`
- YARA: `0x259:$busy1:`
- YARA: `0x2f5:$busy1:`
- YARA: `0x391:$busy1:`
- YARA: `0x42d:$busy1:`
- YARA: `0x4c9:$busy1:`
- YARA: `0x565:$busy1:`
- YARA: `0x5fe:$busy1:`
- YARA: `0x697:$busy1:`
- YARA: `0x730:$busy1:`
- YARA: `0x7c9:$busy1:`
- YARA: `0x47d:$arch1:`
- YARA: `0x4a0:$arch1:`
- YARA: `0x4bb:$arch1:`
- YARA: `0xcbe:$arch1:`
- YARA: `0xce1:$arch1:`
- YARA: `0xcfc:$arch1:`
- YARA: `0x780:$arch3:`
- YARA: `0x7a2:$arch3:`
- YARA: `0x7bc:$arch3:`
- YARA: `0x819:$arch3:`
- YARA: `0x83e:$arch3:`
- YARA: `0x85b:$arch3:`
- YARA: `0xf99:$arch3:`
- YARA: `0xfbb:$arch3:`
- YARA: `0xfd5:$arch3:`
- YARA: `__YARA_SENTINEL_NO_MATCH__`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

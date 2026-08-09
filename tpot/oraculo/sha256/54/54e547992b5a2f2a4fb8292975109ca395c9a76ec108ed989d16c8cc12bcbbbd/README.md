# 🧬 Payload Analysis

`54e547992b5a2f2a4fb8292975109ca395c9a76ec108ed989d16c8cc12bcbbbd`

## 📌 Resumen

Botnet registrado por Oráculo SOC. 7 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:48+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `54e547992b5a2f2a4fb8292975109ca395c9a76ec108ed989d16c8cc12bcbbbd`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 4095 |
| Entropía | 5.32 |

## 🧬 Detecciones

- YARA: `Suspicious_BusyBox_Mirai`
- YARA: `0xa0f:$bot1:`
- YARA: `0x584:$loader1:`
- YARA: `0x6d3:$loader1:`
- YARA: `0x78e:$loader1:`
- YARA: `0x99b:$loader1:`
- YARA: `__YARA_SENTINEL_NO_MATCH__`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

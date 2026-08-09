# 🧬 Payload Analysis

`d12f2cee37a0f946b84ea982d6a0860ecb2e96d61745e2d923085bf1227b58c1`

## 📌 Resumen

Botnet registrado por Oráculo SOC. 7 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:40:51+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `d12f2cee37a0f946b84ea982d6a0860ecb2e96d61745e2d923085bf1227b58c1`

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

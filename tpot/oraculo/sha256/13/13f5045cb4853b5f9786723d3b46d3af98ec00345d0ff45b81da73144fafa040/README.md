# 🧬 Payload Analysis

`13f5045cb4853b5f9786723d3b46d3af98ec00345d0ff45b81da73144fafa040`

## 📌 Resumen

Web shell registrado por Oráculo SOC. 18 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:42:13+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `13f5045cb4853b5f9786723d3b46d3af98ec00345d0ff45b81da73144fafa040`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 4095 |
| Entropía | 5.6 |

## 🧬 Detecciones

- YARA: `Suspicious_PHP_Webshell`
- YARA: `0x43c:$php1:`
- YARA: `0x643:$php1:`
- YARA: `0x823:$php1:`
- YARA: `0x92b:$php1:`
- YARA: `0xa2f:$php1:`
- YARA: `0xb2f:$php1:`
- YARA: `0xc36:$php1:`
- YARA: `0xd49:$php1:`
- YARA: `0xe4e:$php1:`
- YARA: `0xf4f:$php1:`
- YARA: `0x448:$exec1:`
- YARA: `0x64f:$exec1:`
- YARA: `0x442:$shell1:`
- YARA: `0x649:$shell1:`
- YARA: `0x44d:$base64d:`
- YARA: `0x654:$base64d:`
- YARA: `__YARA_SENTINEL_NO_MATCH__`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

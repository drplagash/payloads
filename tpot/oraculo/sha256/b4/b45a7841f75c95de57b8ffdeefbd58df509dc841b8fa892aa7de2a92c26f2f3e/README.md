# 🧬 Payload Analysis

`b45a7841f75c95de57b8ffdeefbd58df509dc841b8fa892aa7de2a92c26f2f3e`

## 📌 Resumen

Web shell registrado por Oráculo SOC. 10 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `b45a7841f75c95de57b8ffdeefbd58df509dc841b8fa892aa7de2a92c26f2f3e`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 1848 |
| Entropía | 5.8 |

## 🧬 Detecciones

- YARA: `Suspicious_PHP_Webshell`
- YARA: `0x43c:$php1:`
- YARA: `0x643:$php1:`
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

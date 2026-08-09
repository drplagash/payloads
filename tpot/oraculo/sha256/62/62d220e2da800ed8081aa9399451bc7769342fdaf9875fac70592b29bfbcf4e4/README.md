# 🧬 Payload Analysis

`62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4`

## 📌 Resumen

Web shell registrado por Oráculo SOC. 14 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `62d220e2da800ed8081aa9399451bc7769342fdaf9875fac70592b29bfbcf4e4`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 2380 |
| Entropía | 5.85 |

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
- YARA: `0x857:$php1:`
- YARA: `0x863:$exec1:`
- YARA: `0x85d:$shell1:`
- YARA: `0x868:$base64d:`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

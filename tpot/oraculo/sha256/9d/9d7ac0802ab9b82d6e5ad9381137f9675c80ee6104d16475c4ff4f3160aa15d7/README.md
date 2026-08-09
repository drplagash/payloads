# 🧬 Payload Analysis

`9d7ac0802ab9b82d6e5ad9381137f9675c80ee6104d16475c4ff4f3160aa15d7`

## 📌 Resumen

Web shell registrado por Oráculo SOC. 6 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:29+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `9d7ac0802ab9b82d6e5ad9381137f9675c80ee6104d16475c4ff4f3160aa15d7`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 1329 |
| Entropía | 5.67 |

## 🧬 Detecciones

- YARA: `Suspicious_PHP_Webshell`
- YARA: `0x43c:$php1:`
- YARA: `0x448:$exec1:`
- YARA: `0x442:$shell1:`
- YARA: `0x44d:$base64d:`
- YARA: `__YARA_SENTINEL_NO_MATCH__`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

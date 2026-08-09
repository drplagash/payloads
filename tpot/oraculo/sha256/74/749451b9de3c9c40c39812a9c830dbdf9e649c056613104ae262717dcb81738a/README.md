# 🧬 Payload Analysis

`749451b9de3c9c40c39812a9c830dbdf9e649c056613104ae262717dcb81738a`

## 📌 Resumen

Web shell registrado por Oráculo SOC. 24 coincidencias YARA.

## 🏷️ Clasificación

- **Categoría:** `Web shell`
- **Familia:** `webshell`
- **Confianza:** `0.9`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:39:48+00:00`
- **Modo:** `automatic_snapshot`

## 🔐 Identidad

- **SHA256:** `749451b9de3c9c40c39812a9c830dbdf9e649c056613104ae262717dcb81738a`

## 🧪 Análisis del artefacto

| Propiedad | Resultado |
| --- | --- |
| Tipo | payload |
| Tamaño | 4095 |
| Entropía | 5.84 |

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
- YARA: `0xa6c:$php1:`
- YARA: `0xc7b:$php1:`
- YARA: `0xe5b:$php1:`
- YARA: `0xf63:$php1:`
- YARA: `0x863:$exec1:`
- YARA: `0xa78:$exec1:`
- YARA: `0xc87:$exec1:`
- YARA: `0x85d:$shell1:`
- YARA: `0xa72:$shell1:`
- YARA: `0xc81:$shell1:`
- YARA: `0x868:$base64d:`
- YARA: `0xa7d:$base64d:`
- YARA: `0xc8c:$base64d:`

## 🛡️ Nota de publicación

Este informe es una **fotografía inmutable del momento de registro**. No se publican marcas temporales de observación ni contadores que requieran actualización posterior.

Las direcciones IPv4 públicas se publican con el último octeto como `XXX`; las direcciones internas y material sensible se redactan antes de salir de Oráculo SOC.

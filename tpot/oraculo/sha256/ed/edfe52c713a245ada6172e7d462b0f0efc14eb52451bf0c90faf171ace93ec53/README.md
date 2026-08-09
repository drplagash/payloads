# 🧬 Payload Analysis

`edfe52c713a245ada6172e7d462b0f0efc14eb52451bf0c90faf171ace93ec53`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:23:38+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `edfe52c713a245ada6172e7d462b0f0efc14eb52451bf0c90faf171ace93ec53`
- **SHA1:** `7bdbb8797efeaf52875c2be0f48695aefaa6710a`
- **MD5:** `be68f6f402598d03d31fb1af791db91b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 221 B |
| Entropía | 5.09 |
| Strings | 7 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.68.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | edfe52c713a245ada6172e7d462b0f0efc14eb52451bf0c90faf171ace93ec53 | static_analysis |
| command | User-Agent: curl/7.68.0 | strings |
| ip | 82.49.235.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

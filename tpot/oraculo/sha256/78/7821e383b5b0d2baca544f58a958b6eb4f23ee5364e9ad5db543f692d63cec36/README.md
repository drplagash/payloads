# 🧬 Payload Analysis

`7821e383b5b0d2baca544f58a958b6eb4f23ee5364e9ad5db543f692d63cec36`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/7821e383b5b0d2baca544f58a958b6eb4f23ee5364e9ad5db543f692d63cec36.md](../../../../../malware-like/oraculo/botnet/7821e383b5b0d2baca544f58a958b6eb4f23ee5364e9ad5db543f692d63cec36.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7821e383b5b0d2baca544f58a958b6eb4f23ee5364e9ad5db543f692d63cec36`
- **MD5:** `04fedf2c29808f31c3c909ac2f2d3a95`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (1216), with CRLF line terminators |
| Tamaño | 2.8 KiB |
| Entropía | 5.95 |
| Strings | 9 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (1216), with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
config set dir /var/spool/cron/
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 8.219.145.XXX | static_analysis |
| command | config set dir /var/spool/cron/ | strings |
| hash | 7821e383b5b0d2baca544f58a958b6eb4f23ee5364e9ad5db543f692d63cec36 | static_analysis |
| ip | 124.236.108.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

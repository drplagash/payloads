# 🧬 Payload Analysis

`1c3f58f1c4393df7e1d146490584d5f75a2e727fd147fc22df3c04da990040dd`

## 📌 Resumen

Artefacto de 626 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.99. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1c3f58f1c4393df7e1d146490584d5f75a2e727fd147fc22df3c04da990040dd`
- **MD5:** `15007909b869a68cd17e5debf01b1489`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 626 B |
| Entropía | 4.99 |
| Strings | 20 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
User-Agent: Wget/1.25.0 (linux-gnu)
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 41.216.189.XXX | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| hash | 1c3f58f1c4393df7e1d146490584d5f75a2e727fd147fc22df3c04da990040dd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

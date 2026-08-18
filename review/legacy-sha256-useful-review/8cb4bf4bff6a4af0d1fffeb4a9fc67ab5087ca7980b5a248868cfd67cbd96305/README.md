# 🧬 Payload Analysis

`8cb4bf4bff6a4af0d1fffeb4a9fc67ab5087ca7980b5a248868cfd67cbd96305`

## 📌 Resumen

Artefacto de 4.0 KiB. Presenta entropía elevada (7.77), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8cb4bf4bff6a4af0d1fffeb4a9fc67ab5087ca7980b5a248868cfd67cbd96305`
- **SHA1:** `2d550c9ce150d1ec0fc48dbb9794669885ad420c`
- **MD5:** `a8752e651b788f4f28348689083f1126`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.77 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/tv.apkOKAY
/data/local/tmp/tv.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/tv.apkOKAY | strings |
| command | /data/local/tmp/tv.apk,33261DATA | strings |
| hash | 8cb4bf4bff6a4af0d1fffeb4a9fc67ab5087ca7980b5a248868cfd67cbd96305 | static_analysis |
| ip | 119.207.147.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

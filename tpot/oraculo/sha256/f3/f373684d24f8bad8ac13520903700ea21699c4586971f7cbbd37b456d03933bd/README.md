# 🧬 Payload Analysis

`f373684d24f8bad8ac13520903700ea21699c4586971f7cbbd37b456d03933bd`

## 📌 Resumen

Artefacto de 3.1 KiB. Presenta entropía elevada (7.70), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f373684d24f8bad8ac13520903700ea21699c4586971f7cbbd37b456d03933bd`
- **SHA1:** `e645b94a12c7264914576cfd15aabf5e2122194a`
- **MD5:** `d648198e05f36414bca896f88ac86cce`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.1 KiB |
| Entropía | 7.7 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apkOKAY
/data/local/tmp/ufo.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| hash | f373684d24f8bad8ac13520903700ea21699c4586971f7cbbd37b456d03933bd | static_analysis |
| ip | 121.145.50.XXX | artifact_source |

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

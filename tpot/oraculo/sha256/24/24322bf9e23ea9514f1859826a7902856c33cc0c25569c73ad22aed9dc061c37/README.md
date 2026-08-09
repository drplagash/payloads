# 🧬 Payload Analysis

`24322bf9e23ea9514f1859826a7902856c33cc0c25569c73ad22aed9dc061c37`

## 📌 Resumen

Artefacto de 2.9 KiB. Presenta entropía elevada (7.68), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `24322bf9e23ea9514f1859826a7902856c33cc0c25569c73ad22aed9dc061c37`
- **SHA1:** `121f29afeac90ba6c6426a8aef8b4e33bd2971ed`
- **MD5:** `a372275b0dd9f49c36d66b844621d56e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 2.9 KiB |
| Entropía | 7.68 |
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
| hash | 24322bf9e23ea9514f1859826a7902856c33cc0c25569c73ad22aed9dc061c37 | static_analysis |
| ip | 2.193.129.XXX | artifact_source |

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

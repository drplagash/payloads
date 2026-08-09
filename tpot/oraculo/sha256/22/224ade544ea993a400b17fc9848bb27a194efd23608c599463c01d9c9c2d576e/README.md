# 🧬 Payload Analysis

`224ade544ea993a400b17fc9848bb27a194efd23608c599463c01d9c9c2d576e`

## 📌 Resumen

Artefacto de 3.0 KiB. Presenta entropía elevada (7.69), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `224ade544ea993a400b17fc9848bb27a194efd23608c599463c01d9c9c2d576e`
- **MD5:** `eb57f4fb7ba4d1852209d9ee80ef2e02`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.0 KiB |
| Entropía | 7.69 |
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
| hash | 224ade544ea993a400b17fc9848bb27a194efd23608c599463c01d9c9c2d576e | static_analysis |
| ip | 117.68.74.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

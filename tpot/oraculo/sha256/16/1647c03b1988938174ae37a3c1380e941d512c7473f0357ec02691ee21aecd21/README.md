# 🧬 Payload Analysis

`1647c03b1988938174ae37a3c1380e941d512c7473f0357ec02691ee21aecd21`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como TeX packed font data (\002)M\254o\345z\2567d\234.[`\265\245\341\243z\0114\372). Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1647c03b1988938174ae37a3c1380e941d512c7473f0357ec02691ee21aecd21`
- **SHA1:** `e7339162670c47ccc31185f1c056355e8b54ddce`
- **MD5:** `4e6d114cbd62cb728a86cfd42ec928b4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | TeX packed font data (\002)M\254o\345z\2567d\234.[`\265\245\341\243z\0114\372) |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=TeX packed font data (\002)M\254o\345z\2567d\234.[`\265\245\341\243z\0114\372); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1647c03b1988938174ae37a3c1380e941d512c7473f0357ec02691ee21aecd21 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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

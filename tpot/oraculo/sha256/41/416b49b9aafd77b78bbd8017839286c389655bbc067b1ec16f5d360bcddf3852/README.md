# 🧬 Payload Analysis

`416b49b9aafd77b78bbd8017839286c389655bbc067b1ec16f5d360bcddf3852`

## 📌 Resumen

Artefacto de 3.6 KiB. Entropía registrada: 6.60. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `416b49b9aafd77b78bbd8017839286c389655bbc067b1ec16f5d360bcddf3852`
- **MD5:** `252e9e516bfc819729ac26ec7c5498b6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.6 KiB |
| Entropía | 6.6 |
| Strings | 11 |

## 🧠 Comportamiento observado

1. **Limpieza**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
shell:rm -rf /data/local/tmp/*
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | shell:rm -rf /data/local/tmp/* | strings |
| hash | 416b49b9aafd77b78bbd8017839286c389655bbc067b1ec16f5d360bcddf3852 | static_analysis |
| ip | 203.229.224.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

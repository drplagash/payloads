# 🧬 Payload Analysis

`88ec022c9ee0d46c8ae7ea0b4d1b36669694e8e6dc02286af3826f3c7aa43dd9`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 6.66. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:19.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `88ec022c9ee0d46c8ae7ea0b4d1b36669694e8e6dc02286af3826f3c7aa43dd9`
- **MD5:** `2dbdec6e6c74388e9e9b7ec32ab2f761`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 6.66 |
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
| hash | 88ec022c9ee0d46c8ae7ea0b4d1b36669694e8e6dc02286af3826f3c7aa43dd9 | static_analysis |
| ip | 211.118.82.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

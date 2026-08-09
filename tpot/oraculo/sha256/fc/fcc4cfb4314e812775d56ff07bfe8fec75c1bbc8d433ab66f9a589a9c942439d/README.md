# 🧬 Payload Analysis

`fcc4cfb4314e812775d56ff07bfe8fec75c1bbc8d433ab66f9a589a9c942439d`

## 📌 Resumen

Artefacto de 3.4 KiB. Entropía registrada: 6.64. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Limpieza. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `fcc4cfb4314e812775d56ff07bfe8fec75c1bbc8d433ab66f9a589a9c942439d`
- **MD5:** `5d153a20eb970b870724f6330c10c752`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.4 KiB |
| Entropía | 6.64 |
| Strings | 27 |

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
| hash | fcc4cfb4314e812775d56ff07bfe8fec75c1bbc8d433ab66f9a589a9c942439d | static_analysis |
| ip | 42.55.169.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.

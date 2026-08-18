# MIPS cad9e90 YARA detection note

Fuente: `firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/`

Esta nota apunta a la regla YARA y al material de análisis del payload ELF32 MIPS confirmado.

## Payload

```text
SHA256: cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41
Tipo: ELF32 MIPS payload / malware-like artifact
Fuente: telemetría controlada de honeypot
Estado: promovido como firma confirmada
```

## Regla disponible

```text
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/yara/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41.yar
```

## Material relacionado

```text
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/README.md
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/analysis/
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/evidence/
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/metadata/
firmas/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/raw/
```

## Uso defensivo

Esta detección sirve como punto de entrada para:

- validación en laboratorio,
- comparación contra muestras MIPS observadas,
- documentación del flujo de promoción de una firma,
- demostración de análisis de payload confirmado.

## Regla humana

La regla YARA no debe vivir escondida adentro de una carpeta de hash sin contexto. Este archivo existe para que alguien entre a `detecciones/` y encuentre de inmediato qué detección existe y a qué payload apunta.

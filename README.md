# Parcial: CI/CD y Calidad de Código

Descripción
-----------
Pequeño proyecto de ejemplo que contiene una calculadora simple en Python
(`src/calculator.py`) y su conjunto de pruebas (`tests/`). El objetivo es
mostrar cómo integrar comprobaciones de calidad (linter y formateador),
pruebas unitarias y un pipeline de CI que valida todo esto automáticamente.

Contenido principal
-------------------
- `src/` : código fuente (módulo `calculator`).
- `tests/` : pruebas unitarias con `pytest`.
- `pyproject.toml` y `requirements.txt` : configuración y dependencias.
- `.github/workflows/ci-quality.yml` : workflow de CI para el proyecto.

Requisitos
----------
- Python 3.10+ (recomendado 3.11)
- pip
- Docker (para ejecutar workflows localmente con `act`)

Instalación rápida (Windows - PowerShell)
---------------------------------------
```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Uso básico
----------
Ejecutar pruebas:
```powershell
& .venv\Scripts\python.exe -m pytest -q
```

Comprobar estilo y formato:
```powershell
& .venv\Scripts\python.exe -m flake8 src/ tests/
& .venv\Scripts\python.exe -m black --check src/ tests/
```

Cobertura de pruebas
--------------------
Comprobar que la cobertura cumple el umbral configurado (80% por defecto):
```powershell
& .venv\Scripts\python.exe -m pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

Ejecutar workflow localmente (opcional)
--------------------------------------
```powershell
act push
```
---

**Estudiante:** Zully Beleño Lopez  
**Fecha:** 20 Nov 2025  
**Repositorio:** https://github.com/ZullyMelisa14/parcial-ci-cd.git
# RESPUESTAS - Parcial Calidad de Software Avanzado
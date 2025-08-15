# Thoughtful AI Challenge – Package Sorter

A function to classify packages based on their dimensions and mass, following the rules from **Thoughtful's robotic automation factory** challenge described here: [FDE Technical Screen](https://thoughtfulautomation.notion.site/FDE-Technical-Screen-12af43a78fa480af8d97c2fc9478cb18 ).

---

## 📋 Problem Summary

A robotic arm needs to classify packages into three different stacks:

- **STANDARD** → packages that are neither heavy nor bulky.
- **SPECIAL** → packages that are heavy **or** bulky.
- **REJECTED** → packages that are both heavy **and** bulky.

### Criteria:
- **Bulky** if:
  - Volume (`width × height × length`) ≥ `1_000_000 cm³`, **or**
  - Any dimension ≥ `150 cm`.
- **Heavy** if:
  - Mass ≥ `20 kg`.

---

## 🗂 Project Structure
~~~

thoughtful-sort/
├─ src/
│ └─ app/
│   ├─ init.py # Public API (exports sort)
│   └─ PackageSorting.py # sort() implementation + validations
├─ tests/
│ └─ test_sorter.py # Unit tests with pytest
| └─ test_sanity.py # environment check
├─ pyproject.toml # Dependencies and tool configuration
├─ poetry.lock # lock down the exact versions of all dependencies
├─ README.md # This file
|─ pytest.ini # pytests configs
└─ .gitignore
~~~

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
~~~

git clone https://github.com/your-username/thoughtful-sort.git
cd thoughtful-sort
~~~

### 2️⃣ Create a virtual environment with Poetry

~~~

poetry install
This creates an isolated venv and installs all dependencies declared in pyproject.toml.
~~~


### 3️⃣ Run the function interactively using the terminal
~~~

poetry run python

from src.app.PackageSorting import sort
sort(100, 100, 100, 10) # Output: "SPECIAL"
~~~

## 🧪 Running Tests
The project uses pytest for unit testing.

~~~

poetry run pytest
~~~
Run with coverage:
~~~
poetry add --group dev pytest-cov
poetry run pytest --cov=src --cov-report=term-missing
~~~

⚙️ API

`sort(width: float, height: float, length: float, mass: float) -> str`
~~~

Parameters:
width, height, length → package dimensions in centimeters.
mass → package mass in kilograms.
~~~

Returns:

`"STANDARD", "SPECIAL" or "REJECTED".`

Example:
~~~
sort(50, 50, 50, 10)       # "STANDARD"
sort(150, 10, 10, 5)       # "SPECIAL" (bulky)
sort(100, 100, 100, 20)    # "REJECTED" (bulky & heavy)
~~~

✅ Input Validation
The function raises a ValueError when:

`-Any parameter is None.`

`-Value is not numeric or cannot be converted to float.`

`-Value is not finite (inf, -inf, NaN).`

`-Value is negative.`

🛠 Tools Used
Python 3.11+
~~~

Poetry – dependency management
pytest – unit testing
pytest-cov - test coverage
pytest-env - environment variable setting and setting
~~~
# package-sorter
# package-sorter

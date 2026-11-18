# 📘 Assignment: Searching Algorithms in Python

## 🎯 Objective

Implemente e compare busca linear e busca binária em listas usando Python. Você praticará percorrer estruturas de dados e avaliar quando cada algoritmo é adequado.

## 📝 Tasks

### 🛠️ Implementar a busca linear

#### Descrição
Complete `linear_search(values, target)` para encontrar um valor em uma lista que pode estar desordenada.

#### Requisitos
A função concluída deve:

- Retornar o índice da primeira ocorrência de `target` em `values`.
- Retornar `-1` se `target` não estiver na lista.
- Funcionar com listas vazias e listas com valores repetidos.
- Percorrer a lista sem alterá-la.

Exemplos:

```python
linear_search([8, 3, 6, 1], 6)  # 2
linear_search([8, 3, 6, 1], 5)  # -1
```

### 🛠️ Implementar a busca binária

#### Descrição
Complete `binary_search(values, target)` para localizar um valor em uma lista ordenada em ordem crescente. Use a estratégia de dividir repetidamente o intervalo de busca pela metade.

#### Requisitos
A função concluída deve:

- Retornar o índice de `target` se ele estiver em `values`.
- Retornar `-1` se `target` não estiver na lista.
- Funcionar quando o alvo estiver no início, no fim ou no meio da lista, e também quando a lista estiver vazia.
- Manter a lista sem alterações e assumir que ela já está ordenada; não é necessário ordenar os valores.
- Usar busca binária, reduzindo o intervalo de busca a cada etapa, em vez de percorrer todos os elementos em sequência.

Exemplos:

```python
binary_search([1, 3, 6, 8, 10], 8)  # 3
binary_search([1, 3, 6, 8, 10], 5)  # -1
```

### 🛠️ Comparar os algoritmos

#### Descrição
Compare os dois métodos e explique quando escolher cada um.

#### Requisitos
A resposta concluída deve:

- Explicar por que a busca binária exige que a lista esteja ordenada.
- Comparar o crescimento do trabalho da busca linear, $O(n)$, com o da busca binária, $O(\log n)$.
- Descrever uma situação em que a busca linear é uma escolha adequada, mesmo existindo busca binária.

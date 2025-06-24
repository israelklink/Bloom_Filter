![logo do Bloom](https://www.andreinc.net/assets/images/2022-03-01-on-implementing-bloom-filters-in-c/bloomexplained.drawio.png)

# Bloom Filter

## Principais componentes necessários para a implementação dos Bloom Filter:

- **Capacidade** *i*: O número máximo de elementos que podem ser armazenados no BF.

- **Número de funções de hash** *k*: O número de funções de hash necessárias para fazer o hash dos elementos.

- **Número de bits** *m*: O número de bits na matriz necessários para representar o BF.

- **Taxa de erro**: como os BF são estruturas de dados probabilísticas, precisamos definir a taxa máxima desejada de falsos positivos.

## Probabilidade de falso positivo e relação entre i, m, k

Assume uma função que seleciona cada posição do array com a mesma probabilidade. Considerando *m* que há um número de bits no array, a probabilidade de selecionar um bit é 1/*m* e a probabilidade de não definir um bit é:

$$
p=1-\frac{1}{m}
$$

E há *k* funções hash e *i* strings. Então, a probabilidade agora de **não definir um bit** pela função hash *k* é:

$$
p=(1-\frac{1}{m})^{k*i}
$$

O falso positivo, ou seja, definir um *bit* por engano para uma *string*:


$$
P_{fp}=1- p = 1-(1-\frac{1}{m})^{k*i}
$$

Para *k* vezes, temos a taxa de erro para uma *string*:

$$
Erro_{rate}=(1-(1-\frac{1}{m})^{k*i})^k
$$

**Queremos saber o comportamento do erro quando** $m \to \infty$.

Vale lembrar que: 

$$
(1-\frac{1}{m})^{k*i} \approx e^{- \frac{k \cdot i}{m}}
$$

Substituindo, temos:

$$
Erro_{rate} \approx (1-e^{- \frac{k \cdot i}{m}})^k
$$

Agora, tome o limite:

$$
\lim_{m \to \infty} \left(1 - e^{- \frac{k \cdot i}{m}} \right)^k
$$

como $\frac{ki}{m} \to 0$

então: 

$$e^{- \frac{k \cdot i}{m}} \to 1 \quad \Rightarrow \quad 1 - e^{- \frac{k \cdot i}{m}} \to 0$$

Logo:

$$\lim_{m \to \infty} \text{Erro}_{\text{rate}} = 0$$

Portanto, quanto maior o número de bits $m$, menor a taxa de falso positivo, tendendo a zero.


**Para $m \to 1$**, temos:

A taxa de erro se torna 1, que é $100\%$. Ou seja, todas as posições de *bits* são rapidamente ocupadas, e qualquer novo teste pode aparecer um falso positivo.




**Para maior entendimento do BF** - [Simulação]( https://programaai.github.io/bloom-filters/)
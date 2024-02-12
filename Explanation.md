On a 2d plane, the position of a point $P$ relative to a triangle $\Delta ABC$ can be represented by 3 vectors:
- $A$, a vertex of $\Delta ABC$
- $v_{B}$, a vector parallel to $\overline{AB}$
- $v_{C}$ is a vector parallel to $\overline{AC}$

Using these vectors, the position of $P$ can be represented as:
$$P = A + v_{B} + v_{C} $$

$v_{B}$ is the distance of $P$ from $A$ towards $B$. So, it can be rewritten as $w_{B} * (B-A)$, where $w_{B}$ is an unknown scalar and $(B-A)$ is the difference in position between $A$ and $B$. Similarly, $v_{C}$ can be rewritten as $w_{C} * (C-A)$. So the equation can be rewritten as:
$$P = A + w_{B} (B-A) + w_{C} (C-A)$$

With $w_{B}$ and $w_{C}$, it is much easier to see if $P$ is in $\Delta ABC$. $P$ must be outside $\Delta ABC$ if $w_{B}$ or $w_{C}$ is greater than 1 or less than 0. And if $P$ is outside of the triangle where $\overline{BC}$ is between itself and $A$, then $w_{B} + w_{C} > 1$. This means $P$ is inside $\Delta ABC$ only if all these requirements are true:
- $0 \leq w_{B} \leq 1$
- $0 \leq w_{C} \leq 1$
- $w_{B} + w_{C} \leq 1$

To calculate $w_{B}$ and $w_{C}$, the vectors must first be expanded into their x and y components. For now, the x component is all that is needed.
$$P = A + w_{B} (B-A) + w_{C} (C-A)$$

$$\therefore P_{x} = A_{x} + w_{B} (B_{x}-A_{x}) + w_{C} (C_{x}-A_{x}), P_{y} = A_{y} + w_{B} (B_{y}-A_{y}) + w_{C} (C_{y}-A_{y})$$

Then, by rearranging the x-position equation to make $w_{B}$ the subject, we can substitute $w_{B}$ into the y-axis equation to make $w_{C}$ the only unknown variable.
$$P_{x} = A_{x} + w_{B} (B_{x}-A_{x}) + w_{C} (C_{x}-A_{x})$$

$$ -w_{B} (B_{x}-A_{x}) = A_{x} + w_{C} (C_{x}-A_{x}) - P_{x} $$

$$ w_{B} (B_{x}-A_{x}) = P_{x} - A_{x} - w_{C} (C_{x}-A_{x})$$

$$ w_{B} = \frac {P_{x} - A_{x} - w_{C} (C_{x}-A_{x})} {B_{x}-A_{x}} $$
